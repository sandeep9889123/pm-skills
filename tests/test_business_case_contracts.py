"""Regression tests for the reliability-first business case plugin.

These tests protect structural proof obligations and high-risk guard language.
They do not claim to measure end-to-end LLM truthfulness.
"""

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "pm-business-case"
GOLDENS = ROOT / "reliability" / "business_case_golden_scenarios.json"
VALIDATOR_PATH = PLUGIN / "scripts" / "validate_evidence.py"


def load_validator_module():
    spec = importlib.util.spec_from_file_location("validate_evidence", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class TestBusinessCasePluginShape(unittest.TestCase):
    def test_skill_and_command_counts(self):
        skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
        commands = sorted((PLUGIN / "commands").glob("*.md"))
        self.assertEqual(len(skills), 6)
        self.assertEqual(len(commands), 5)

    def test_orchestrator_is_fail_closed(self):
        text = (PLUGIN / "skills" / "business-case-orchestrator" / "SKILL.md").read_text(encoding="utf-8").lower()
        required = [
            "fail-closed",
            "never invent a citation",
            "tool/search failure",
            "build, buy, or partner recommendation is prohibited",
            "falsifiable poc",
            "strongest rejection case",
            "validate_evidence.py",
            "not ready",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

    def test_market_proof_blocks_first_pass_absence(self):
        text = (PLUGIN / "skills" / "opportunity-market-proof" / "SKILL.md").read_text(encoding="utf-8").lower()
        required = [
            "never conclude \"no competitors\" from a first pass",
            "regional players",
            "emerging startups",
            "in-house alternatives",
            "contradiction pass",
            "coverage incomplete / unknown",
            "do nothing",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

    def test_customer_skill_blocks_fabricated_demand(self):
        text = (PLUGIN / "skills" / "customer-jtbd-proof" / "SKILL.md").read_text(encoding="utf-8").lower()
        required = [
            "do not fabricate personas",
            "willingness to pay",
            "user",
            "economic buyer",
            "current alternative",
            "contradiction pass",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

    def test_economics_requires_reconstructable_numbers(self):
        text = (PLUGIN / "skills" / "economics-commercial-proof" / "SKILL.md").read_text(encoding="utf-8").lower()
        required = [
            "every material estimate",
            "formula",
            "bear, base, and bull",
            "willingness to pay",
            "market size is used as revenue forecast",
            "pilot must have a production path",
        ]
        for phrase in required:
            self.assertIn(phrase, text)

    def test_red_team_requires_rejection_case(self):
        text = (PLUGIN / "skills" / "investment-red-team" / "SKILL.md").read_text(encoding="utf-8").lower()
        required = [
            "strongest rejection case",
            "build vs buy vs partner vs do nothing",
            "kill criteria",
            "technical success presented as commercial validation",
            "platform or reusable accelerator",
        ]
        for phrase in required:
            self.assertIn(phrase, text)


class TestBusinessCaseGoldenScenarios(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(GOLDENS.read_text(encoding="utf-8"))
        cls.scenarios = cls.data["scenarios"]

    def test_has_broad_failure_coverage(self):
        self.assertGreaterEqual(len(self.scenarios), 20)
        ids = {scenario["id"] for scenario in self.scenarios}
        required_ids = {
            "BC1_ZERO_COMPETITOR_FIRST_PASS",
            "BC2_USER_INVENTS_COMPETITOR",
            "BC4_CONFLICTING_MARKET_SIZES",
            "BC5_ROI_WITH_MISSING_INPUTS",
            "BC8_NO_WTP_EVIDENCE",
            "BC10_DEMO_AS_POC",
            "BC11_PREMATURE_PLATFORM",
            "BC12_TOOL_FAILURE",
            "BC18_AI_LABEL_WITHOUT_MECHANISM",
            "BC19_TECHNICAL_SUCCESS_COMMERCIAL_FAILURE",
        }
        self.assertTrue(required_ids.issubset(ids))

    def test_every_golden_has_required_and_forbidden_behavior(self):
        for scenario in self.scenarios:
            self.assertTrue(scenario.get("setup"), scenario.get("id"))
            self.assertTrue(scenario.get("must_do"), scenario.get("id"))
            self.assertTrue(scenario.get("must_not_do"), scenario.get("id"))


class TestEvidenceValidator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator_module()

    def test_rejects_unsourced_fact(self):
        payload = {
            "claims": [
                {
                    "claim_id": "C001",
                    "claim_text": "A decision-critical fact",
                    "state": "FACT",
                    "priority": "P0",
                    "decision_critical": True,
                    "sources": [],
                    "basis_claim_ids": [],
                    "formula": "",
                    "inputs": [],
                    "verification_status": "VERIFIED",
                    "freshness_status": "CURRENT",
                    "contradiction_status": "NONE_FOUND",
                }
            ],
            "decision": {"status": "NOT READY", "rationale_claim_ids": [], "blocking_claim_ids": ["C001"]},
        }
        errors = self.validator.validate_document(payload)
        self.assertTrue(any("requires at least one source" in error for error in errors))

    def test_rejects_estimate_without_formula(self):
        payload = {
            "claims": [
                {
                    "claim_id": "C001",
                    "claim_text": "Expected annual savings are 1M",
                    "state": "ESTIMATE",
                    "priority": "P1",
                    "decision_critical": False,
                    "sources": [],
                    "basis_claim_ids": [],
                    "formula": "",
                    "inputs": [],
                    "verification_status": "UNVERIFIED",
                    "freshness_status": "NOT_APPLICABLE",
                    "contradiction_status": "NOT_CHECKED",
                }
            ],
            "decision": {"status": "EXPERIMENT", "rationale_claim_ids": [], "blocking_claim_ids": []},
        }
        errors = self.validator.validate_document(payload)
        self.assertTrue(any("ESTIMATE requires formula" in error for error in errors))
        self.assertTrue(any("ESTIMATE requires explicit inputs" in error for error in errors))

    def test_rejects_build_with_unknown_p0(self):
        payload = {
            "claims": [
                {
                    "claim_id": "C001",
                    "claim_text": "Willingness to pay is not yet known",
                    "state": "UNKNOWN",
                    "priority": "P0",
                    "decision_critical": True,
                    "sources": [],
                    "basis_claim_ids": [],
                    "formula": "",
                    "inputs": [],
                    "verification_status": "UNVERIFIED",
                    "freshness_status": "UNKNOWN",
                    "contradiction_status": "NOT_CHECKED",
                }
            ],
            "decision": {"status": "BUILD", "rationale_claim_ids": [], "blocking_claim_ids": ["C001"]},
        }
        errors = self.validator.validate_document(payload)
        self.assertTrue(any("BUILD prohibited" in error for error in errors))

    def test_accepts_primary_sourced_current_fact_for_build(self):
        payload = {
            "claims": [
                {
                    "claim_id": "C001",
                    "claim_text": "Authoritative internal source establishes the current metric",
                    "state": "FACT",
                    "priority": "P0",
                    "decision_critical": True,
                    "sources": [
                        {
                            "source_type": "USER_PROVIDED_PRIMARY",
                            "title": "Internal source of truth",
                            "reference": "internal://source-of-truth",
                            "source_date": "2026-08-24",
                            "accessed_date": "not applicable",
                            "support": "Metric field in authoritative artifact",
                            "independence_group": "internal-source-of-truth",
                        }
                    ],
                    "basis_claim_ids": [],
                    "formula": "",
                    "inputs": [],
                    "verification_status": "VERIFIED",
                    "freshness_status": "CURRENT",
                    "contradiction_status": "NONE_FOUND",
                }
            ],
            "decision": {"status": "BUILD", "rationale_claim_ids": ["C001"], "blocking_claim_ids": []},
        }
        errors = self.validator.validate_document(payload)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
