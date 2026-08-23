#!/usr/bin/env python3
"""Validate a pm-business-case evidence ledger using only the Python standard library.

This validator enforces structural proof obligations. It does not verify that an
external source is true. The business-case workflow must retrieve and inspect
sources before marking them VERIFIED.
"""

import json
import sys
from pathlib import Path

ALLOWED_STATES = {
    "FACT",
    "INFERENCE",
    "ASSUMPTION",
    "ESTIMATE",
    "UNKNOWN",
    "STALE",
    "PROPOSAL",
    "DECISION_THRESHOLD",
}
ALLOWED_PRIORITIES = {"P0", "P1", "P2"}
ALLOWED_VERIFICATION = {"VERIFIED", "PARTIAL", "UNVERIFIED", "NOT_APPLICABLE"}
ALLOWED_FRESHNESS = {"CURRENT", "STALE", "UNKNOWN", "NOT_APPLICABLE"}
ALLOWED_CONTRADICTION = {"NONE_FOUND", "RESOLVED", "UNRESOLVED", "NOT_CHECKED"}
ALLOWED_DECISIONS = {"BUILD", "BUY", "PARTNER", "EXPERIMENT", "DEFER", "KILL", "NOT READY"}
PRIMARY_TYPES = {"PRIMARY_AUTHORITATIVE", "USER_PROVIDED_PRIMARY"}
DISALLOWED_FACT_SOURCE_TYPES = {"MODEL_MEMORY", "NONE", "USER_PROVIDED_CLAIM", "USER_PROVIDED_LEAD"}


def fail(errors, message):
    errors.append(message)


def distinct_independence_groups(sources):
    groups = set()
    for source in sources:
        group = str(source.get("independence_group", "")).strip()
        if group:
            groups.add(group)
    return groups


def has_primary_source(sources):
    return any(source.get("source_type") in PRIMARY_TYPES for source in sources)


def validate_source(errors, claim_id, source, index):
    prefix = f"{claim_id} source[{index}]"
    source_type = str(source.get("source_type", "")).strip()
    title = str(source.get("title", "")).strip()
    reference = str(source.get("reference", "")).strip()
    support = str(source.get("support", "")).strip()

    if not source_type:
        fail(errors, f"{prefix}: missing source_type")
    if not title:
        fail(errors, f"{prefix}: missing title")
    if source_type not in {"USER_PROVIDED_PRIMARY", "USER_PROVIDED_CLAIM", "USER_PROVIDED_LEAD", "NONE"} and not reference:
        fail(errors, f"{prefix}: missing reference or URL")
    if source_type not in {"NONE", "MODEL_MEMORY"} and not support:
        fail(errors, f"{prefix}: missing supporting excerpt or precise location marker")


def validate_claim(errors, claim, known_ids):
    claim_id = str(claim.get("claim_id", "")).strip()
    state = claim.get("state")
    priority = claim.get("priority")
    critical = bool(claim.get("decision_critical", False))
    sources = claim.get("sources", [])
    verification = claim.get("verification_status")
    freshness = claim.get("freshness_status")
    contradiction = claim.get("contradiction_status")

    if not claim_id:
        fail(errors, "claim with missing claim_id")
        return
    if not str(claim.get("claim_text", "")).strip():
        fail(errors, f"{claim_id}: missing claim_text")
    if state not in ALLOWED_STATES:
        fail(errors, f"{claim_id}: invalid state {state!r}")
    if priority not in ALLOWED_PRIORITIES:
        fail(errors, f"{claim_id}: invalid priority {priority!r}")
    if verification not in ALLOWED_VERIFICATION:
        fail(errors, f"{claim_id}: invalid verification_status {verification!r}")
    if freshness not in ALLOWED_FRESHNESS:
        fail(errors, f"{claim_id}: invalid freshness_status {freshness!r}")
    if contradiction not in ALLOWED_CONTRADICTION:
        fail(errors, f"{claim_id}: invalid contradiction_status {contradiction!r}")
    if not isinstance(sources, list):
        fail(errors, f"{claim_id}: sources must be a list")
        sources = []

    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            fail(errors, f"{claim_id} source[{index}]: source must be an object")
            continue
        validate_source(errors, claim_id, source, index)

    if state == "FACT":
        if verification != "VERIFIED":
            fail(errors, f"{claim_id}: FACT must be VERIFIED")
        if freshness not in {"CURRENT", "NOT_APPLICABLE"}:
            fail(errors, f"{claim_id}: FACT must be CURRENT or NOT_APPLICABLE for freshness")
        if not sources:
            fail(errors, f"{claim_id}: FACT requires at least one source")
        for source in sources:
            if source.get("source_type") in DISALLOWED_FACT_SOURCE_TYPES:
                fail(errors, f"{claim_id}: source type {source.get('source_type')!r} cannot establish a FACT")
        if critical or priority == "P0":
            if not has_primary_source(sources) and len(distinct_independence_groups(sources)) < 2:
                fail(errors, f"{claim_id}: decision-critical FACT needs one primary source or two independent credible sources")
        if contradiction in {"UNRESOLVED", "NOT_CHECKED"} and (critical or priority == "P0"):
            fail(errors, f"{claim_id}: decision-critical FACT must complete contradiction checking")

    if state == "INFERENCE":
        basis = claim.get("basis_claim_ids", [])
        if not isinstance(basis, list) or not basis:
            fail(errors, f"{claim_id}: INFERENCE requires basis_claim_ids")
        else:
            for ref in basis:
                if ref not in known_ids:
                    fail(errors, f"{claim_id}: basis claim {ref!r} does not exist")

    if state == "ESTIMATE":
        if not str(claim.get("formula", "")).strip():
            fail(errors, f"{claim_id}: ESTIMATE requires formula or method")
        inputs = claim.get("inputs", [])
        if not isinstance(inputs, list) or not inputs:
            fail(errors, f"{claim_id}: ESTIMATE requires explicit inputs")
        else:
            for index, item in enumerate(inputs):
                if not isinstance(item, dict):
                    fail(errors, f"{claim_id} input[{index}]: input must be an object")
                    continue
                if not str(item.get("name", "")).strip():
                    fail(errors, f"{claim_id} input[{index}]: missing name")
                if "value" not in item:
                    fail(errors, f"{claim_id} input[{index}]: missing value")
                source_claim_id = str(item.get("source_claim_id", "")).strip()
                if source_claim_id and source_claim_id not in known_ids:
                    fail(errors, f"{claim_id} input[{index}]: source claim {source_claim_id!r} does not exist")

    if state in {"ASSUMPTION", "UNKNOWN", "PROPOSAL", "DECISION_THRESHOLD"} and verification == "VERIFIED":
        fail(errors, f"{claim_id}: {state} cannot be marked VERIFIED")

    if state == "UNKNOWN" and sources and verification == "VERIFIED":
        fail(errors, f"{claim_id}: UNKNOWN cannot be both sourced and VERIFIED")

    if state == "STALE":
        if freshness != "STALE":
            fail(errors, f"{claim_id}: STALE claim must have freshness_status STALE")
        if verification == "VERIFIED" and critical:
            fail(errors, f"{claim_id}: stale decision-critical evidence cannot be treated as ready")


