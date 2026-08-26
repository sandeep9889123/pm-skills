#!/usr/bin/env python3
"""Aggregate repeated PM Skills behavioral benchmark runs.

This runner does not call an LLM. It validates captured first-run records,
verifies prompt/output hashes, applies deterministic hard gates plus optional
weighted judgements, and reports failure rates by model, family, and mutation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any

try:  # direct: python evaluation/run_benchmark.py
    from benchmark_utils import (
        case_fingerprint,
        get_case,
        load_json,
        validate_manifest,
        validate_suite,
    )
    from score_output import score_case
except ModuleNotFoundError:  # imported from repository-root tests/tools
    from evaluation.benchmark_utils import (
        case_fingerprint,
        get_case,
        load_json,
        validate_manifest,
        validate_suite,
    )
    from evaluation.score_output import score_case

EVAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = EVAL_DIR.parent
DEFAULT_MANIFEST = EVAL_DIR / "benchmark_manifest.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def model_key(record: dict[str, Any]) -> str:
    model = record.get("model") or {}
    tools = record.get("tool_profile") or {}
    configuration = model.get("configuration") or "default"
    tool_state = tools.get("profile") or (
        "tools-on" if tools.get("tools_enabled") is True else
        "tools-off" if tools.get("tools_enabled") is False else
        "tools-unknown"
    )
    return (
        f"{model.get('provider','?')}/{model.get('name','?')}@{model.get('version','?')}"
        f" | config={configuration} | tools={tool_state}"
    )


def repo_path(value: str) -> Path:
    path = (REPO_ROOT / value).resolve()
    try:
        path.relative_to(REPO_ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"path escapes repository: {value}") from exc
    return path


def validate_run_record(
    record: Any,
    *,
    manifest: dict[str, Any],
    suite: dict[str, Any],
    record_path: Path,
) -> tuple[list[str], dict[str, Any] | None, dict[str, Any] | None]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return ["record must be a JSON object"], None, None

    required = [
        "record_id",
        "benchmark_id",
        "suite_path",
        "case_id",
        "case_fingerprint",
        "model",
        "run_index",
        "captured_at",
        "fresh_session",
        "raw_output_path",
        "raw_output_sha256",
    ]
    for field in required:
        if field not in record:
            errors.append(f"missing required field {field}")

    if record.get("benchmark_id") != manifest.get("benchmark_id"):
        errors.append("benchmark_id does not match manifest")
    if record.get("suite_path") != manifest.get("primary_suite"):
        errors.append("suite_path does not match primary suite")

    try:
        case = get_case(suite, str(record.get("case_id")))
    except KeyError:
        errors.append(f"unknown case_id {record.get('case_id')!r}")
        case = None

    if case is not None and record.get("case_fingerprint") != case_fingerprint(case):
        errors.append("case_fingerprint mismatch; case stimulus changed or record is stale")

    model = record.get("model")
    if not isinstance(model, dict):
        errors.append("model must be an object")
    else:
        for field in ("provider", "name", "version"):
            if not isinstance(model.get(field), str) or not model.get(field, "").strip():
                errors.append(f"model.{field} is required")

    run_index = record.get("run_index")
    if not isinstance(run_index, int) or run_index < 1:
        errors.append("run_index must be integer >= 1")

    if manifest.get("require_fresh_session") and record.get("fresh_session") is not True:
        errors.append("fresh_session must be true for Wave 7 benchmark runs")

    delivery = record.get("prompt_delivery") or {}
    if delivery.get("corrective_followup_used") is True:
        errors.append("corrective follow-up used; not a first-run observation")
    if delivery.get("additional_context_given") is True:
        errors.append("additional context beyond frozen case was supplied")
    if case is not None:
        invoked = delivery.get("workflow_invoked")
        if invoked and invoked != case.get("workflow"):
            errors.append(
                f"workflow_invoked {invoked!r} does not match frozen workflow {case.get('workflow')!r}"
            )

    raw_output = None
    raw_value = record.get("raw_output_path")
    if not isinstance(raw_value, str) or not raw_value.strip():
        errors.append("raw_output_path must be a non-empty string")
    else:
        try:
            raw_path = repo_path(raw_value)
            if not raw_path.is_file():
                errors.append(f"raw output missing: {raw_value}")
            else:
                observed_hash = sha256_file(raw_path)
                if observed_hash != record.get("raw_output_sha256"):
                    errors.append("raw output SHA-256 mismatch")
                raw_output = raw_path.read_text(encoding="utf-8")
        except (ValueError, UnicodeDecodeError) as exc:
            errors.append(f"raw output invalid: {exc}")

    judgement = None
    judgement_value = record.get("judgement_path")
    if judgement_value:
        try:
            judgement_path = repo_path(judgement_value)
            if not judgement_path.is_file():
                errors.append(f"judgement missing: {judgement_value}")
            else:
                expected_hash = record.get("judgement_sha256")
                if expected_hash and sha256_file(judgement_path) != expected_hash:
                    errors.append("judgement SHA-256 mismatch")
                judgement = load_json(judgement_path)
        except ValueError as exc:
            errors.append(f"judgement invalid: {exc}")

    if manifest.get("require_judgement_for_full_benchmark") and not judgement_value:
        errors.append("weighted judgement missing")

    return errors, case, {"raw_output": raw_output, "judgement": judgement}


def summarize_case_results(
    case: dict[str, Any],
    results: list[dict[str, Any]],
    minimum_runs: int,
) -> dict[str, Any]:
    weighted = [r["weighted_score"] for r in results if r.get("weighted_score") is not None]
    hard_failures = sum(1 for r in results if not r["hard_gates"]["passed"])
    pass_runs = sum(1 for r in results if r.get("status") == "PASS")
    complete = len(results) >= minimum_runs and all(r.get("status") not in {
        "UNSCORED",
        "HARD_GATE_PASS_UNSCORED",
        "INVALID_JUDGEMENT",
    } for r in results)
    passed = complete and all(r.get("status") == "PASS" for r in results)
    return {
        "case_id": case["id"],
        "family": case.get("family", "legacy"),
        "variant": case.get("variant", "LEGACY"),
        "runs": len(results),
        "minimum_runs": minimum_runs,
        "missing_runs": max(0, minimum_runs - len(results)),
        "hard_gate_failures": hard_failures,
        "run_passes": pass_runs,
        "complete": complete,
        "passed": passed,
        "mean_weighted_score": round(statistics.mean(weighted), 2) if weighted else None,
        "min_weighted_score": min(weighted) if weighted else None,
        "max_weighted_score": max(weighted) if weighted else None,
        "score_range": round(max(weighted) - min(weighted), 2) if len(weighted) >= 2 else 0.0 if weighted else None,
        "mixed_pass_fail": len({r.get("status") == "PASS" for r in results}) > 1,
    }


def aggregate_model(
    key: str,
    records: list[dict[str, Any]],
    *,
    suite: dict[str, Any],
    manifest: dict[str, Any],
) -> dict[str, Any]:
    minimum_runs = int(manifest.get("minimum_runs_per_case", 3))
    by_case: dict[str, list[dict[str, Any]]] = defaultdict(list)
    duplicate_slots: list[str] = []
    seen_slots: set[tuple[str, int]] = set()

    for item in records:
        case_id = item["case"]["id"]
        slot = (case_id, item["record"]["run_index"])
        if slot in seen_slots:
            duplicate_slots.append(f"{case_id}:run-{slot[1]}")
            continue
        seen_slots.add(slot)
        by_case[case_id].append(item["score"])

    case_summaries = []
    for case in suite.get("cases", []):
        case_summaries.append(
            summarize_case_results(case, by_case.get(case["id"], []), minimum_runs)
        )

    all_scores = [
        score
        for summary in case_summaries
        for score in [summary.get("mean_weighted_score")]
        if score is not None
    ]
    total_runs = sum(summary["runs"] for summary in case_summaries)
    hard_failures = sum(summary["hard_gate_failures"] for summary in case_summaries)
    missing_slots = sum(summary["missing_runs"] for summary in case_summaries)
    complete_cases = sum(1 for summary in case_summaries if summary["complete"])
    passed_cases = sum(1 for summary in case_summaries if summary["passed"])
    unstable_cases = [
        summary["case_id"]
        for summary in case_summaries
        if summary["mixed_pass_fail"] or (summary.get("score_range") or 0) > 10
    ]

    families: dict[str, dict[str, Any]] = {}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for summary in case_summaries:
        grouped[summary["family"]].append(summary)
    for family, items in sorted(grouped.items()):
        family_scores = [x["mean_weighted_score"] for x in items if x["mean_weighted_score"] is not None]
        base = [x for x in items if x["variant"] == "BASE"]
        mutation = [x for x in items if x["variant"] == "MUTATION"]
        families[family] = {
            "cases": len(items),
            "complete_cases": sum(1 for x in items if x["complete"]),
            "passed_cases": sum(1 for x in items if x["passed"]),
            "mean_weighted_score": round(statistics.mean(family_scores), 2) if family_scores else None,
            "hard_gate_failures": sum(x["hard_gate_failures"] for x in items),
            "base_pass_rate": (
                round(sum(1 for x in base if x["passed"]) / len(base), 4) if base else None
            ),
            "mutation_pass_rate": (
                round(sum(1 for x in mutation if x["passed"]) / len(mutation), 4) if mutation else None
            ),
        }

    coverage_complete = (
        not duplicate_slots
        and complete_cases == len(case_summaries)
        and missing_slots == 0
    )
    hard_rate = hard_failures / total_runs if total_runs else None
    case_pass_rate = passed_cases / len(case_summaries) if case_summaries else None
    mean_score = round(statistics.mean(all_scores), 2) if all_scores else None

    release = manifest.get("release_gate", {})
    if not coverage_complete:
        release_status = "INCOMPLETE"
    elif hard_rate is None or mean_score is None or case_pass_rate is None:
        release_status = "INCOMPLETE"
    elif (
        hard_rate <= float(release.get("maximum_hard_gate_failure_rate", 0))
        and case_pass_rate >= float(release.get("minimum_case_pass_rate", 0.9))
        and mean_score >= float(release.get("minimum_mean_weighted_score", 90))
    ):
        release_status = "PASS"
    else:
        release_status = "FAIL"

    return {
        "model_key": key,
        "release_status": release_status,
        "coverage_complete": coverage_complete,
        "expected_cases": len(case_summaries),
        "complete_cases": complete_cases,
        "passed_cases": passed_cases,
        "case_pass_rate": round(case_pass_rate, 4) if case_pass_rate is not None else None,
        "total_valid_runs": total_runs,
        "missing_run_slots": missing_slots,
        "duplicate_slots": sorted(duplicate_slots),
        "hard_gate_failures": hard_failures,
        "hard_gate_failure_rate": round(hard_rate, 4) if hard_rate is not None else None,
        "mean_weighted_score": mean_score,
        "min_case_mean_score": min(all_scores) if all_scores else None,
        "max_case_mean_score": max(all_scores) if all_scores else None,
        "unstable_case_ids": unstable_cases,
        "families": families,
        "cases": case_summaries,
    }


def markdown_report(report: dict[str, Any]) -> str:
    lines = [
        f"# Behavioral Benchmark Report: {report['benchmark_id']}",
        "",
        f"Definition status: **{report['definition_status']}**",
        f"Invalid run records: **{len(report['invalid_records'])}**",
        "",
    ]
    if report["invalid_records"]:
        lines.extend(["## Integrity Errors", ""])
        for item in report["invalid_records"]:
            lines.append(f"- `{item['path']}`: {'; '.join(item['errors'])}")
        lines.append("")

    for model in report["models"]:
        lines.extend(
            [
                f"## {model['model_key']}",
                "",
                f"Benchmark status: **{model['release_status']}**",
                f"Coverage complete: **{model['coverage_complete']}**",
                f"Complete cases: {model['complete_cases']}/{model['expected_cases']}",
                f"Missing run slots: {model['missing_run_slots']}",
                f"Hard-gate failure rate: {model['hard_gate_failure_rate']}",
                f"Case pass rate: {model['case_pass_rate']}",
                f"Mean weighted score: {model['mean_weighted_score']}",
                "",
                "### Family breakdown",
                "",
                "| Family | Complete | Passed | Mean score | Hard fails | Base pass | Mutation pass |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for family, data in model["families"].items():
            lines.append(
                f"| {family} | {data['complete_cases']}/{data['cases']} | {data['passed_cases']}/{data['cases']} | "
                f"{data['mean_weighted_score']} | {data['hard_gate_failures']} | {data['base_pass_rate']} | {data['mutation_pass_rate']} |"
            )
        lines.extend(["", "### Unstable cases", ""])
        if model["unstable_case_ids"]:
            for case_id in model["unstable_case_ids"]:
                lines.append(f"- {case_id}")
        else:
            lines.append("- None observed")
        lines.append("")

    lines.extend(
        [
            "## Interpretation policy",
            "",
            "A PASS applies only to the recorded benchmark scope, model/version/configuration, tool profile, and frozen case distribution.",
            "It is not a guarantee of hallucination-free behavior or universal PM decision quality.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", type=Path, default=EVAL_DIR / "runs")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--md-out", type=Path)
    parser.add_argument("--json", action="store_true", help="Print report as JSON")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    definition_errors = validate_manifest(manifest)
    suite = load_json(REPO_ROOT / manifest.get("primary_suite", "evaluation/wave7_cases.json"))
    definition_errors.extend(
        validate_suite(
            suite,
            required_families=manifest.get("required_families", []),
            require_variants=True,
            minimum_cases=24,
        )
    )

    invalid_records: list[dict[str, Any]] = []
    valid_by_model: dict[str, list[dict[str, Any]]] = defaultdict(list)

    if args.runs.exists():
        for record_path in sorted(args.runs.rglob("*.run.json")):
            try:
                record = load_json(record_path)
            except Exception as exc:  # definition/integrity reporting, not silent skip
                invalid_records.append({"path": str(record_path), "errors": [str(exc)]})
                continue
            errors, case, payload = validate_run_record(
                record,
                manifest=manifest,
                suite=suite,
                record_path=record_path,
            )
            if errors or case is None or payload is None or payload["raw_output"] is None:
                invalid_records.append({"path": str(record_path), "errors": errors or ["unusable record"]})
                continue
            score = score_case(suite, case, payload["raw_output"], payload["judgement"])
            if score.get("judgement_errors"):
                invalid_records.append(
                    {
                        "path": str(record_path),
                        "errors": [f"judgement: {x}" for x in score["judgement_errors"]],
                    }
                )
                continue
            valid_by_model[model_key(record)].append(
                {"record": record, "case": case, "score": score, "path": str(record_path)}
            )

    models = [
        aggregate_model(key, records, suite=suite, manifest=manifest)
        for key, records in sorted(valid_by_model.items())
    ]

    report = {
        "benchmark_id": manifest.get("benchmark_id"),
        "definition_status": "VALID" if not definition_errors else "INVALID",
        "definition_errors": definition_errors,
        "invalid_records": invalid_records,
        "models": models,
    }

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if args.md_out:
        args.md_out.parent.mkdir(parents=True, exist_ok=True)
        args.md_out.write_text(markdown_report(report), encoding="utf-8")

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(markdown_report(report))

    if definition_errors or invalid_records:
        return 2
    if not models or any(model["release_status"] != "PASS" for model in models):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
