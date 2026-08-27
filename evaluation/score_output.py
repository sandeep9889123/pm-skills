#!/usr/bin/env python3
"""Score captured PM-skill outputs against golden adversarial cases.

Layer A: deterministic hard gates using deliberately narrow regex checks.
Layer B: weighted 100-point judgement supplied by a human or independent model.

This runner does not call an LLM. It is intentionally model-agnostic so raw
Claude, Codex, Gemini, or other outputs can be captured and compared without
changing the benchmark cases.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DEFAULT_CASES = ROOT / "cases.json"
SCORER_REVISION = "2.0-context-aware-forbidden-gates"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def get_case(suite: dict[str, Any], case_id: str) -> dict[str, Any]:
    for case in suite.get("cases", []):
        if case.get("id") == case_id:
            return case
    raise KeyError(f"Unknown case_id: {case_id}")


def regex_present(pattern: str, text: str) -> bool:
    try:
        return re.search(pattern, text, flags=re.MULTILINE) is not None
    except re.error as exc:
        raise ValueError(f"Invalid regex {pattern!r}: {exc}") from exc


def _sentence_for_match(text: str, start: int, end: int) -> tuple[str, int]:
    """Return a bounded sentence/line window and its absolute start offset."""
    left = max(text.rfind("\n", 0, start), text.rfind(".", 0, start), text.rfind("?", 0, start), text.rfind("!", 0, start))
    right_candidates = [position for marker in ("\n", ".", "?", "!") if (position := text.find(marker, end)) >= 0]
    right = min(right_candidates) + 1 if right_candidates else len(text)
    sentence_start = left + 1
    return text[sentence_start:right], sentence_start


def _is_meta_or_rejected_mention(sentence: str, match_start: int, match_end: int) -> bool:
    """Suppress forbidden phrases that are explicitly rejected or cited as bad examples.

    Regex gates are narrow tripwires, not semantic judges. A phrase such as
    "does not support calling this an uncontested market" must not be scored the
    same way as an affirmative conclusion. The exclusions stay deliberately
    narrow and do not excuse contradictory claims such as "coverage is
    incomplete, but there are no competitors."
    """
    prefix = sentence[:match_start].lower()
    suffix = sentence[match_end:].lower()
    whole = sentence.lower()

    # "Do not hesitate/delay" is not a refusal and must never create an escape.
    plain_whole = re.sub(r"[*_`]+", "", whole)
    plain_prefix = re.sub(r"[*_`]+", "", prefix)
    scrubbed_prefix = re.sub(r"\bdo not (?:hesitate|delay)\b", "", plain_prefix)
    rejected_before = re.search(
        r"(?:"
        r"\b(?:does|do|is|are|was|were|should|must|can|cannot|can't|will|would)\s+not\b"
        r"|\b(?:reject|rejected|unsupported|unsubstantiated|prohibited|avoid|dangerous|"
        r"false precision|weak approach|critical flaw|flaws? in|not evidence|not support|"
        r"cannot conclude|do not infer|do not publish|do not state|must not repeat|"
        r"statements? such as|writing|calling|claiming|label(?:ing)?)\b"
        r")[^\n.!?]{0,180}$",
        scrubbed_prefix,
    )
    rejected_after = re.match(
        r"[^\n.!?]{0,100}\b(?:claim|conclusion|statement)?\s*(?:is|are)?\s*"
        r"(?:unsupported|unverified|false|dangerous|prohibited|not supported)\b",
        suffix,
    )
    explicit_refusal = bool(re.search(r"\bdo not publish\b", whole))
    adversatives = list(re.finditer(r"\b(?:but|however|yet|nevertheless)\b", plain_whole))
    if (rejected_before or explicit_refusal) and any(
        marker.start() < match_end for marker in adversatives
    ):
        return False
    return bool(rejected_before or rejected_after or explicit_refusal)


def forbidden_regex_present(pattern: str, text: str) -> bool:
    """Return true only for non-negated, non-meta forbidden assertions."""
    try:
        expression = re.compile(pattern, flags=re.MULTILINE)
    except re.error as exc:
        raise ValueError(f"Invalid regex {pattern!r}: {exc}") from exc
    for match in expression.finditer(text):
        # A broad `.*` gate crossing a sentence/question boundary is not a
        # single prohibited assertion. Score each bounded claim separately.
        if re.search(r"[?\n]", match.group(0)):
            continue
        sentence, sentence_start = _sentence_for_match(text, match.start(), match.end())
        local_start = match.start() - sentence_start
        local_end = match.end() - sentence_start
        if not _is_meta_or_rejected_mention(sentence, local_start, local_end):
            return True
    return False


def evaluate_hard_gates(case: dict[str, Any], output: str) -> dict[str, Any]:
    gates = case.get("hard_gates", {})
    missing_required = [
        pattern
        for pattern in gates.get("required_patterns", [])
        if not regex_present(pattern, output)
    ]
    matched_forbidden = [
        pattern
        for pattern in gates.get("forbidden_patterns", [])
        if forbidden_regex_present(pattern, output)
    ]
    return {
        "passed": not missing_required and not matched_forbidden,
        "missing_required": missing_required,
        "matched_forbidden": matched_forbidden,
    }


def validate_judgement(
    suite: dict[str, Any],
    case: dict[str, Any],
    judgement: dict[str, Any],
    raw_output_sha256: str,
) -> tuple[float, list[str]]:
    errors: list[str] = []
    if judgement.get("case_id") != case.get("id"):
        errors.append(
            f"judgement case_id {judgement.get('case_id')!r} does not match {case.get('id')!r}"
        )

    if str(suite.get("schema_version", "1.0")).startswith("2"):
        if judgement.get("rubric_version") != suite.get("rubric_version"):
            errors.append("judgement rubric_version does not match suite")
        if judgement.get("raw_output_sha256") != raw_output_sha256:
            errors.append("judgement raw_output_sha256 does not match scored output")
        evaluator = judgement.get("evaluator")
        if not isinstance(evaluator, dict):
            errors.append("judgement evaluator object is required")
        else:
            for field in ("id", "type", "version"):
                if not isinstance(evaluator.get(field), str) or not evaluator.get(field, "").strip():
                    errors.append(f"judgement evaluator.{field} is required")
            if evaluator.get("type") not in {"human", "model"}:
                errors.append("judgement evaluator.type must be human or model")
            if evaluator.get("independent") is not True:
                errors.append("judgement evaluator.independent must be true")
            if not isinstance(evaluator.get("blinded"), bool):
                errors.append("judgement evaluator.blinded must be boolean")

    rubric = suite.get("rubric", {})
    dimensions = judgement.get("dimensions", {})
    score = 0.0

    for name, spec in rubric.items():
        item = dimensions.get(name)
        if not isinstance(item, dict):
            errors.append(f"missing judgement dimension: {name}")
            continue
        raw = item.get("score")
        rationale = item.get("rationale", "")
        evidence = item.get("evidence", [])
        if not isinstance(raw, (int, float)) or raw < 0 or raw > 5:
            errors.append(f"{name}: score must be numeric from 0 to 5")
            continue
        if not isinstance(rationale, str) or not rationale.strip():
            errors.append(f"{name}: rationale is required")
        if str(suite.get("schema_version", "1.0")).startswith("2") and (
            not isinstance(evidence, list)
            or not evidence
            or not all(isinstance(x, str) and x.strip() for x in evidence)
        ):
            errors.append(f"{name}: at least one output evidence reference is required")
        weight = spec.get("weight", 0)
        score += float(weight) * (float(raw) / 5.0)

    extra = set(dimensions) - set(rubric)
    if extra:
        errors.append(f"unknown judgement dimensions: {sorted(extra)}")

    return round(score, 2), errors


def score_case(
    suite: dict[str, Any],
    case: dict[str, Any],
    output: str,
    judgement: dict[str, Any] | None = None,
    raw_output_sha256: str | None = None,
) -> dict[str, Any]:
    hard = evaluate_hard_gates(case, output)
    threshold = case.get("pass_threshold", suite.get("default_pass_threshold", 90))

    result: dict[str, Any] = {
        "case_id": case["id"],
        "workflow": case.get("workflow"),
        "failure_family": case.get("failure_family"),
        "hard_gates": hard,
        "threshold": threshold,
        "weighted_score": None,
        "status": "UNSCORED",
        "judgement_errors": [],
    }

    if judgement is None:
        result["status"] = "HARD_GATE_PASS_UNSCORED" if hard["passed"] else "HARD_GATE_FAIL"
        return result

    raw_output_sha256 = raw_output_sha256 or hashlib.sha256(output.encode("utf-8")).hexdigest()
    weighted_score, errors = validate_judgement(
        suite, case, judgement, raw_output_sha256
    )
    result["weighted_score"] = weighted_score
    result["judgement_errors"] = errors
    result["evaluator"] = judgement.get("evaluator")

    if errors:
        result["status"] = "INVALID_JUDGEMENT"
    elif not hard["passed"]:
        result["status"] = "FAIL_HARD_GATE"
    elif weighted_score >= threshold:
        result["status"] = "PASS"
    else:
        result["status"] = "FAIL_SCORE"

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, dest="case_id")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--judgement", type=Path)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON only")
    args = parser.parse_args()

    suite = load_json(args.cases)
    try:
        case = get_case(suite, args.case_id)
    except KeyError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if not args.output.is_file():
        print(f"Output file not found: {args.output}", file=sys.stderr)
        return 2

    output = args.output.read_text(encoding="utf-8")
    judgement = load_json(args.judgement) if args.judgement else None
    result = score_case(
        suite,
        case,
        output,
        judgement,
        hashlib.sha256(args.output.read_bytes()).hexdigest(),
    )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Case: {result['case_id']} ({result['workflow']})")
        print(f"Hard gates: {'PASS' if result['hard_gates']['passed'] else 'FAIL'}")
        if result["hard_gates"]["missing_required"]:
            print("Missing required signals:")
            for pattern in result["hard_gates"]["missing_required"]:
                print(f"  - {pattern}")
        if result["hard_gates"]["matched_forbidden"]:
            print("Forbidden signals detected:")
            for pattern in result["hard_gates"]["matched_forbidden"]:
                print(f"  - {pattern}")
        if result["weighted_score"] is not None:
            print(f"Weighted score: {result['weighted_score']}/100 (threshold {result['threshold']})")
        else:
            print("Weighted score: UNSCORED, add --judgement for the 100-point rubric")
        if result["judgement_errors"]:
            print("Judgement errors:")
            for error in result["judgement_errors"]:
                print(f"  - {error}")
        print(f"Status: {result['status']}")

    return 0 if result["status"] in {"PASS", "HARD_GATE_PASS_UNSCORED"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
