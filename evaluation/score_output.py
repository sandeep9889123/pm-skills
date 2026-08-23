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
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DEFAULT_CASES = ROOT / "cases.json"


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
        if regex_present(pattern, output)
    ]
    return {
        "passed": not missing_required and not matched_forbidden,
        "missing_required": missing_required,
        "matched_forbidden": matched_forbidden,
    }


def validate_judgement(
    suite: dict[str, Any], case: dict[str, Any], judgement: dict[str, Any]
) -> tuple[float, list[str]]:
    errors: list[str] = []
    if judgement.get("case_id") != case.get("id"):
        errors.append(
            f"judgement case_id {judgement.get('case_id')!r} does not match {case.get('id')!r}"
        )

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
        if not isinstance(raw, (int, float)) or raw < 0 or raw > 5:
            errors.append(f"{name}: score must be numeric from 0 to 5")
            continue
        if not isinstance(rationale, str) or not rationale.strip():
            errors.append(f"{name}: rationale is required")
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

    weighted_score, errors = validate_judgement(suite, case, judgement)
    result["weighted_score"] = weighted_score
    result["judgement_errors"] = errors

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
    result = score_case(suite, case, output, judgement)

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
