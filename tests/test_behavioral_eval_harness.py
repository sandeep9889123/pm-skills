"""Tests for the model-agnostic behavioral evaluation harness."""

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_PATH = ROOT / "evaluation" / "cases.json"
SCORER_PATH = ROOT / "evaluation" / "score_output.py"

spec = importlib.util.spec_from_file_location("score_output", SCORER_PATH)
score_output = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(score_output)


class TestBehavioralEvalSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.suite = json.loads(CASES_PATH.read_text(encoding="utf-8"))
        cls.cases = cls.suite["cases"]

    def test_rubric_weights_total_100(self):
        total = sum(d["weight"] for d in self.suite["rubric"].values())
        self.assertEqual(total, 100)

    def test_case_ids_are_unique(self):
        ids = [c["id"] for c in self.cases]
        self.assertEqual(len(ids), len(set(ids)))

    def test_suite_has_at_least_ten_adversarial_cases(self):
        self.assertGreaterEqual(len(self.cases), 10)

    def test_core_enterprise_workflows_are_covered(self):
        workflows = {c["workflow"] for c in self.cases}
        self.assertIn("pm-enterprise-transformation:build-future-capability", workflows)
        self.assertIn("pm-enterprise-transformation:proof-to-gtm", workflows)
        self.assertIn("pm-enterprise-transformation:transform-sales", workflows)
        self.assertIn("pm-enterprise-transformation:automate-pm-workflow", workflows)
        self.assertIn("pm-market-research:competitor-analysis", workflows)
        self.assertIn("pm-business-case:build-business-case", workflows)

    def test_every_case_has_expected_behavior_and_hard_gates(self):
        for case in self.cases:
            with self.subTest(case=case["id"]):
                self.assertGreaterEqual(len(case.get("expected_behaviors", [])), 3)
                gates = case.get("hard_gates", {})
                self.assertTrue(gates.get("required_patterns"))
                self.assertTrue(gates.get("forbidden_patterns"))
                threshold = case.get(
                    "pass_threshold", self.suite.get("default_pass_threshold", 90)
                )
                self.assertGreaterEqual(threshold, 80)
                self.assertLessEqual(threshold, 100)

    def test_known_bad_outputs_fail_hard_gates(self):
        bad_outputs = {
            "MR1_ZERO_RESULT_COMPETITOR": "There are no competitors. The first search returned nothing.",
            "ET1_SINGLE_CLIENT_DEMAND": "Three requests prove clear market demand. We should invest now.",
            "ET2_BESPOKE_IP": "This is reusable IP and ready as a platform.",
            "ET3_TARGET_TO_SUCCESS_CLAIM": "We achieved 30% faster processing and reduced review effort by 20%.",
            "ET4_CONFIDENTIAL_GTM_PROOF": "Use the client name publicly. It is safe to publish the proprietary rules.",
            "ET5_CHERRYPICKED_WIN_RATE": "The 38% win rate proves the process worked. Scale it because of 38%.",
            "ET6_POC_NOT_PRODUCTION": "Position it as production-ready because the PoC hit 95%.",
            "ET8_AUTOMATION_REVIEW_ERASES_ROI": "ROI is obviously excellent because four hours fell to 15 minutes.",
            "ET9_AUTOMATION_NO_ROLLBACK": "Remove human approval. No review is needed; go fully autonomous immediately.",
            "ET10_VENDOR_DEMO_BIAS": "Select Vendor A now. The demo proves it and the analyst report proves it.",
            "BC1_ZERO_RESULT_BUSINESS_CASE": "This is an uncontested market. There are no competitors, so BUILD.",
            "BC5_ROI_MISSING_INPUTS": "The 5x ROI is confirmed and clearly achievable.",
            "BC11_PREMATURE_PLATFORM": "One PoC proves this is ready as an enterprise platform. Fund the full platform investment now.",
            "BC19_TECH_SUCCESS_NO_COMMERCIAL_PROOF": "The 25% technical lift proves commercial validation. Recommend BUILD because of 25%.",
        }
        for case in self.cases:
            with self.subTest(case=case["id"]):
                result = score_output.evaluate_hard_gates(case, bad_outputs[case["id"]])
                self.assertFalse(result["passed"])
                self.assertTrue(
                    result["matched_forbidden"] or result["missing_required"],
                    f"Known-bad output unexpectedly survived {case['id']}",
                )

    def test_full_rubric_can_score_100_without_overriding_hard_gate(self):
        case = next(c for c in self.cases if c["id"] == "ET1_SINGLE_CLIENT_DEMAND")
        good_output = (
            "This is a single client source, not independent demand. "
            "I would HOLD broad investment and run a pilot while seeking independent demand signals."
        )
        judgement = {
            "case_id": case["id"],
            "evaluator": "test",
            "dimensions": {
                name: {"score": 5, "rationale": "Meets the criterion in this fixture."}
                for name in self.suite["rubric"]
            },
        }
        result = score_output.score_case(self.suite, case, good_output, judgement)
        self.assertTrue(result["hard_gates"]["passed"])
        self.assertEqual(result["weighted_score"], 100.0)
        self.assertEqual(result["status"], "PASS")

        bad_output = "Three requests prove clear market demand. Invest now."
        result = score_output.score_case(self.suite, case, bad_output, judgement)
        self.assertEqual(result["weighted_score"], 100.0)
        self.assertEqual(result["status"], "FAIL_HARD_GATE")


if __name__ == "__main__":
    unittest.main()
