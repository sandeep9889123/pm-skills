#!/usr/bin/env python3
"""Validate Wave 7 benchmark definitions without requiring model run outputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmark_utils import case_fingerprint, load_json, validate_manifest, validate_suite

EVAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = EVAL_DIR.parent
DEFAULT_MANIFEST = EVAL_DIR / "benchmark_manifest.json"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    errors = validate_manifest(manifest)

    primary_path = REPO_ROOT / manifest.get("primary_suite", "evaluation/wave7_cases.json")
    primary = load_json(primary_path)
    errors.extend(
        validate_suite(
            primary,
            required_families=manifest.get("required_families", []),
            require_variants=True,
            minimum_cases=24,
        )
    )

    regression_path_value = manifest.get("regression_suite")
    regression = None
    if regression_path_value:
        regression = load_json(REPO_ROOT / regression_path_value)
        errors.extend(
            f"regression: {error}"
            for error in validate_suite(regression, require_variants=False, minimum_cases=10)
        )

    fingerprints = {
        case["id"]: case_fingerprint(case)
        for case in primary.get("cases", [])
        if isinstance(case, dict) and case.get("id")
    }

    systemic = manifest.get("systemic_case_ids", [])
    missing_systemic = sorted(set(systemic) - set(fingerprints))
    if missing_systemic:
        errors.append(f"manifest systemic_case_ids missing from primary suite: {missing_systemic}")

    result = {
        "status": "VALID" if not errors else "INVALID",
        "benchmark_id": manifest.get("benchmark_id"),
        "primary_cases": len(primary.get("cases", [])),
        "regression_cases": len(regression.get("cases", [])) if regression else 0,
        "required_families": manifest.get("required_families", []),
        "case_fingerprints": fingerprints,
        "errors": errors,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Benchmark: {result['benchmark_id']}")
        print(f"Primary cases: {result['primary_cases']}")
        print(f"Regression cases: {result['regression_cases']}")
        print(f"Status: {result['status']}")
        for error in errors:
            print(f"- {error}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
