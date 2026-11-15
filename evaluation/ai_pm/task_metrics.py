#!/usr/bin/env python3
"""Summarize supplied task costs and elapsed latency offline; no provider calls."""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path


def amount(value, field):
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise ValueError(f"{field} must be an explicit finite nonnegative number")
    try:
        number = Decimal(str(value))
    except InvalidOperation as error:
        raise ValueError(f"invalid {field}") from error
    if not number.is_finite() or number < 0:
        raise ValueError(f"{field} must be finite and nonnegative")
    return number


def summarize(rows, *, provenance="unknown"):
    if provenance not in {"observed", "synthetic", "unknown"}:
        raise ValueError("invalid provenance")
    rows = list(rows)
    if not rows:
        raise ValueError("no task records")
    seen, currencies, latencies = set(), set(), []
    total, successes, partial = Decimal(0), 0, []
    for index, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            raise ValueError(f"row {index}: expected an object")
        ident = row.get("task_id")
        if not isinstance(ident, str) or not ident.strip() or ident in seen:
            raise ValueError("task_id must be nonempty and unique")
        seen.add(ident)
        if not isinstance(row.get("success"), bool):
            raise ValueError("success must be a supplied boolean, not a string or inferred claim")
        currency = row.get("currency", "")
        if not isinstance(currency, str) or not re.fullmatch(r"[A-Z]{3}", currency):
            raise ValueError("supply an explicit three-letter currency code")
        currencies.add(currency)
        if row.get("cost_basis") not in {"complete", "partial"}:
            raise ValueError("cost_basis must explicitly be complete or partial")
        if row["cost_basis"] == "partial":
            partial.append(ident)
        total += amount(row.get("cost"), "cost")
        latencies.append(amount(row.get("duration_ms"), "duration_ms"))
        successes += int(row["success"])
    if len(currencies) != 1:
        raise ValueError("mixed currencies require separate reports; no exchange rate is assumed")
    latencies.sort()
    n = len(rows)
    p95 = latencies[math.ceil(0.95 * n) - 1]
    fmt = lambda v: format(v, "f") if v is not None else None
    return {
        "schema_version": "1.0", "status": "FIXTURE_ONLY" if provenance == "synthetic" else "DESCRIPTIVE",
        "provenance": provenance, "provenance_verified_by_tool": False,
        "attempted_tasks": n, "verified_successes_supplied": successes,
        "success_verification": "Operator supplied; calculator does not inspect final state.",
        "currency": next(iter(currencies)), "reported_total_cost": fmt(total),
        "cost_basis": "partial" if partial else "complete", "partial_cost_task_ids": partial,
        "reported_cost_per_attempted_task": fmt(total / n),
        "known_cost_per_successful_task": fmt(total / successes) if successes else None,
        "complete_cost_per_successful_task": fmt(total / successes) if successes and not partial else None,
        "latency_ms": {"n": n, "min": fmt(latencies[0]), "max": fmt(latencies[-1]),
                       "p95": fmt(p95), "percentile_method": "nearest-rank",
                       "basis": "Supplied end-to-end wall-clock task durations, not sums of overlapping spans."},
        "limitations": ["No task success, price source or cost completeness is independently verified.",
                        "All supplied task costs, including failures, contribute to the total.",
                        "Small samples do not establish a production SLO or superiority."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jsonl", type=Path)
    parser.add_argument("--provenance", choices=("observed", "synthetic", "unknown"), required=True)
    args = parser.parse_args(argv)
    try:
        with args.jsonl.open(encoding="utf-8") as stream:
            rows = [json.loads(line) for line in stream if line.strip()]
        result = summarize(rows, provenance=args.provenance)
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