def validate_decision(errors, decision, claims_by_id):
    status = decision.get("status")
    if status not in ALLOWED_DECISIONS:
        fail(errors, f"decision: invalid status {status!r}")
        return

    rationale_ids = decision.get("rationale_claim_ids", [])
    blocking_ids = decision.get("blocking_claim_ids", [])
    if not isinstance(rationale_ids, list):
        fail(errors, "decision: rationale_claim_ids must be a list")
        rationale_ids = []
    if not isinstance(blocking_ids, list):
        fail(errors, "decision: blocking_claim_ids must be a list")
        blocking_ids = []

    for ref in rationale_ids + blocking_ids:
        if ref not in claims_by_id:
            fail(errors, f"decision: referenced claim {ref!r} does not exist")

    if status in {"BUILD", "BUY", "PARTNER"}:
        blockers = []
        for claim_id, claim in claims_by_id.items():
            if claim.get("priority") != "P0" and not claim.get("decision_critical", False):
                continue
            if claim.get("state") in {"UNKNOWN", "STALE", "ASSUMPTION"}:
                blockers.append(claim_id)
                continue
            if claim.get("state") == "FACT" and claim.get("verification_status") != "VERIFIED":
                blockers.append(claim_id)
                continue
            if claim.get("contradiction_status") in {"UNRESOLVED", "NOT_CHECKED"}:
                blockers.append(claim_id)
        if blockers:
            fail(errors, f"decision: {status} prohibited while critical claims are unresolved: {', '.join(sorted(set(blockers)))}")


def validate_document(data):
    errors = []
    if not isinstance(data, dict):
        return ["root must be a JSON object"]

    claims = data.get("claims")
    if not isinstance(claims, list) or not claims:
        return ["claims must be a non-empty list"]

    ids = []
    for claim in claims:
        if isinstance(claim, dict):
            ids.append(str(claim.get("claim_id", "")).strip())
    duplicates = sorted({claim_id for claim_id in ids if claim_id and ids.count(claim_id) > 1})
    if duplicates:
        fail(errors, f"duplicate claim IDs: {', '.join(duplicates)}")

    known_ids = {claim_id for claim_id in ids if claim_id}
    for claim in claims:
        if not isinstance(claim, dict):
            fail(errors, "claim entry must be an object")
            continue
        validate_claim(errors, claim, known_ids)

    claims_by_id = {
        str(claim.get("claim_id", "")).strip(): claim
        for claim in claims
        if isinstance(claim, dict) and str(claim.get("claim_id", "")).strip()
    }
    decision = data.get("decision", {})
    if not isinstance(decision, dict):
        fail(errors, "decision must be an object")
    else:
        validate_decision(errors, decision, claims_by_id)

    return errors


def main(argv):
    if len(argv) != 2:
        print("Usage: validate_evidence.py <evidence-ledger.json>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 2

    errors = validate_document(data)
    if errors:
        print("EVIDENCE VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("EVIDENCE VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
