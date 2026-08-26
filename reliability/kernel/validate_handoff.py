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
ALLOWED_SOURCE_CLASSES = {
    "user-source-of-truth",
    "connected-internal",
    "primary-external",
    "independent-credible",
    "secondary",
    "stale",
    "model-prior-knowledge",
    "derived",
    "none",
}
ALLOWED_FRESHNESS = {"CURRENT", "STALE", "UNKNOWN", "NOT_APPLICABLE"}
ALLOWED_PUBLISHABILITY = {
    "PUBLIC",
    "INTERNAL_ONLY",
    "CLIENT_CONFIDENTIAL",
    "REQUIRES_CLEARANCE",
    "NOT_APPLICABLE",
}
ALLOWED_CONFIDENCE = {"HIGH", "MEDIUM", "LOW", None}
RESTRICTED_PUBLISHABILITY = {"INTERNAL_ONLY", "CLIENT_CONFIDENTIAL", "REQUIRES_CLEARANCE"}
FORWARD_DECISIONS = {"PROCEED", "PROCEED WITH CONDITIONS"}


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


def list_of_strings(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def string_set(value: Any) -> set[str]:
    if not list_of_strings(value):
        return set()
    return set(value)


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
    if source_class not in ALLOWED_SOURCE_CLASSES:
        errors.append(f"{where}: invalid source_class {source_class!r}")
    if not isinstance(scope, dict):
        errors.append(f"{where}: scope must be an object")

    source_refs = record.get("source_refs", [])
    if not list_of_strings(source_refs) or len(source_refs) != len(set(source_refs)):
        errors.append(f"{where}: source_refs must be a unique array of strings")

    freshness = record.get("freshness")
    if freshness is not None and freshness not in ALLOWED_FRESHNESS:
        errors.append(f"{where}: invalid freshness {freshness!r}")

    confidence = record.get("confidence")
    if confidence not in ALLOWED_CONFIDENCE:
        errors.append(f"{where}: invalid confidence {confidence!r}")

    publishability = record.get("publishability")
    if publishability is not None and publishability not in ALLOWED_PUBLISHABILITY:
        errors.append(f"{where}: invalid publishability {publishability!r}")
    if publishability == "PUBLIC" and state == "UNKNOWN":
        errors.append(f"{where}: UNKNOWN claim cannot be PUBLIC")

    for field in ("contradictions", "caveats"):
        value = record.get(field, [])
        if not list_of_strings(value):
            errors.append(f"{where}: {field} must be an array of strings")

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
        for field in ("allowed_uses", "prohibited_uses"):
            value = downstream.get(field, [])
            if not list_of_strings(value):
                errors.append(f"{where}: downstream_policy.{field} must be an array of strings")

    history = record.get("promotion_history") or []
    if not isinstance(history, list):
        errors.append(f"{where}: promotion_history must be an array")
    else:
        for idx, item in enumerate(history):
            hwhere = f"{where}.promotion_history[{idx}]"
            if not isinstance(item, dict):
                errors.append(f"{hwhere}: must be an object")
                continue
            if item.get("from") not in ALLOWED_STATES or item.get("to") not in ALLOWED_STATES:
                errors.append(f"{hwhere}: from/to must be valid evidence states")
            evidence = item.get("new_evidence")
            if not isinstance(evidence, list) or not evidence:
                errors.append(f"{hwhere}: new_evidence must be a non-empty array")
            elif not all(isinstance(ref, str) and ref.strip() for ref in evidence):
                errors.append(f"{hwhere}: new_evidence entries must be non-empty strings")

    return claim_id if isinstance(claim_id, str) else None


def detect_parent_cycles(parent_map: dict[str, list[str]], current_ids: set[str]) -> list[str]:
    errors: list[str] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        if node in visiting:
            try:
                start = path.index(node)
                cycle = path[start:] + [node]
            except ValueError:
                cycle = path + [node]
            errors.append("claim lineage cycle detected: " + " -> ".join(cycle))
            return
        if node in visited:
            return
        visiting.add(node)
        for parent in parent_map.get(node, []):
            if parent in current_ids:
                visit(parent, path + [parent])
        visiting.remove(node)
        visited.add(node)

    for claim_id in current_ids:
        visit(claim_id, [claim_id])
    return errors


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

    consumers = data.get("intended_consumers")
    if not isinstance(consumers, list) or not consumers or not all(isinstance(x, str) and x.strip() for x in consumers):
        errors.append("handoff.intended_consumers: must be a non-empty array of strings")

    prohibited_interpretations = data.get("prohibited_interpretations")
    if not list_of_strings(prohibited_interpretations):
        errors.append("handoff.prohibited_interpretations: must be an array of strings")

    coverage = data.get("coverage")
    if not isinstance(coverage, dict):
        errors.append("handoff.coverage: must be an object")
    else:
        status = coverage.get("status")
        if status not in ALLOWED_COVERAGE:
            errors.append(f"handoff.coverage: invalid status {status!r}")
        gaps = coverage.get("gaps")
        if not list_of_strings(gaps):
            errors.append("handoff.coverage.gaps: must be an array of strings")
        failures = coverage.get("tool_or_retrieval_failures") or []
        if not list_of_strings(failures):
            errors.append("handoff.coverage.tool_or_retrieval_failures: must be an array of strings")
        if failures and status == "COMPLETE FOR DECLARED SCOPE":
            errors.append("handoff.coverage: cannot be COMPLETE when tool/retrieval failures exist")

    decision = data.get("decision")
    if not isinstance(decision, dict):
        errors.append("handoff.decision: must be an object")
    else:
        status = decision.get("status")
        if status not in ALLOWED_DECISIONS:
            errors.append(f"handoff.decision: invalid status {status!r}")
        blockers = decision.get("blockers")
        if not list_of_strings(blockers):
            errors.append("handoff.decision.blockers: must be an array of strings")

    claims = data.get("claims")
    if not isinstance(claims, list):
        errors.append("handoff.claims: must be an array")
        claims = []

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

    seen_ids: set[str] = set()
    current_by_id: dict[str, dict[str, Any]] = {}
    entry_by_id: dict[str, dict[str, Any]] = {}
    parent_map: dict[str, list[str]] = {}
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
        reason = entry.get("transformation_reason")

        if transformation not in ALLOWED_TRANSFORMATIONS:
            errors.append(f"{where}: invalid transformation {transformation!r}")
        if not isinstance(parents, list):
            errors.append(f"{where}: parent_claim_ids must be an array")
            parents = []
        elif len(parents) != len(set(parents)):
            errors.append(f"{where}: duplicate parent_claim_ids")
        elif not all(isinstance(parent, str) and parent.strip() for parent in parents):
            errors.append(f"{where}: parent_claim_ids entries must be non-empty strings")

        if transformation == "DERIVED":
            if not parents:
                errors.append(f"{where}: DERIVED claim requires parent_claim_ids")
            if not isinstance(reason, str) or not reason.strip():
                errors.append(f"{where}: DERIVED claim requires transformation_reason")
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
            entry_by_id[claim_id] = entry
            parent_map[claim_id] = [p for p in parents if isinstance(p, str)]
            if isinstance(record, dict):
                current_by_id[claim_id] = record
            for parent in parents:
                if isinstance(parent, str):
                    all_parent_refs.append((claim_id, parent))

    available_parent_ids = seen_ids | previous_ids
    for child, parent in all_parent_refs:
        if parent not in available_parent_ids:
            errors.append(f"claim {child!r}: unknown parent_claim_id {parent!r}")
        if child == parent:
            errors.append(f"claim {child!r}: claim cannot be its own parent")

    errors.extend(detect_parent_cycles(parent_map, seen_ids))

    for claim_id, entry in entry_by_id.items():
        transformation = entry.get("transformation")
        existed_before = claim_id in previous_ids
        if transformation in {"RESTATED", "PROMOTED", "DOWNGRADED"}:
            if previous is None:
                errors.append(
                    f"claim {claim_id!r}: {transformation} requires --previous so lineage can be verified"
                )
            elif not existed_before:
                errors.append(
                    f"claim {claim_id!r}: {transformation} requires the same claim_id in previous handoff"
                )
        if transformation in {"ORIGINAL", "DERIVED"} and existed_before:
            errors.append(
                f"claim {claim_id!r}: {transformation} cannot reuse an existing claim_id; preserve/restatement or create a new ID"
            )

    if previous:
        for claim_id, current in current_by_id.items():
            old = previous_by_id.get(claim_id)
            if not old:
                continue
            entry = entry_by_id.get(claim_id, {})
            transformation = entry.get("transformation")

            old_state = old.get("state")
            new_state = current.get("state")
            if transformation == "RESTATED" and old_state != new_state:
                errors.append(
                    f"claim {claim_id!r}: RESTATED claim must preserve state {old_state!r}; got {new_state!r}"
                )
            elif transformation == "PROMOTED":
                if old_state == new_state:
                    errors.append(f"claim {claim_id!r}: PROMOTED claim must change state")
                elif not find_promotion(current, str(old_state), str(new_state)):
                    errors.append(
                        f"claim {claim_id!r}: state changed {old_state!r} -> {new_state!r} "
                        "without matching promotion_history + new evidence"
                    )
            elif transformation == "DOWNGRADED":
                if old_state == new_state:
                    errors.append(f"claim {claim_id!r}: DOWNGRADED claim must change state")
            elif old_state != new_state:
                errors.append(
                    f"claim {claim_id!r}: state changed {old_state!r} -> {new_state!r} "
                    f"but transformation is {transformation!r}, not PROMOTED/DOWNGRADED"
                )

            if scope_signature(old.get("scope")) != scope_signature(current.get("scope")):
                errors.append(
                    f"claim {claim_id!r}: material scope changed under the same claim_id; "
                    "create a new derived claim instead"
                )

            old_refs = string_set(old.get("source_refs", []))
            new_refs = string_set(current.get("source_refs", []))
            if not old_refs.issubset(new_refs):
                errors.append(
                    f"claim {claim_id!r}: downstream handoff removed source_refs; preserve prior provenance"
                )

            for field in ("contradictions", "caveats"):
                old_items = string_set(old.get(field, []))
                new_items = string_set(current.get(field, []))
                if not old_items.issubset(new_items):
                    errors.append(
                        f"claim {claim_id!r}: downstream handoff removed {field}; create a new evidence-backed derived claim to resolve them"
                    )

            old_pub = old.get("publishability")
            new_pub = current.get("publishability")
            if old_pub in RESTRICTED_PUBLISHABILITY and new_pub != old_pub:
                errors.append(
                    f"claim {claim_id!r}: restricted publishability {old_pub!r} cannot change under the same claim_id; "
                    "create a new cleared claim record"
                )

            old_policy = old.get("downstream_policy") if isinstance(old.get("downstream_policy"), dict) else {}
            new_policy = current.get("downstream_policy") if isinstance(current.get("downstream_policy"), dict) else {}
            if transformation == "RESTATED":
                if old.get("source_class") != current.get("source_class"):
                    errors.append(f"claim {claim_id!r}: RESTATED claim must preserve source_class")
                if old.get("freshness") != current.get("freshness"):
                    errors.append(f"claim {claim_id!r}: RESTATED claim must preserve freshness")
                if old_pub != new_pub:
                    errors.append(f"claim {claim_id!r}: RESTATED claim must preserve publishability")
                if old_policy != new_policy:
                    errors.append(f"claim {claim_id!r}: RESTATED claim must preserve downstream_policy")
                if old_policy.get("may_restate") is False:
                    errors.append(f"claim {claim_id!r}: upstream downstream_policy forbids restatement")
            elif transformation == "DOWNGRADED":
                old_prohibited = string_set(old_policy.get("prohibited_uses", []))
                new_prohibited = string_set(new_policy.get("prohibited_uses", []))
                if not old_prohibited.issubset(new_prohibited):
                    errors.append(
                        f"claim {claim_id!r}: DOWNGRADED claim cannot remove prohibited downstream uses"
                    )
                old_allowed = string_set(old_policy.get("allowed_uses", []))
                new_allowed = string_set(new_policy.get("allowed_uses", []))
                if old_allowed and not new_allowed.issubset(old_allowed):
                    errors.append(
                        f"claim {claim_id!r}: DOWNGRADED claim cannot expand allowed downstream uses"
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
    reversible = decision.get("reversible") if isinstance(decision, dict) else None
    if unresolved and decision_status == "PROCEED":
        errors.append("handoff.decision: PROCEED is not allowed while unresolved_p0 is non-empty")
    if unresolved and decision_status in FORWARD_DECISIONS and reversible is False:
        errors.append(
            "handoff.decision: irreversible forward decision is not allowed while unresolved_p0 is non-empty"
        )

    if isinstance(coverage, dict) and coverage.get("status") != "COMPLETE FOR DECLARED SCOPE":
        if decision_status in FORWARD_DECISIONS and reversible is False:
            errors.append(
                "handoff.decision: irreversible forward decision is not allowed with incomplete coverage"
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
