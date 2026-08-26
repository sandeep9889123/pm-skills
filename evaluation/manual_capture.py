#!/usr/bin/env python3
"""Prepare and validate zero-cost manual UI benchmark captures.

This script does not call any model API. It creates copy-paste prompt packs for
manual ChatGPT/Claude/local-model sessions and verifies that copied raw outputs
have the same tamper-evident metadata discipline as automated API captures.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:  # direct: python evaluation/manual_capture.py
    from benchmark_utils import get_case, load_json, suite_fingerprint
    from capture_baseline import build_prompt_bundle, canonical_json, repository_commit, sha256_bytes, write_json
except ModuleNotFoundError:  # imported from repository-root tests/tools
    from evaluation.benchmark_utils import get_case, load_json, suite_fingerprint
    from evaluation.capture_baseline import build_prompt_bundle, canonical_json, repository_commit, sha256_bytes, write_json

EVAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = EVAL_DIR.parent
DEFAULT_MANIFEST = EVAL_DIR / "benchmark_manifest.json"


class ManualCaptureError(RuntimeError):
    """Raised when manual capture would weaken the benchmark protocol."""


def slug(value: str) -> str:
    result = re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip()).strip("-")
    return result or "manual"


def repo_relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError as exc:
        raise ManualCaptureError(f"manual capture artifacts must live inside the repository: {path}") from exc


def repo_path(value: str) -> Path:
    path = (REPO_ROOT / value).resolve()
    try:
        path.relative_to(REPO_ROOT.resolve())
    except ValueError as exc:
        raise ManualCaptureError(f"path escapes repository: {value}") from exc
    return path


def select_cases(suite: dict[str, Any], case_ids: str, allow_all: bool) -> list[str]:
    all_case_ids = [case["id"] for case in suite["cases"]]
    if case_ids == "all":
        if not allow_all:
            raise ManualCaptureError("full-suite manual plan requires --allow-all")
        return all_case_ids
    requested = [value.strip() for value in case_ids.split(",") if value.strip()]
    if not requested or len(requested) != len(set(requested)):
        raise ManualCaptureError("--case-ids must contain unique comma-separated case IDs")
    unknown = sorted(set(requested) - set(all_case_ids))
    if unknown:
        raise ManualCaptureError(f"unknown case IDs: {unknown}")
    return [value for value in all_case_ids if value in set(requested)]


def plan_identity(plan: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in plan.items() if key != "created_at"}


def prepare_plan(path: Path, plan: dict[str, Any], resume: bool) -> None:
    if path.exists():
        observed = load_json(path)
        if plan_identity(observed) != plan_identity(plan):
            raise ManualCaptureError("existing manual plan differs; use a new output cell")
        if not resume:
            raise ManualCaptureError("manual plan already exists; use --resume to continue exact slots")
        return
    write_json(path, plan)


def prompt_text(case: dict[str, Any], bundle: dict[str, Any], run_index: int, planned_runs: int) -> str:
    return "\n".join(
        [
            "# Manual Wave 7 Prompt Pack",
            "",
            "Copy the SYSTEM section into the model's system/instructions field if available.",
            "Copy the USER section as the first and only user message in a fresh session.",
            "Do not paste expected behaviors, regex gates, rubric, prior outputs, or evaluator feedback.",
            "",
            f"Case: {case['id']}",
            f"Workflow: {case['workflow']}",
            f"Run slot: {run_index}/{planned_runs}",
            "",
            "## SYSTEM",
            "",
            bundle["model_visible"]["system"],
            "",
            "## USER",
            "",
            bundle["model_visible"]["user"],
            "",
        ]
    )


def prepare_manual(args: argparse.Namespace) -> Path:
    manifest = load_json(args.manifest)
    suite = load_json(REPO_ROOT / manifest["primary_suite"])
    case_ids = select_cases(suite, args.case_ids, args.allow_all)
    minimum_runs = int(manifest["minimum_runs_per_case"])
    if args.planned_runs < minimum_runs:
        raise ManualCaptureError(f"--planned-runs must be at least {minimum_runs}")

    tool_profile = {
        "tools_enabled": args.tools_enabled,
        "profile": args.tool_profile,
        "notes": args.tool_notes,
    }
    configuration = {
        "capture_mode": "manual_ui",
        "interface": args.interface,
        "model": args.model,
        "version": args.version,
        "tool_profile": tool_profile,
    }
    cell_name = slug(
        f"{args.provider}-{args.model}-{args.version}-manual-"
        f"{sha256_bytes(canonical_json(configuration).encode('utf-8'))[:12]}"
    )
    cell_dir = args.output_root / cell_name
    repo_relative(cell_dir)

    plan = {
        "schema_version": "1.0",
        "benchmark_id": manifest["benchmark_id"],
        "suite_fingerprint": suite_fingerprint(suite),
        "repository_commit": repository_commit(),
        "capture_mode": "manual_ui",
        "provider": args.provider,
        "model": args.model,
        "version": args.version,
        "interface": args.interface,
        "configuration": configuration,
        "case_ids": case_ids,
        "planned_runs": args.planned_runs,
        "execution_order": "run-index-then-suite-order",
        "retry_policy": "no retries; discard-and-disclose any failed UI attempt",
        "cost_policy": "zero paid API calls; manual subscription UI or local model only",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    prepare_plan(cell_dir / "manual-plan.json", plan, args.resume)

    for run_index in range(1, args.planned_runs + 1):
        for case_id in case_ids:
            case = get_case(suite, case_id)
            case_dir = cell_dir / case_id
            prompt_path = case_dir / f"run-{run_index}.manual-prompt.md"
            bundle_path = case_dir / f"run-{run_index}.prompt.json"
            output_path = case_dir / f"run-{run_index}.md"
            record_path = case_dir / f"run-{run_index}.run.json"
            if any(path.exists() for path in (prompt_path, bundle_path, output_path, record_path)) and not args.resume:
                raise ManualCaptureError(f"slot artifact already exists for {case_id}:run-{run_index}")
            if record_path.exists():
                continue
            bundle = build_prompt_bundle(case, manifest["workflow_subjects"][case["workflow"]])
            write_json(bundle_path, bundle)
            prompt_path.parent.mkdir(parents=True, exist_ok=True)
            prompt_path.write_text(prompt_text(case, bundle, run_index, args.planned_runs), encoding="utf-8")
            if not output_path.exists():
                output_path.write_text(
                    (
                        "<PASTE THE UNEDITED FIRST MODEL RESPONSE HERE. "
                        "Delete this placeholder before recording the run.>\n"
                    ),
                    encoding="utf-8",
                )
    return cell_dir


def placeholder_present(path: Path) -> bool:
    return "<PASTE THE UNEDITED FIRST MODEL RESPONSE HERE" in path.read_text(encoding="utf-8")


def record_manual(args: argparse.Namespace) -> Path:
    manifest = load_json(args.manifest)
    suite = load_json(REPO_ROOT / manifest["primary_suite"])
    cell_dir = args.cell.resolve()
    try:
        cell_dir.relative_to(REPO_ROOT.resolve())
    except ValueError as exc:
        raise ManualCaptureError("--cell must be inside the repository") from exc
    plan_path = cell_dir / "manual-plan.json"
    if not plan_path.is_file():
        raise ManualCaptureError(f"manual plan missing: {plan_path}")
    plan = load_json(plan_path)
    if plan.get("capture_mode") != "manual_ui":
        raise ManualCaptureError("manual plan capture_mode must be manual_ui")
    if plan.get("suite_fingerprint") != suite_fingerprint(suite):
        raise ManualCaptureError("manual plan suite fingerprint is stale")
    if plan.get("benchmark_id") != manifest["benchmark_id"]:
        raise ManualCaptureError("manual plan benchmark_id does not match manifest")

    case_ids = plan.get("case_ids")
    planned_runs = plan.get("planned_runs")
    if not isinstance(case_ids, list) or not all(isinstance(item, str) for item in case_ids):
        raise ManualCaptureError("manual plan case_ids must be a string array")
    if not isinstance(planned_runs, int) or planned_runs < int(manifest["minimum_runs_per_case"]):
        raise ManualCaptureError("manual plan planned_runs is invalid")

    recorded = 0
    for run_index in range(1, planned_runs + 1):
        for case_id in case_ids:
            case = get_case(suite, case_id)
            case_dir = cell_dir / case_id
            output_path = case_dir / f"run-{run_index}.md"
            record_path = case_dir / f"run-{run_index}.run.json"
            if record_path.exists():
                continue
            if not output_path.is_file():
                raise ManualCaptureError(f"manual raw output missing: {output_path}")
            if placeholder_present(output_path):
                raise ManualCaptureError(f"placeholder output was not replaced: {output_path}")
            command = [
                sys.executable,
                str(EVAL_DIR / "record_run.py"),
                "--case",
                case_id,
                "--output",
                str(output_path),
                "--provider",
                str(plan["provider"]),
                "--model",
                str(plan["model"]),
                "--version",
                str(plan["version"]),
                "--configuration",
                canonical_json(plan["configuration"]),
                "--run-index",
                str(run_index),
                "--planned-runs",
                str(planned_runs),
                "--fresh-session",
                "--tools-enabled",
                "true" if plan["configuration"]["tool_profile"]["tools_enabled"] else "false",
                "--tool-profile",
                str(plan["configuration"]["tool_profile"]["profile"]),
                "--tool-notes",
                str(plan["configuration"]["tool_profile"].get("notes") or "Manual UI capture."),
                "--workflow-invoked",
                case["workflow"],
                "--record",
                str(record_path),
                "--notes",
                "Zero-cost manual UI capture; weighted judgement pending.",
            ]
            completed = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True)
            if completed.returncode != 0:
                raise ManualCaptureError(f"record_run.py rejected manual slot: {completed.stderr}{completed.stdout}")
            record = load_json(record_path)
            bundle_path = case_dir / f"run-{run_index}.prompt.json"
            prompt_path = case_dir / f"run-{run_index}.manual-prompt.md"
            record["capture"] = {
                "mode": "manual_ui",
                "interface": plan["interface"],
                "manual_plan_path": repo_relative(plan_path),
                "manual_plan_sha256": sha256_bytes(plan_path.read_bytes()),
                "prompt_bundle_path": repo_relative(bundle_path),
                "prompt_bundle_sha256": sha256_bytes(bundle_path.read_bytes()),
                "manual_prompt_path": repo_relative(prompt_path),
                "manual_prompt_sha256": sha256_bytes(prompt_path.read_bytes()),
                "operator_attestation": {
                    "fresh_session": True,
                    "first_response_only": True,
                    "no_corrective_followup": True,
                    "no_extra_context": True,
                    "raw_output_unedited": True,
                },
            }
            write_json(record_path, record)
            recorded += 1
    print(f"Recorded manual slots: {recorded}")
    return cell_dir


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="Create zero-cost manual prompt packs")
    prepare.add_argument("--provider", required=True, help="Provider label, for example ChatGPT, Claude, Local")
    prepare.add_argument("--model", required=True, help="Visible model name")
    prepare.add_argument("--version", required=True, help="Visible model/version/date label")
    prepare.add_argument("--interface", required=True, help="UI used, for example chatgpt-web")
    prepare.add_argument("--case-ids", required=True, help="Comma-separated IDs or 'all'")
    prepare.add_argument("--allow-all", action="store_true")
    prepare.add_argument("--planned-runs", type=int, default=3)
    prepare.add_argument("--tools-enabled", action="store_true")
    prepare.add_argument("--tool-profile", default="manual-ui-no-external-tools")
    prepare.add_argument("--tool-notes", default="Manual UI run; no paid API calls.")
    prepare.add_argument("--output-root", type=Path, default=EVAL_DIR / "manual-runs")
    prepare.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    prepare.add_argument("--resume", action="store_true")

    record = subparsers.add_parser("record", help="Create run records for pasted manual outputs")
    record.add_argument("--cell", type=Path, required=True)
    record.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    return parser.parse_args(argv)


def main() -> int:
    try:
        args = parse_args()
        if args.command == "prepare":
            destination = prepare_manual(args)
        elif args.command == "record":
            destination = record_manual(args)
        else:  # pragma: no cover - argparse enforces choices
            raise ManualCaptureError(f"unsupported command: {args.command}")
    except ManualCaptureError as exc:
        print(f"MANUAL CAPTURE FAILED: {exc}", file=sys.stderr)
        return 2
    print(f"Manual capture cell: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
