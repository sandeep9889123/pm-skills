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
import re
import statistics
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

try:  # direct: python evaluation/run_benchmark.py
    from benchmark_utils import (
        case_fingerprint,
        get_case,
        load_json,
        subject_fingerprint,
        suite_fingerprint,
        validate_manifest,
        validate_suite,
    )
    from score_output import score_case
except ModuleNotFoundError:  # imported from repository-root tests/tools
    from evaluation.benchmark_utils import (
        case_fingerprint,
        get_case,
        load_json,
        subject_fingerprint,
        suite_fingerprint,
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
    tool_digest = hashlib.sha256(
        json.dumps(tools, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:12]
    return (
        f"{model.get('provider','?')}/{model.get('name','?')}@{model.get('version','?')}"
        f" | config={configuration} | tools={tool_state}:{tool_digest}"
        f" | commit={str(record.get('repository_commit', '?'))[:12]}"
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
        "suite_fingerprint",
        "subject_paths",
        "subject_fingerprint",
        "repository_commit",
        "model",
        "run_index",
        "planned_runs",
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
    if record.get("suite_fingerprint") != suite_fingerprint(suite):
        errors.append("suite_fingerprint mismatch; rubric or suite changed")

    subject_paths = record.get("subject_paths")
    expected_subjects = (
        manifest.get("workflow_subjects", {}).get(case.get("workflow")) if case else None
    )
    if subject_paths != expected_subjects:
        errors.append("subject_paths do not match manifest workflow mapping")
    elif isinstance(subject_paths, list):
        try:
            if record.get("subject_fingerprint") != subject_fingerprint(REPO_ROOT, subject_paths):
                errors.append("subject_fingerprint mismatch; tested workflow changed")
        except Exception as exc:
            errors.append(f"subject files invalid: {exc}")

    commit = record.get("repository_commit")
    if not isinstance(commit, str) or not re.fullmatch(r"[a-f0-9]{40}", commit):
        errors.append("repository_commit must be a 40-character lowercase git SHA")
    else:
        resolved_commit = subprocess.run(
            ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
            cwd=REPO_ROOT,
            capture_output=True,
        )
        if resolved_commit.returncode != 0:
            errors.append("repository_commit does not resolve to a commit in this repository")

    model = record.get("model")
    if not isinstance(model, dict):
        errors.append("model must be an object")
    else:
        for field in ("provider", "name", "version"):
            if not isinstance(model.get(field), str) or not model.get(field, "").strip():
                errors.append(f"model.{field} is required")
        if not isinstance(model.get("configuration"), str) or not model.get("configuration", "").strip():
            errors.append("model.configuration is required")

    run_index = record.get("run_index")
    if not isinstance(run_index, int) or run_index < 1:
        errors.append("run_index must be integer >= 1")
    planned_runs = record.get("planned_runs")
    minimum_runs = int(manifest.get("minimum_runs_per_case", 3))
    if not isinstance(planned_runs, int) or planned_runs < minimum_runs:
        errors.append(f"planned_runs must be integer >= {minimum_runs}")
    elif isinstance(run_index, int) and run_index > planned_runs:
        errors.append("run_index cannot exceed planned_runs")

    if manifest.get("require_fresh_session") and record.get("fresh_session") is not True:
        errors.append("fresh_session must be true for Wave 7 benchmark runs")

    captured_at = record.get("captured_at")
    try:
        parsed_at = datetime.fromisoformat(str(captured_at))
        if parsed_at.tzinfo is None:
            errors.append("captured_at must include a timezone")
    except ValueError:
        errors.append("captured_at must be an ISO-8601 timestamp")

    delivery = record.get("prompt_delivery")
    if not isinstance(delivery, dict):
        errors.append("prompt_delivery object is required")
        delivery = {}
    if delivery.get("corrective_followup_used") is not False:
        errors.append("corrective follow-up used; not a first-run observation")
    if delivery.get("additional_context_given") is not False:
        errors.append("additional context beyond frozen case was supplied")
    if case is not None:
        invoked = delivery.get("workflow_invoked")
        if invoked != case.get("workflow"):
            errors.append(
                f"workflow_invoked {invoked!r} does not match frozen workflow {case.get('workflow')!r}"
            )

    tools = record.get("tool_profile")
    if not isinstance(tools, dict) or not isinstance(tools.get("profile"), str) or not tools.get("profile", "").strip():
        errors.append("tool_profile.profile is required")
    elif not isinstance(tools.get("tools_enabled"), bool):
        errors.append("tool_profile.tools_enabled must be boolean for qualification runs")

    evaluator_blinded = record.get("evaluator_blinded")
    if evaluator_blinded is not None and not isinstance(evaluator_blinded, bool):
        errors.append("evaluator_blinded must be boolean or null")

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
                if not expected_hash:
                    errors.append("judgement_sha256 is required when judgement_path is set")
                elif sha256_file(judgement_path) != expected_hash:
                    errors.append("judgement SHA-256 mismatch")
                judgement = load_json(judgement_path)
                evaluator = judgement.get("evaluator") if isinstance(judgement, dict) else None
                if isinstance(evaluator, dict) and record.get("evaluator_blinded") != evaluator.get("blinded"):
                    errors.append("record evaluator_blinded does not match judgement evaluator.blinded")
        except ValueError as exc:
            errors.append(f"judgement invalid: {exc}")

    capture = record.get("capture")
    if capture is not None:
        if not isinstance(capture, dict):
            errors.append("capture must be an object when present")
        else:
            mode = capture.get("mode")
            if mode == "automated_api":
                if capture.get("adapter") not in {"openai-responses", "anthropic-messages"}:
                    errors.append("capture.adapter is unsupported")
                endpoint = capture.get("endpoint")
                if not isinstance(endpoint, str) or not endpoint.startswith("https://"):
                    errors.append("capture.endpoint must use https")
                for prefix in ("prompt_bundle", "request", "provider_response"):
                    path_value = capture.get(f"{prefix}_path")
                    expected_hash = capture.get(f"{prefix}_sha256")
                    if not isinstance(path_value, str) or not path_value.strip():
                        errors.append(f"capture.{prefix}_path is required")
                        continue
                    try:
                        artifact_path = repo_path(path_value)
                        if not artifact_path.is_file():
                            errors.append(f"capture artifact missing: {path_value}")
                        elif sha256_file(artifact_path) != expected_hash:
                            errors.append(f"capture.{prefix}_sha256 mismatch")
                    except ValueError as exc:
                        errors.append(f"capture.{prefix}_path invalid: {exc}")
                for field in ("provider_request_id", "response_model"):
                    if not isinstance(capture.get(field), str) or not capture.get(field, "").strip():
                        errors.append(f"capture.{field} is required")
                if not isinstance(capture.get("request_parameters"), dict):
                    errors.append("capture.request_parameters must be an object")
            elif mode == "manual_ui":
                if not isinstance(capture.get("interface"), str) or not capture.get("interface", "").strip():
                    errors.append("capture.interface is required for manual_ui")
                attestation = capture.get("operator_attestation")
                if not isinstance(attestation, dict):
                    errors.append("capture.operator_attestation is required for manual_ui")
                else:
                    for field in (
                        "fresh_session",
                        "first_response_only",
                        "no_corrective_followup",
                        "no_extra_context",
                        "raw_output_unedited",
                    ):
                        if attestation.get(field) is not True:
                            errors.append(f"capture.operator_attestation.{field} must be true")
                for prefix in ("manual_plan", "prompt_bundle", "manual_prompt"):
                    path_value = capture.get(f"{prefix}_path")
                    expected_hash = capture.get(f"{prefix}_sha256")
                    if not isinstance(path_value, str) or not path_value.strip():
                        errors.append(f"capture.{prefix}_path is required")
                        continue
                    try:
                        artifact_path = repo_path(path_value)
                        if not artifact_path.is_file():
                            errors.append(f"capture artifact missing: {path_value}")
                        elif sha256_file(artifact_path) != expected_hash:
                            errors.append(f"capture.{prefix}_sha256 mismatch")
                    except ValueError as exc:
                        errors.append(f"capture.{prefix}_path invalid: {exc}")
            else:
                errors.append("capture.mode must be automated_api or manual_ui")

    return errors, case, {"raw_output": raw_output, "judgement": judgement}


def summarize_case_results(
    case: dict[str, Any],
    results: list[dict[str, Any]],
    minimum_runs: int,
    run_indices: set[int] | None = None,
) -> dict[str, Any]:
    weighted = [r["weighted_score"] for r in results if r.get("weighted_score") is not None]
    hard_failures = sum(1 for r in results if not r["hard_gates"]["passed"])
    pass_runs = sum(1 for r in results if r.get("status") == "PASS")
    expected_indices = set(range(1, minimum_runs + 1))
    observed_indices = run_indices or set()
    exact_slots = observed_indices == expected_indices
    complete = exact_slots and all(r.get("status") not in {
        "UNSCORED",
        "HARD_GATE_PASS_UNSCORED",
        "INVALID_JUDGEMENT",
    } for r in results)
    passed = complete and all(r.get("status") == "PASS" for r in results)
    hard_gate_outcomes = {
        r.get("hard_gates", {}).get("passed")
        for r in results
        if isinstance(r.get("hard_gates", {}).get("passed"), bool)
    }
    judged_outcomes = {
        r.get("status") == "PASS"
        for r in results
        if r.get("status") not in {"UNSCORED", "HARD_GATE_PASS_UNSCORED", "HARD_GATE_FAIL"}
    }
    mixed_hard_gate = len(hard_gate_outcomes) > 1
    mixed_pass_fail = len(judged_outcomes) > 1 or mixed_hard_gate
    return {
        "case_id": case["id"],
        "family": case.get("family", "legacy"),
        "variant": case.get("variant", "LEGACY"),
        "runs": len(results),
        "minimum_runs": minimum_runs,
        "missing_runs": len(expected_indices - observed_indices),
        "observed_run_indices": sorted(observed_indices),
        "missing_run_indices": sorted(expected_indices - observed_indices),
        "unexpected_run_indices": sorted(observed_indices - expected_indices),
        "hard_gate_failures": hard_failures,
        "run_passes": pass_runs,
        "complete": complete,
        "passed": passed,
        "mean_weighted_score": round(statistics.mean(weighted), 2) if weighted else None,
        "min_weighted_score": min(weighted) if weighted else None,
        "max_weighted_score": max(weighted) if weighted else None,
        "score_range": round(max(weighted) - min(weighted), 2) if len(weighted) >= 2 else 0.0 if weighted else None,
        "mixed_hard_gate": mixed_hard_gate,
        "mixed_pass_fail": mixed_pass_fail,
        "run_details": [
            {
                "run_index": r.get("run_index"),
                "status": r.get("status"),
                "weighted_score": r.get("weighted_score"),
                "hard_gate_passed": r.get("hard_gates", {}).get("passed"),
                "missing_required": r.get("hard_gates", {}).get("missing_required", []),
                "matched_forbidden": r.get("hard_gates", {}).get("matched_forbidden", []),
                "captured_at": r.get("captured_at"),
                "evaluator": r.get("evaluator"),
            }
            for r in sorted(results, key=lambda value: value.get("run_index", 0))
        ],
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
    by_case_indices: dict[str, set[int]] = defaultdict(set)
    duplicate_slots: list[str] = []
    seen_slots: set[tuple[str, int]] = set()
    planned_run_values = {
        item.get("record", {}).get("planned_runs", minimum_runs) for item in records
    }
    plan_consistent = len(planned_run_values) == 1
    planned_runs = next(iter(planned_run_values)) if plan_consistent and planned_run_values else minimum_runs
    if not isinstance(planned_runs, int) or planned_runs < minimum_runs:
        plan_consistent = False
        planned_runs = minimum_runs

    for item in records:
        case_id = item["case"]["id"]
        slot = (case_id, item["record"]["run_index"])
        if slot in seen_slots:
            duplicate_slots.append(f"{case_id}:run-{slot[1]}")
            continue
        seen_slots.add(slot)
        enriched_score = dict(item["score"])
        enriched_score.update(
            {
                "run_index": slot[1],
                "captured_at": item["record"].get("captured_at"),
            }
        )
        by_case[case_id].append(enriched_score)
        by_case_indices[case_id].add(slot[1])

    case_summaries = []
    for case in suite.get("cases", []):
        case_summaries.append(
            summarize_case_results(
                case,
                by_case.get(case["id"], []),
                planned_runs,
                by_case_indices.get(case["id"], set()),
            )
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
                round(sum(1 for x in base if x["passed"]) / len(base), 4)
                if base and all(x["complete"] for x in base)
                else None
            ),
            "mutation_pass_rate": (
                round(sum(1 for x in mutation if x["passed"]) / len(mutation), 4)
                if mutation and all(x["complete"] for x in mutation)
                else None
            ),
        }

    capture_complete = (
        not duplicate_slots
        and plan_consistent
        and missing_slots == 0
    )
    coverage_complete = capture_complete and complete_cases == len(case_summaries)
    hard_rate = hard_failures / total_runs if total_runs else None
    case_pass_rate = (
        passed_cases / len(case_summaries)
        if coverage_complete and case_summaries
        else None
    )
    mean_score = round(statistics.mean(all_scores), 2) if all_scores else None

    release = manifest.get("release_gate", {})
    repository_commits = sorted({item["record"].get("repository_commit") for item in records})
    suite_fingerprints = sorted({item["record"].get("suite_fingerprint") for item in records})
    evaluator_profiles = sorted(
        {
            (
                item["score"]["evaluator"].get("id", "?"),
                item["score"]["evaluator"].get("type", "?"),
                item["score"]["evaluator"].get("version", "?"),
                item["score"]["evaluator"].get("blinded"),
            )
            for item in records
            if isinstance(item["score"].get("evaluator"), dict)
        }
    )
    minimum_family_pass_rate = float(release.get("minimum_family_pass_rate", 0))
    family_floor_failures = (
        sorted(
            family
            for family, data in families.items()
            if data["passed_cases"] / data["cases"] < minimum_family_pass_rate
        )
        if coverage_complete
        else []
    )
    maximum_unstable_cases = int(release.get("maximum_unstable_cases", 0))
    if not coverage_complete:
        release_status = "INCOMPLETE"
    elif hard_rate is None or mean_score is None or case_pass_rate is None:
        release_status = "INCOMPLETE"
    elif (
        hard_rate <= float(release.get("maximum_hard_gate_failure_rate", 0))
        and case_pass_rate >= float(release.get("minimum_case_pass_rate", 0.9))
        and mean_score >= float(release.get("minimum_mean_weighted_score", 90))
        and not family_floor_failures
        and len(unstable_cases) <= maximum_unstable_cases
    ):
        release_status = "PASS"
    else:
        release_status = "FAIL"

    return {
        "model_key": key,
        "repository_commits": repository_commits,
        "suite_fingerprints": suite_fingerprints,
        "evaluator_profiles": [
            {"id": x[0], "type": x[1], "version": x[2], "blinded": x[3]}
            for x in evaluator_profiles
        ],
        "release_status": release_status,
        "capture_complete": capture_complete,
        "coverage_complete": coverage_complete,
        "planned_runs_per_case": planned_runs,
        "run_plan_consistent": plan_consistent,
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
        "family_floor_failures": family_floor_failures,
        "families": families,
        "cases": case_summaries,
    }


def markdown_report(report: dict[str, Any]) -> str:
    lines = [
        f"# Behavioral Benchmark Report: {report['benchmark_id']}",
        "",
        f"Definition status: **{report['definition_status']}**",
        f"Mutation policy: **{report['mutation_policy']}**",
        f"Invalid run records: **{len(report['invalid_records'])}**",
        "",
    ]
    if report["invalid_records"]:
        lines.extend(["## Integrity Errors", ""])
        for item in report["invalid_records"]:
            lines.append(f"- `{item['path']}`: {'; '.join(item['errors'])}")
        lines.append("")
    if report.get("definition_errors"):
        lines.extend(["## Definition Errors", ""])
        for error in report["definition_errors"]:
            lines.append(f"- {error}")
        lines.append("")

    for model in report["models"]:
        lines.extend(
            [
                f"## {model['model_key']}",
                "",
                f"Benchmark status: **{model['release_status']}**",
                f"Repository commit(s): {', '.join(model['repository_commits'])}",
                f"Suite fingerprint(s): {', '.join(model['suite_fingerprints'])}",
                "Evaluator profile(s): " + (
                    ", ".join(
                        f"{x['id']} ({x['type']} {x['version']}, blinded={x['blinded']})"
                        for x in model["evaluator_profiles"]
                    ) or "None yet"
                ),
                f"Raw capture complete: **{model['capture_complete']}**",
                f"Coverage complete: **{model['coverage_complete']}**",
                f"Planned runs per case: {model['planned_runs_per_case']}",
                f"Run plan consistent: **{model['run_plan_consistent']}**",
                f"Complete cases: {model['complete_cases']}/{model['expected_cases']}",
                f"Missing run slots: {model['missing_run_slots']}",
                f"Hard-gate failure rate: {model['hard_gate_failure_rate']}",
                f"Case pass rate: {model['case_pass_rate']}",
                f"Mean weighted score: {model['mean_weighted_score']}",
                f"Family floor failures: {', '.join(model['family_floor_failures']) or 'None'}",
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
        lines.extend(
            [
                "",
                "### Case and run detail",
                "",
                "| Case | Variant | Complete | Passed | Runs | Scores | Range | Hard fails | Missing slots |",
                "|---|---|---:|---:|---|---|---:|---:|---|",
            ]
        )
        for case in model["cases"]:
            run_statuses = ", ".join(
                f"{run['run_index']}:{run['status']}" for run in case["run_details"]
            ) or "None"
            scores = ", ".join(
                str(run["weighted_score"])
                for run in case["run_details"]
                if run["weighted_score"] is not None
            ) or "None"
            missing = ", ".join(str(x) for x in case["missing_run_indices"]) or "None"
            lines.append(
                f"| {case['case_id']} | {case['variant']} | {case['complete']} | {case['passed']} | "
                f"{run_statuses} | {scores} | {case['score_range']} | {case['hard_gate_failures']} | {missing} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Interpretation policy",
            "",
            "A PASS applies only to the recorded benchmark scope, model/version/configuration, tool profile, and frozen case distribution.",
            "It is not a guarantee of hallucination-free behavior or universal PM decision quality.",
            "BASE and MUTATION are unpaired family-level challenge strata in this suite. Their rates are descriptive and are not a causal robustness delta.",
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
            require_fixtures=True,
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
            score = score_case(
                suite,
                case,
                payload["raw_output"],
                payload["judgement"],
                record.get("raw_output_sha256"),
            )
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
        "mutation_policy": manifest.get("mutation_policy"),
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
