"""Wave 6 cross-skill claim-lineage regression tests.

These tests protect handoff identity, evidence state, provenance, scope,
confidentiality, downstream restrictions, P0 blockers, and priority runtime
handoffs. They do not verify external factual truth or arbitrary model outputs.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATOR_PATH = ROOT / "reliability" / "kernel" / "validate_handoff.py"

spec = importlib.util.spec_from_file_location("wave6_validate_handoff", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(validator)


def normalize_markdown(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[`*_>#]", "", text)
    text = re.sub(r"[“”‘’\"']", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def record(
    claim_id: str = "MR-001",
    *,
    state: str = "FACT",
    publishability: str = "INTERNAL_ONLY",
    segment: str = "enterprise",
    source_refs: list[str] | None = None,
    may_restate: bool = True,
    allowed_uses: list[str] | None = None,
    prohibited_uses: list[str] | None = None,
) -> dict:
    item = {
        "claim_id": claim_id,
        "claim": "Observed decision-critical claim",
        "state": state,
        "source_class": "primary-external",
        "source_refs": source_refs if source_refs is not None else ["source-1"],
        "source_date": "2026-08-25",
        "freshness": "CURRENT",
        "confidence": "HIGH",
        "scope": {
            "geography": "India",
            "segment": segment,
            "population": "target accounts",
            "time_period": "2026",
            "product_or_workflow": "workflow-a",
        },
        "estimate_method": None,
        "contradictions": ["counter-signal-1"],
        "caveats": ["scope-limited"],
        "attribution": "source owner",
        "publishability": publishability,
        "downstream_policy": {
            "may_restate": may_restate,
            "may_promote_without_new_evidence": False,
            "allowed_uses": allowed_uses if allowed_uses is not None else ["internal analysis"],
            "prohibited_uses": prohibited_uses if prohibited_uses is not None else ["public proof"],
        },
        "promotion_history": [],
    }
    if state == "ESTIMATE":
        item["estimate_method"] = {
            "formula": "accounts * annual_value",
            "inputs": ["accounts", "annual_value"],
            "units": "USD",
            "range_or_sensitivity": "bear/base/bull",
        }
    return item


def handoff(
    *,
    claim: dict | None = None,
    transformation: str = "ORIGINAL",
    parents: list[str] | None = None,
    reason: str | None = None,
    coverage: str = "COMPLETE FOR DECLARED SCOPE",
    failures: list[str] | None = None,
    unresolved: list[dict] | None = None,
    decision: str = "TEST",
    reversible: bool | None = True,
) -> dict:
    claim = claim or record()
    return {
        "handoff_id": "H-001",
        "created_at": "2026-08-26",
        "producer": {
            "plugin": "pm-market-research",
            "artifact": "competitive-analysis",
            "run_id": "run-1",
        },
        "intended_consumers": ["pm-product-strategy/strategy"],
        "decision_context": {
            "decision": "Choose next strategy",
            "actor": "product",
            "stage": "analysis",
            "geography": "India",
            "constraints": [],
        },
        "source_artifacts": ["research.md"],
        "coverage": {
            "status": coverage,
            "declared_scope": "India enterprise workflow-a",
            "gaps": [] if coverage == "COMPLETE FOR DECLARED SCOPE" else ["missing evidence"],
            "tool_or_retrieval_failures": failures or [],
        },
        "claims": [
            {
                "record": claim,
                "transformation": transformation,
                "parent_claim_ids": parents or [],
                "transformation_reason": reason,
            }
        ],
        "unresolved_p0": unresolved or [],
        "decision": {"status": decision, "reversible": reversible, "blockers": []},
        "prohibited_interpretations": ["Do not generalize beyond declared scope"],
    }


def errors_text(errors: list[str]) -> str:
    return "\n".join(errors).lower()


class TestWave6Validator(unittest.TestCase):
    def test_valid_original_handoff_passes(self):
        self.assertEqual(validator.validate_handoff(handoff()), [])

    def test_valid_restatement_with_previous_passes(self):
        previous = handoff()
        current = copy.deepcopy(previous)
        current["handoff_id"] = "H-002"
        current["producer"]["artifact"] = "strategy"
        current["claims"][0]["transformation"] = "RESTATED"
        self.assertEqual(validator.validate_handoff(current, previous), [])

    def test_valid_promotion_requires_matching_new_evidence(self):
        previous = handoff(claim=record(state="ESTIMATE"))
        current = copy.deepcopy(previous)
        current["handoff_id"] = "H-002"
        current["claims"][0]["transformation"] = "PROMOTED"
        current_record = current["claims"][0]["record"]
        current_record["state"] = "FACT"
        current_record["source_refs"].append("measurement-1")
        current_record["promotion_history"] = [
            {
                "from": "ESTIMATE",
                "to": "FACT",
                "new_evidence": ["measurement-1"],
                "reason": "Direct measurement",
            }
        ]
        self.assertEqual(validator.validate_handoff(current, previous), [])

    def test_target_to_fact_without_promotion_is_rejected(self):
        previous = handoff(claim=record(state="TARGET"))
        current = copy.deepcopy(previous)
        current["claims"][0]["transformation"] = "RESTATED"
        current["claims"][0]["record"]["state"] = "FACT"
        self.assertIn(
            "restated claim must preserve state",
            errors_text(validator.validate_handoff(current, previous)),
        )

    def test_estimate_to_fact_without_matching_history_is_rejected(self):
        previous = handoff(claim=record(state="ESTIMATE"))
        current = copy.deepcopy(previous)
        current["claims"][0]["transformation"] = "PROMOTED"
        current["claims"][0]["record"]["state"] = "FACT"
        current["claims"][0]["record"]["promotion_history"] = [
            {"from": "ESTIMATE", "to": "FACT", "new_evidence": [], "reason": "none"}
        ]
        text = errors_text(validator.validate_handoff(current, previous))
        self.assertIn("new_evidence", text)
        self.assertIn("without matching promotion_history", text)

    def test_scope_expansion_under_same_id_is_rejected(self):
        previous = handoff()
        current = copy.deepcopy(previous)
        current["claims"][0]["transformation"] = "RESTATED"
        current["claims"][0]["record"]["scope"]["segment"] = "all industries"
        self.assertIn("material scope changed", errors_text(validator.validate_handoff(current, previous)))

    def test_restricted_claim_cannot_become_public_under_same_id(self):
        previous = handoff(claim=record(publishability="CLIENT_CONFIDENTIAL"))
        current = copy.deepcopy(previous)
        current["claims"][0]["transformation"] = "RESTATED"
        current["claims"][0]["record"]["publishability"] = "PUBLIC"
        self.assertIn("restricted publishability", errors_text(validator.validate_handoff(current, previous)))

    def test_source_provenance_cannot_be_stripped(self):
        previous = handoff(claim=record(source_refs=["source-1", "source-2"]))
        current = copy.deepcopy(previous)
        current["claims"][0]["transformation"] = "RESTATED"
        current["claims"][0]["record"]["source_refs"] = ["source-1"]
        self.assertIn("removed source_refs", errors_text(validator.validate_handoff(current, previous)))

    def test_contradictions_and_caveats_cannot_disappear(self):
        previous = handoff()
        current = copy.deepcopy(previous)
        current["claims"][0]["transformation"] = "RESTATED"
        current["claims"][0]["record"]["contradictions"] = []
        current["claims"][0]["record"]["caveats"] = []
        text = errors_text(validator.validate_handoff(current, previous))
        self.assertIn("removed contradictions", text)
        self.assertIn("removed caveats", text)

    def test_restatement_cannot_weaken_downstream_policy(self):
        previous = handoff()
        current = copy.deepcopy(previous)
        current["claims"][0]["transformation"] = "RESTATED"
        current["claims"][0]["record"]["downstream_policy"]["prohibited_uses"] = []
        self.assertIn("must preserve downstream_policy", errors_text(validator.validate_handoff(current, previous)))

    def test_upstream_may_restate_false_is_enforced(self):
        previous = handoff(claim=record(may_restate=False))
        current = copy.deepcopy(previous)
        current["claims"][0]["transformation"] = "RESTATED"
        self.assertIn("forbids restatement", errors_text(validator.validate_handoff(current, previous)))

    def test_restatement_without_previous_is_rejected(self):
        current = handoff(transformation="RESTATED")
        self.assertIn("requires --previous", errors_text(validator.validate_handoff(current)))

    def test_original_cannot_reuse_previous_claim_id(self):
        previous = handoff()
        current = copy.deepcopy(previous)
        current["handoff_id"] = "H-002"
        current["claims"][0]["transformation"] = "ORIGINAL"
        self.assertIn("cannot reuse an existing claim_id", errors_text(validator.validate_handoff(current, previous)))

    def test_derived_claim_requires_parent_and_reason(self):
        current = handoff(claim=record(claim_id="D-001", state="INFERENCE"), transformation="DERIVED")
        text = errors_text(validator.validate_handoff(current))
        self.assertIn("requires parent_claim_ids", text)
        self.assertIn("requires transformation_reason", text)

    def test_unknown_parent_is_rejected(self):
        current = handoff(
            claim=record(claim_id="D-001", state="INFERENCE"),
            transformation="DERIVED",
            parents=["MISSING-1"],
            reason="Derived from missing parent",
        )
        self.assertIn("unknown parent_claim_id", errors_text(validator.validate_handoff(current)))

    def test_circular_derivation_is_rejected(self):
        a = record(claim_id="D-A", state="INFERENCE")
        a["source_class"] = "derived"
        b = record(claim_id="D-B", state="INFERENCE")
        b["source_class"] = "derived"
        current = handoff(claim=a, transformation="DERIVED", parents=["D-B"], reason="from B")
        current["claims"].append(
            {
                "record": b,
                "transformation": "DERIVED",
                "parent_claim_ids": ["D-A"],
                "transformation_reason": "from A",
            }
        )
        self.assertIn("lineage cycle detected", errors_text(validator.validate_handoff(current)))

    def test_complete_coverage_cannot_hide_tool_failure(self):
        current = handoff(failures=["search unavailable"])
        self.assertIn("cannot be complete", errors_text(validator.validate_handoff(current)))

    def test_irreversible_conditional_proceed_blocked_by_unresolved_p0(self):
        unknown = record(state="UNKNOWN")
        current = handoff(
            claim=unknown,
            unresolved=[
                {
                    "claim_id": "MR-001",
                    "blocker": "Buyer unknown",
                    "evidence_needed": "Authority evidence",
                }
            ],
            decision="PROCEED WITH CONDITIONS",
            reversible=False,
        )
        self.assertIn("irreversible forward decision", errors_text(validator.validate_handoff(current)))

    def test_irreversible_conditional_proceed_blocked_by_partial_coverage(self):
        current = handoff(coverage="PARTIAL", decision="PROCEED WITH CONDITIONS", reversible=False)
        self.assertIn("incomplete coverage", errors_text(validator.validate_handoff(current)))

    def test_unknown_public_claim_is_rejected(self):
        current = handoff(claim=record(state="UNKNOWN", publishability="PUBLIC"))
        self.assertIn("unknown claim cannot be public", errors_text(validator.validate_handoff(current)))

    def test_estimate_requires_reconstructable_method(self):
        estimated = record(state="ESTIMATE")
        estimated["estimate_method"] = None
        current = handoff(claim=estimated)
        self.assertIn("estimate requires estimate_method", errors_text(validator.validate_handoff(current)))

    def test_downgrade_cannot_expand_allowed_uses(self):
        previous = handoff(claim=record(allowed_uses=["internal analysis"]))
        current = copy.deepcopy(previous)
        current["claims"][0]["transformation"] = "DOWNGRADED"
        current["claims"][0]["record"]["state"] = "STALE"
        current["claims"][0]["record"]["downstream_policy"]["allowed_uses"] = [
            "internal analysis",
            "sales collateral",
        ]
        self.assertIn(
            "cannot expand allowed downstream uses",
            errors_text(validator.validate_handoff(current, previous)),
        )


class TestWave6KernelAndRuntime(unittest.TestCase):
    def test_kernel_schemas_parse_and_handoff_refs_claim_schema(self):
        claim_schema = json.loads(
            (ROOT / "reliability/kernel/claim_lineage.schema.json").read_text(encoding="utf-8")
        )
        handoff_schema = json.loads(
            (ROOT / "reliability/kernel/handoff_envelope.schema.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            handoff_schema["properties"]["claims"]["items"]["properties"]["record"]["$ref"],
            "claim_lineage.schema.json",
        )
        self.assertIn("downstream_policy", claim_schema["required"])
        self.assertFalse(
            claim_schema["properties"]["downstream_policy"]["properties"]
            ["may_promote_without_new_evidence"]["const"]
        )

    def test_protocol_contains_non_negotiable_handoff_rules(self):
        text = normalize_markdown(
            (ROOT / "reliability/kernel/HANDOFF_PROTOCOL.md").read_text(encoding="utf-8")
        )
        for phrase in [
            "restating a claim never strengthens it",
            "no silent promotion",
            "no silent scope expansion",
            "propagate confidentiality",
            "respect prohibited uses",
            "unresolved p0 survives polish",
            "tool/retrieval failure stays visible",
        ]:
            self.assertIn(normalize_markdown(phrase), text)

    def test_priority_runtime_handoffs_preserve_lineage(self):
        contracts = {
            "pm-market-research/commands/competitive-analysis.md": [
                "stable claim ids",
                "reliability handoff",
                "parent claim ids",
            ],
            "pm-product-strategy/commands/strategy.md": [
                "lineage consumer contract",
                "preserve stable claim ids",
                "parent claim ids",
            ],
            "pm-prospect-discovery/skills/discovery-synthesis/SKILL.md": [
                "claim-lineage producer contract",
                "reliability handoff",
                "same claim ids",
            ],
            "pm-execution/skills/create-prd/SKILL.md": [
                "lineage consumer contract",
                "source claim id",
                "reliability handoff",
            ],
            "pm-business-case/commands/build-business-case.md": [
                "lineage consumer contract",
                "validate_handoff.py",
                "parent claim ids",
            ],
            "pm-enterprise-transformation/skills/client-proof-extractor/SKILL.md": [
                "claim id",
                "publishability",
                "parent-linkage",
            ],
            "pm-enterprise-transformation/skills/case-study-to-gtm/SKILL.md": [
                "claim id",
                "publishability",
                "parent-linkage",
            ],
            "pm-go-to-market/skills/competitive-battlecard/SKILL.md": [
                "claim id",
                "publishability",
                "parent-linkage",
            ],
            "pm-execution/skills/outcome-roadmap/SKILL.md": [
                "claim id",
                "parent-linkage",
                "proposal",
            ],
            "pm-enterprise-transformation/commands/build-future-capability.md": [
                "claim id",
                "parent-linkage",
                "proposal",
            ],
            "pm-data-analytics/skills/cohort-analysis/SKILL.md": [
                "claim id",
                "parent-linkage",
                "reliability handoff",
            ],
            "pm-data-analytics/skills/ab-test-analysis/SKILL.md": [
                "claim id",
                "parent-linkage",
                "reliability handoff",
            ],
            "pm-product-discovery/skills/prioritize-features/SKILL.md": [
                "claim id",
                "parent-linkage",
                "causal",
            ],
            "pm-go-to-market/commands/plan-launch.md": [
                "claim id",
                "parent-linkage",
                "target",
            ],
            "pm-ai-shipping/commands/ship-check.md": ["claim id", "poc", "production"],
        }
        failures = []
        for rel_path, phrases in contracts.items():
            path = ROOT / rel_path
            if not path.is_file():
                failures.append(f"missing file: {rel_path}")
                continue
            text = normalize_markdown(path.read_text(encoding="utf-8"))
            for phrase in phrases:
                needle = normalize_markdown(phrase)
                if needle == "parent-linkage":
                    has_parent_linkage = any(
                        candidate in text
                        for candidate in (
                            "parent claim",
                            "parent claims",
                            "parent id",
                            "parent ids",
                            "parent claim id",
                            "parent claim ids",
                        )
                    )
                    if not has_parent_linkage:
                        failures.append(f"{rel_path}: missing parent-claim/parent-id linkage")
                elif needle not in text:
                    failures.append(f"{rel_path}: missing {phrase!r}")
        self.assertEqual(failures, [], "\n".join(failures))

    def test_wave6_scenario_catalog_covers_all_priority_failures(self):
        text = (ROOT / "reliability/WAVE6_SCENARIOS.md").read_text(encoding="utf-8")
        for index in range(1, 19):
            self.assertIn(f"L{index}.", text)
        for phrase in [
            "Market Research -> Strategy",
            "Prospect Discovery -> PRD / Business Case",
            "Client Proof -> GTM / Battlecard",
            "Business Case -> Roadmap / Capability Investment",
            "Analytics -> Prioritization / Launch",
            "PoC -> Production Readiness",
        ]:
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
