#!/usr/bin/env python3
"""Offline arithmetic for supplied labels; never calls a model or certifies a judge."""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import Counter
from pathlib import Path

REQUIRED = ("case_id", "group_id", "split", "human_label", "judge_label")
PROVENANCE = ("human-reviewed", "synthetic", "unknown")


def wilson(successes: int, total: int) -> list[float] | None:
    """95% Wilson interval, conditional on independent binomial observations."""
    if not total:
        return None
    z = 1.959963984540054
    p = successes / total
    denom = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denom
    half = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denom
    return [max(0.0, center - half), min(1.0, center + half)]


def read_labels(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        names = reader.fieldnames or []
        if len(names) != len(set(names)) or not set(REQUIRED).issubset(names):
            raise ValueError("unique CSV headers must include " + ", ".join(REQUIRED))
        rows = list(reader)
        if any(None in row for row in rows):
            raise ValueError("CSV row has more values than headers")
        return rows


def score_rows(rows, *, split="test", provenance="unknown", heldout_attested=False,
               independent_groups_attested=False):
    if split not in {"train", "dev", "test"} or provenance not in PROVENANCE:
        raise ValueError("invalid split or label provenance")
    normalized = []
    seen = set()
    group_splits = {}
    for index, row in enumerate(rows, 1):
        if not isinstance(row, dict) or any(not isinstance(row.get(k), str) for k in REQUIRED):
            raise ValueError(f"row {index}: missing or non-string required field")
        item = {k: row[k].strip() for k in REQUIRED}
        if not all(item.values()):
            raise ValueError(f"row {index}: empty required field")
        if item["case_id"] in seen:
            raise ValueError("duplicate case_id: " + item["case_id"])
        seen.add(item["case_id"])
        if item["split"] not in {"train", "dev", "test"}:
            raise ValueError("invalid split: " + item["split"])
        if item["human_label"] not in {"PASS", "FAIL", "UNRESOLVED"}:
            raise ValueError("invalid human_label: " + item["human_label"])
        if item["judge_label"] not in {"PASS", "FAIL", "ABSTAIN"}:
            raise ValueError("invalid judge_label: " + item["judge_label"])
        old = group_splits.setdefault(item["group_id"], item["split"])
        if old != item["split"]:
            raise ValueError("group crosses data splits: " + item["group_id"])
        normalized.append(item)
    selected = [r for r in normalized if r["split"] == split]
    if not selected:
        raise ValueError("no rows in requested split")
    matrix = {k: 0 for k in ("TP", "FN", "TN", "FP")}
    exclusions = []
    for r in selected:
        human, judge = r["human_label"], r["judge_label"]
        if human == "UNRESOLVED" or judge == "ABSTAIN":
            exclusions.append({"case_id": r["case_id"], "human_label": human, "judge_label": judge})
        else:
            cell = {("FAIL", "FAIL"): "TP", ("FAIL", "PASS"): "FN",
                    ("PASS", "PASS"): "TN", ("PASS", "FAIL"): "FP"}[(human, judge)]
            matrix[cell] += 1
    tp, fn, tn, fp = (matrix[k] for k in ("TP", "FN", "TN", "FP"))
    groups = Counter(r["group_id"] for r in selected)
    interval_ok = independent_groups_attested and all(n == 1 for n in groups.values())

    def rate(num, den):
        return {"numerator": num, "denominator": den,
                "value": num / den if den else None,
                "wilson_95": wilson(num, den) if interval_ok else None}

    actual_fail = sum(r["human_label"] == "FAIL" for r in selected)
    if provenance == "synthetic":
        status = "FIXTURE_ONLY"
    elif provenance == "unknown":
        status = "UNVERIFIED_LABEL_PROVENANCE"
    elif split != "test":
        status = "DEVELOPMENT_ONLY"
    elif not heldout_attested:
        status = "UNVERIFIED_HOLDOUT"
    elif exclusions:
        status = "INCOMPLETE_LABELS"
    elif not (tp + fn) or not (tn + fp):
        status = "INCOMPLETE_CLASS_COVERAGE"
    else:
        status = "DESCRIPTIVE_ALIGNMENT"
    return {
        "schema_version": "1.0", "positive_class": "FAIL", "status": status,
        "readiness": "OWNER_REVIEW_REQUIRED",
        "provenance": provenance, "provenance_verified_by_tool": False,
        "heldout_attested": bool(heldout_attested), "split": split,
        "input_rows": len(normalized), "selected_rows": len(selected),
        "unique_groups": len(groups), "usable_binary_pairs": tp + fn + tn + fp,
        "unresolved_human_labels": sum(r["human_label"] == "UNRESOLVED" for r in selected),
        "judge_abstentions": sum(r["judge_label"] == "ABSTAIN" for r in selected),
        "excluded_from_binary_matrix": exclusions, "confusion_matrix": matrix,
        "binary_pair_coverage": rate(tp + fn + tn + fp, len(selected)),
        "conditional_binary_rates": {
            "failure_recall": rate(tp, tp + fn), "specificity": rate(tn, tn + fp),
            "false_pass_rate": rate(fn, tp + fn), "false_fail_rate": rate(fp, tn + fp),
            "precision": rate(tp, tp + fp), "agreement": rate(tp + tn, tp + fn + tn + fp)},
        "failure_detection_all_human_failures": rate(tp, actual_fail),
        "interval_note": ("Operator attests independent groups; tool does not verify population assumptions."
                          if interval_ok else "Intervals omitted: independent groups not attested or groups repeat."),
        "limitations": ["No acceptance thresholds are inferred.",
                        "Conditional binary rates exclude disclosed unresolved/abstained rows.",
                        "Class balance and sample selection affect operational interpretation."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--split", choices=("train", "dev", "test"), default="test")
    parser.add_argument("--provenance", choices=PROVENANCE, required=True)
    parser.add_argument("--heldout-attested", action="store_true")
    parser.add_argument("--independent-groups-attested", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = score_rows(read_labels(args.csv), split=args.split, provenance=args.provenance,
                            heldout_attested=args.heldout_attested,
                            independent_groups_attested=args.independent_groups_attested)
    except (OSError, ValueError, csv.Error) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
