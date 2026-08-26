#!/usr/bin/env python3
"""Create a tamper-evident behavioral benchmark run record.

This script records metadata after a raw first-run model output has been saved. It
hashes the frozen case stimulus, raw output, and optional judgement so later
benchmark aggregation can detect prompt/output edits.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from benchmark_utils import case_fingerprint, get_case, load_json, validate_manifest, validate_suite

EVAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = EVAL_DIR.parent
DEFAULT_MANIFEST = EVAL_DIR / "benchmark_manifest.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_relative(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError as exc:
        raise ValueError(f"benchmark artifacts must live inside repository: {path}") from exc


def slug(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip()).strip("-")
    return value or "run"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, dest="case_id")
    parser.add_argument("--output", required=True, type=Path, help="Raw model output file")
    parser.add_argument("--judgement", type=Path, help="Optional weighted judgement JSON")
    parser.add_argument("--provider", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--configuration")
    parser.add_argument("--run-index", required=True, type=int)
    parser.add_argument("--fresh-session", action="store_true")
    parser.add_argument("--tools-enabled", choices=["true", "false", "unknown"], default="unknown")
    parser.add_argument("--tool-profile")
    parser.add_argument("--tool-notes")
    parser.add_argument("--workflow-invoked")
    parser.add_argument("--corrective-followup", action="store_true")
    parser.add_argument("--additional-context", action="store_true")
    parser.add_argument("--evaluator-blinded", choices=["true", "false", "unknown"], default="unknown")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--record", type=Path, help="Destination .run.json")
    parser.add_argument("--notes")
    args = parser.parse_args()

    if args.run_index < 1:
        parser.error("--run-index must be >= 1")
    if not args.output.is_file():
        parser.error(f"raw output not found: {args.output}")
    if args.judgement and not args.judgement.is_file():
        parser.error(f"judgement not found: {args.judgement}")

    manifest = load_json(args.manifest)
    manifest_errors = validate_manifest(manifest)
    if manifest_errors:
        for error in manifest_errors:
            print(f"INVALID MANIFEST: {error}")
        return 2

    suite_path = REPO_ROOT / manifest["primary_suite"]
    suite = load_json(suite_path)
    suite_errors = validate_suite(
        suite,
        required_families=manifest.get("required_families", []),
        require_variants=True,
        minimum_cases=24,
    )
    if suite_errors:
        for error in suite_errors:
            print(f"INVALID SUITE: {error}")
        return 2

    try:
        case = get_case(suite, args.case_id)
    except KeyError as exc:
        print(str(exc))
        return 2

    tools_enabled = {"true": True, "false": False, "unknown": None}[args.tools_enabled]
    blinded = {"true": True, "false": False, "unknown": None}[args.evaluator_blinded]

    raw_output_path = repo_relative(args.output)
    judgement_path = repo_relative(args.judgement) if args.judgement else None
    model_key = f"{args.provider}-{args.model}-{args.version}"
    record_id = f"{slug(model_key)}:{args.case_id}:run-{args.run_index}"

    record = {
        "record_id": record_id,
        "benchmark_id": manifest["benchmark_id"],
        "suite_path": manifest["primary_suite"],
        "case_id": args.case_id,
        "case_fingerprint": case_fingerprint(case),
        "model": {
            "provider": args.provider,
            "name": args.model,
            "version": args.version,
            "configuration": args.configuration,
        },
        "run_index": args.run_index,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "fresh_session": args.fresh_session,
        "raw_output_path": raw_output_path,
        "raw_output_sha256": sha256_file(args.output),
        "judgement_path": judgement_path,
        "judgement_sha256": sha256_file(args.judgement) if args.judgement else None,
        "evaluator_blinded": blinded,
        "tool_profile": {
            "tools_enabled": tools_enabled,
            "profile": args.tool_profile,
            "notes": args.tool_notes,
        },
        "prompt_delivery": {
            "workflow_invoked": args.workflow_invoked or case.get("workflow"),
            "corrective_followup_used": args.corrective_followup,
            "additional_context_given": args.additional_context,
        },
        "notes": args.notes,
    }

    destination = args.record
    if destination is None:
        destination = args.output.with_name(
            f"{args.output.stem}.run-{args.run_index}.run.json"
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

    print(f"Recorded: {destination}")
    print(f"Case fingerprint: {record['case_fingerprint']}")
    print(f"Raw output SHA-256: {record['raw_output_sha256']}")
    if not args.fresh_session:
        print("WARNING: fresh_session=false; this run cannot satisfy full Wave 7 benchmark coverage.")
    if args.corrective_followup:
        print("WARNING: corrective follow-up used; this run is not a first-run benchmark observation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
