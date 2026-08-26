#!/usr/bin/env python3
"""Validate PM cross-skill handoff envelopes using the Python standard library.

This validator checks structural and lineage proof obligations. It is not a truth
oracle and does not verify that external sources are factually correct.

Usage:
    python reliability/kernel/validate_handoff.py handoff.json
    python reliability/kernel/validate_handoff.py handoff.json --previous previous.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ALLOWED_STATES = {
    "FACT",
    "INFERENCE",
    "ASSUMPTION",
    "ESTIMATE",
    "UNKNOWN",
    "STALE",
    "TARGET",
    "PROPOSAL",
    "DECISION_THRESHOLD",
}
ALLOWED_TRANSFORMATIONS = {"ORIGINAL", "RESTATED", "DERIVED", "PROMOTED", "DOWNGRADED"}
ALLOWED_COVERAGE = {"COMPLETE FOR DECLARED SCOPE", "PARTIAL", "BLOCKED"}
ALLOWED_DECISIONS = {
    "PROCEED",
    "PROCEED WITH CONDITIONS",
    "TEST",
    "HOLD",
    "REFRAME",
    "NOT READY",
    "NO-GO",
}
RESTRICTED_PUBLISHABILITY = {"INTERNAL_ONLY", "CLIENT_CONFIDENTIAL", "REQUIRES_CLEARANCE"}
DOWNGRADE_STATES = {"UNKNOWN", "STALE"}


class ValidationError(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValidationError(f"handoff must be a JSON object: {path}")
    return data


def require(obj: dict[str, Any], key: str, where: str, errors: list[str]) -> Any:
    if key not in obj:
        errors.append(f"{where}: missing required field {key!r}")
        return None
    return obj[key]


def scope_signature(scope: Any) -> tuple[Any, ...]:
    if not isinstance(scope, dict):
        return (None, None, None, None, None)
    return tuple(
        scope.get(key)
        for key in ("geography", "segment", "population", "time_period", "product_or_workflow")
    )


def find_promotion(record: dict[str, Any], old_state: str, new_state: str) -> bool:
    history = record.get("promotion_history") or []
    if not isinstance(history, list):
        return False
    for item in history:
        if not isinstance(item, dict):
            continue
        evidence = item.get("new_evidence")
        if (
            item.get("from") == old_state
            and item.get("to") == new_state
            and isinstance(evidence, list)
            and len(evidence) > 0
            and all(isinstance(ref, str) and ref.strip() for ref in evidence)
        ):
            return True
    return False


def validate_record(record: Any, where: str, errors: list[str]) -> str | None:
    if not isinstance(record, dict):
        errors.append(f"{where}: record must be an object")
        return None

    claim_id = require(record, "claim_id", where, errors)
    claim = require(record, "claim", where, errors)
    state = require(record, "state", where, errors)
    source_class = require(record, "source_class", where, errors)
    scope = require(record, "scope", where, errors)
    downstream = require(record, "downstream_policy", where, errors)

    if not isinstance(claim_id, str) or not claim_id.strip():
        errors.append(f"{where}: claim_id must be a non-empty string")
    if not isinstance(claim, str) or not claim.strip():
        errors.append(f"{where}: claim must be a non-empty string")
    if state not in ALLOWED_STATES:
        errors.append(f"{where}: invalid state {state!r}")
    if not isinstance(source_class, str) or not source_class:
        errors.append(f"{where}: source_class must be a non-empty string")
    if not isinstance(scope, dict):
        errors.append(f"{where}: scope must be an object")

    if state == "ESTIMATE":
        method = record.get("estimate_method")
        if not isinstance(method, dict):
            errors.append(f"{where}: ESTIMATE requires estimate_method")
        else:
            if not method.get("formula"):
                errors.append(f"{where}: ESTIMATE requires estimate_method.formula")
            inputs = method.get("inputs")
            if not isinstance(inputs, list) or not inputs:
                errors.append(f"{where}: ESTIMATE requires non-empty estimate_method.inputs")
            if not method.get("units"):
                errors.append(f"{where}: ESTIMATE requires estimate_method.units")

    if not isinstance(downstream, dict):
        errors.append(f"{where}: downstream_policy must be an object")
    else:
        if downstream.get("may_promote_without_new_evidence") is not False:
            errors.append(f"{where}: may_promote_without_new_evidence must be false")
        if "may_restate" not in downstream:
            errors.append(f"{where}: downstream_policy.may_restate is required")

    publishability = record.get("publishability")
    if publishability == "PUBLIC" and state == "UNKNOWN":
        errors.append(f"{where}: UNKNOWN claim cannot be PUBLIC")

    history = record.get("promotion_history") or []
    if not isinstance(history, list):
        errors.append(f"{where}: promotion_history must be an array")
    else:
        for idx, item in enumerate(history):
            hwhere = f"{where}.promotion_history[{idx}]"
            if not isinstance(item, dict):
                errors.append(f"{hwhere}: must be an object")
                continue
            evidence = item.get("new_evidence")
            if not isinstance(evidence, list) or not evidence:
                errors.append(f"{hwhere}: new_evidence must be a non-empty array")

    return claim_id if isinstance(claim_id, str) else None


def validate_handoff(data: dict[str, Any], previous: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []

    for key in (
        "handoff_id",
        "producer",
        "intended_consumers",
        "decision_context",
        "coverage",
        "claims",
        "unresolved_p0",
        "decision",
        "prohibited_interpretations",
    ):
        require(data, key, "handoff", errors)

    coverage = data.get("coverage")
    if not isinstance(coverage, dict):
        errors.append("handoff.coverage: must be an object")
    else:
        status = coverage.get("status")
        if status not in ALLOWED_COVERAGE:
            errors.append(f"handoff.coverage: invalid status {status!r}")
        failures = coverage.get("tool_or_retrieval_failures") or []
        if failures and status == "COMPLETE FOR DECLARED SCOPE":
            errors.append("handoff.coverage: cannot be COMPLETE when tool/retrieval failures exist")

    decision = data.get("decision")
    if not isinstance(decision, dict):
        errors.append("handoff.decision: must be an object")
    else:
        status = decision.get("status")
        if status not in ALLOWED_DECISIONS:
            errors.append(f"handoff.decision: invalid status {status!r}")

    claims = data.get("claims")
    if not isinstance(claims, list):
        errors.append("handoff.claims: must be an array")
        claims = []

    seen_ids: set[str] = set()
    current_by_id: dict[str, dict[str, Any]] = {}
    all_parent_refs: list[tuple[str, str]] = []

    for idx, entry in enumerate(claims):
        where = f"handoff.claims[{idx}]"
        if not isinstance(entry, dict):
            errors.append(f"{where}: must be an object")
            continue
        record = entry.get("record")
        claim_id = validate_record(record, f"{where}.record", errors)
        transformation = entry.get("transformation")
        parents = entry.get("parent_claim_ids")

        if transformation not in ALLOWED_TRANSFORMATIONS:
            errors.append(f"{where}: invalid transformation {transformation!r}")
        if not isinstance(parents, list):
            errors.append(f"{where}: parent_claim_ids must be an array")
            parents = []
        elif len(parents) != len(set(parents)):
            errors.append(f"{where}: duplicate parent_claim_ids")

        if transformation == "DERIVED" and not parents:
            errors.append(f"{where}: DERIVED claim requires parent_claim_ids")
        if transformation == "ORIGINAL" and parents:
            errors.append(f"{where}: ORIGINAL claim must not have parent_claim_ids")
        if transformation == "PROMOTED":
            history = record.get("promotion_history") if isinstance(record, dict) else None
            if not isinstance(history, list) or not history:
                errors.append(f"{where}: PROMOTED claim requires promotion_history")

        if claim_id:
            if claim_id in seen_ids:
                errors.append(f"{where}: duplicate claim_id {claim_id!r}")
            seen_ids.add(claim_id)
            if isinstance(record, dict):
                current_by_id[claim_id] = record
            for parent in parents:
                if isinstance(parent, str):
                    all_parent_refs.append((claim_id, parent))

    previous_ids: set[str] = set()
    previous_by_id: dict[str, dict[str, Any]] = {}
    if previous:
        prev_claims = previous.get("claims") or []
        if isinstance(prev_claims, list):
            for entry in prev_claims:
                if not isinstance(entry, dict) or not isinstance(entry.get("record"), dict):
                    continue
                record = entry["record"]
                claim_id = record.get("claim_id")
                if isinstance(claim_id, str):
                    previous_ids.add(claim_id)
                    previous_by_id[claim_id] = record

    available_parent_ids = seen_ids | previous_ids
    for child, parent in all_parent_refs:
        if parent not in available_parent_ids:
            errors.append(f"claim {child!r}: unknown parent_claim_id {parent!r}")
        if child == parent:
            errors.append(f"claim {child!r}: claim cannot be its own parent")

    if previous:
        for claim_id, current in current_by_id.items():
            old = previous_by_id.get(claim_id)
            if not old:
                continue

            old_state = old.get("state")
            new_state = current.get("state")
            if old_state != new_state and new_state not in DOWNGRADE_STATES:
                if not find_promotion(current, str(old_state), str(new_state)):
                    errors.append(
                        f"claim {claim_id!r}: state changed {old_state!r} -> {new_state!r} "
                        "without matching promotion_history + new evidence"
                    )

            if scope_signature(old.get("scope")) != scope_signature(current.get("scope")):
                errors.append(
                    f"claim {claim_id!r}: material scope changed under the same claim_id; "
                    "create a new derived claim instead"
                )

            old_pub = old.get("publishability")
            new_pub = current.get("publishability")
            if old_pub in RESTRICTED_PUBLISHABILITY and new_pub == "PUBLIC":
                errors.append(
                    f"claim {claim_id!r}: restricted publishability {old_pub!r} -> PUBLIC "
                    "requires a new cleared/public claim record"
                )

    unresolved = data.get("unresolved_p0")
    if not isinstance(unresolved, list):
        errors.append("handoff.unresolved_p0: must be an array")
        unresolved = []
    else:
        for idx, item in enumerate(unresolved):
            where = f"handoff.unresolved_p0[{idx}]"
            if not isinstance(item, dict):
                errors.append(f"{where}: must be an object")
                continue
            claim_id = item.get("claim_id")
            if claim_id not in seen_ids:
                errors.append(f"{where}: claim_id must reference a current claim")
            if not item.get("blocker"):
                errors.append(f"{where}: blocker is required")
            if not item.get("evidence_needed"):
                errors.append(f"{where}: evidence_needed is required")

    decision_status = decision.get("status") if isinstance(decision, dict) else None
    if unresolved and decision_status == "PROCEED":
        errors.append("handoff.decision: PROCEED is not allowed while unresolved_p0 is non-empty")

    if isinstance(coverage, dict) and coverage.get("status") != "COMPLETE FOR DECLARED SCOPE":
        if decision_status == "PROCEED" and decision and decision.get("reversible") is False:
            errors.append(
                "handoff.decision: irreversible PROCEED is not allowed with incomplete coverage"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("handoff", type=Path, help="Current handoff envelope JSON")
    parser.add_argument("--previous", type=Path, help="Previous handoff envelope for lineage comparison")
    args = parser.parse_args()

    try:
        current = load_json(args.handoff)
        previous = load_json(args.previous) if args.previous else None
    except ValidationError as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2

    errors = validate_handoff(current, previous)
    if errors:
        print("INVALID HANDOFF")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALID HANDOFF")
    print("Structural and lineage proof obligations passed.")
    print("This does not verify external factual truth.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
