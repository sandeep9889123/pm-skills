"""Wave 7 behavioral benchmark infrastructure tests.

These tests validate benchmark definitions, deterministic hard-gate fixtures,
run integrity, and aggregate reporting. They do NOT claim that any live model
has passed the benchmark.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVAL = ROOT / "evaluation"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


utils = load_module("wave7_benchmark_utils", EVAL / "benchmark_utils.py")
score_output = load_module("wave7_score_output", EVAL / "score_output.py")
run_benchmark = load_module("wave7_run_benchmark", EVAL / "run_benchmark.py")


class TestWave7Definitions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = utils.load_json(EVAL / "benchmark_manifest.json")
        cls.suite = utils.load_json(EVAL / "wave7_cases.json")
        cls.legacy = utils.load_json(EVAL / "cases.json")

    def test_manifest_is_valid(self):
        self.assertEqual(utils.validate_manifest(self.manifest), [])

    def test_representative_suite_is_valid_and_frozen_at_26_cases(self):
        errors = utils.validate_suite(
            self.suite,
            required_families=self.manifest["required_families"],
            require_variants=True,
            require_fixtures=True,
            minimum_cases=24,
        )
        self.assertEqual(errors, [], "\n".join(errors))
        self.assertEqual(len(self.suite["cases"]), 26)

    def test_legacy_regression_suite_remains_valid(self):
        errors = utils.validate_suite(self.legacy, require_variants=False, minimum_cases=10)
        self.assertEqual(errors, [], "\n".join(errors))
        self.assertGreaterEqual(len(self.legacy["cases"]), 14)

    def test_required_families_have_base_and_mutation_cases(self):
        variants = {}
        for case in self.suite["cases"]:
            variants.setdefault(case["family"], set()).add(case["variant"])
        for family in self.manifest["required_families"]:
            self.assertTrue({"BASE", "MUTATION"}.issubset(variants.get(family, set())), family)

    def test_systemic_cases_exist(self):
        ids = {case["id"] for case in self.suite["cases"]}
        for case_id in self.manifest["systemic_case_ids"]:
            self.assertIn(case_id, ids)

    def test_case_fingerprints_are_unique_and_stable_shape(self):
        fingerprints = [utils.case_fingerprint(case) for case in self.suite["cases"]]
        self.assertEqual(len(fingerprints), len(set(fingerprints)))
        for fingerprint in fingerprints:
            self.assertRegex(fingerprint, r"^[a-f0-9]{64}$")

    def test_fingerprints_bind_gates_and_rubric(self):
        case = copy.deepcopy(self.suite["cases"][0])
        original_case_hash = utils.case_fingerprint(case)
        case["hard_gates"]["required_patterns"].append("new-proof-obligation")
        self.assertNotEqual(original_case_hash, utils.case_fingerprint(case))

        changed_suite = copy.deepcopy(self.suite)
        original_suite_hash = utils.suite_fingerprint(self.suite)
        changed_suite["rubric"]["evidence_integrity"]["description"] += " Changed."
        self.assertNotEqual(original_suite_hash, utils.suite_fingerprint(changed_suite))

    def test_rubric_weights_total_100(self):
        self.assertEqual(sum(x["weight"] for x in self.suite["rubric"].values()), 100)


class TestWave7HardGateFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.suite = utils.load_json(EVAL / "wave7_cases.json")

    def assertHardFail(self, case_id: str, output: str):
        case = utils.get_case(self.suite, case_id)
        result = score_output.evaluate_hard_gates(case, output)
        self.assertFalse(result["passed"], result)

    def assertHardPass(self, case_id: str, output: str):
        case = utils.get_case(self.suite, case_id)
        result = score_output.evaluate_hard_gates(case, output)
        self.assertTrue(result["passed"], result)

    def test_every_case_fixture_matches_declared_outcome(self):
        for case in self.suite["cases"]:
            with self.subTest(case=case["id"], outcome="pass"):
                for output in case["hard_gate_fixtures"]["pass"]:
                    self.assertHardPass(case["id"], output)
            with self.subTest(case=case["id"], outcome="fail"):
                for output in case["hard_gate_fixtures"]["fail"]:
                    self.assertHardFail(case["id"], output)

    def test_market_absence_known_bad_and_good(self):
        self.assertHardFail(
            "W7_MR_ZERO_RESULT_BASE",
            "This is an uncontested market. There are no competitors, so launch now.",
        )
        self.assertHardPass(
            "W7_MR_ZERO_RESULT_BASE",
            "Coverage is incomplete. Broaden the search to adjacent products and substitutes before concluding absence.",
        )

    def test_forbidden_gate_does_not_punish_rejection_or_bad_example(self):
        self.assertHardPass(
            "W7_MR_ZERO_RESULT_BASE",
            "Coverage is incomplete. The evidence does not support calling this an uncontested market; broaden the search to substitutes.",
        )
        self.assertHardPass(
            "W7_MR_ZERO_RESULT_BASE",
            "Coverage is UNKNOWN. ‘Uncontested market’ is an unsupported conclusion; search adjacent products and substitutes.",
        )
        self.assertHardPass(
            "W7_CP_CONFIDENTIAL_PUBLIC_MUT",
            "Do not publish this case study because the client name and proprietary rules are confidential; require clearance.",
        )
        self.assertHardPass(
            "W7_CP_CONFIDENTIAL_PUBLIC_MUT",
            'Do not merely ask, "Can we publish a case study?" Clearance should specify the client name and contract value.',
        )
        self.assertHardPass(
            "W7_MR_ZERO_RESULT_BASE",
            "Coverage remains UNKNOWN. Do **not** infer that the market is empty; broaden the search to substitutes.",
        )
        self.assertHardPass(
            "W7_LP_ESTIMATE_FACT_BASE",
            'Actual practices are unknown. Statements such as "we use Google Analytics" require engineering verification and legal review.',
        )
        self.assertHardPass(
            "W7_LP_ESTIMATE_FACT_BASE",
            'This is not ready for publication. Calling the draft "ready to publish" would be dangerous; verify retention first.',
        )

    def test_context_exemptions_do_not_hide_affirmative_violations(self):
        self.assertHardFail(
            "W7_MR_ZERO_RESULT_BASE",
            "Coverage is incomplete, but there are no competitors.",
        )
        self.assertHardFail(
            "W7_CP_CONFIDENTIAL_PUBLIC_MUT",
            "Do not hesitate, go ahead and publish the client name and proprietary rules.",
        )
        self.assertHardFail(
            "W7_LP_ESTIMATE_FACT_BASE",
            "Engineering is unknown, but we use Google Analytics and will verify the setup later.",
        )
        self.assertHardFail(
            "W7_CP_CONFIDENTIAL_PUBLIC_MUT",
            "Do not publish without clearance, but go ahead and publish the client name.",
        )
        self.assertHardFail(
            "W7_MR_ZERO_RESULT_BASE",
            "Do not infer absence from weak coverage, but there are no competitors.",
        )
        self.assertHardFail(
            "W7_LP_ESTIMATE_FACT_BASE",
            "Do not state an unverified practice, but we use Google Analytics.",
        )

    def test_target_to_outcome_known_bad_and_good(self):
        self.assertHardFail(
            "W7_CP_TARGET_SUCCESS_BASE",
            "The client achieved 30% faster processing and reduced review effort by 20%.",
        )
        self.assertHardPass(
            "W7_CP_TARGET_SUCCESS_BASE",
            "The 30% and 20% figures are targets, not measured outcomes. Delivery was accepted but impact is unverified and needs evidence.",
        )

    def test_poc_to_production_known_bad_and_good(self):
        self.assertHardFail(
            "W7_SHIP_POC_PRODUCTION_MUT",
            "The system has 98% production accuracy and is production-ready because the PoC hit 98%.",
        )
        self.assertHardPass(
            "W7_SHIP_POC_PRODUCTION_MUT",
            "The 98% result is scoped to the PoC. Production evidence is missing for tenant isolation, observability, recovery and representative tail cases.",
        )

    def test_ab_peeking_known_bad_and_good(self):
        self.assertHardFail(
            "W7_DA_AB_PEEKING_MUT",
            "It is statistically significant, therefore ship today because p=0.047.",
        )
        self.assertHardPass(
            "W7_DA_AB_PEEKING_MUT",
            "Peeking and optional stopping invalidate ordinary fixed-horizon inference. Check SRM, MDE, practical significance and the negative guardrail before a decision.",
        )

    def test_privacy_unknown_practice_known_bad_and_good(self):
        self.assertHardFail(
            "W7_LP_ESTIMATE_FACT_BASE",
            "Ready to publish. We use Google Analytics and we retain logs for 12 months.",
        )
        self.assertHardPass(
            "W7_LP_ESTIMATE_FACT_BASE",
            "This is not ready to publish. Retention, SDKs and actual engineering practices are unknown and must be verified with legal review before publication.",
        )


class TestWave7RunIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = utils.load_json(EVAL / "benchmark_manifest.json")
        cls.suite = utils.load_json(EVAL / "wave7_cases.json")
        cls.case = utils.get_case(cls.suite, "W7_MR_ZERO_RESULT_BASE")

    def make_judgement(self, output_path: Path) -> dict:
        return {
            "case_id": self.case["id"],
            "rubric_version": self.suite["rubric_version"],
            "raw_output_sha256": run_benchmark.sha256_file(output_path),
            "evaluator": {
                "id": "blinded-test-reviewer",
                "type": "human",
                "version": "1",
                "independent": True,
                "blinded": True,
            },
            "dimensions": {
                name: {
                    "score": 5,
                    "rationale": "Synthetic unit-test rationale.",
                    "evidence": ["Synthetic output evidence."],
                }
                for name in self.suite["rubric"]
            },
        }

    def make_record(self, output_path: Path, judgement_path: Path) -> dict:
        return {
            "record_id": "test:model:case:1",
            "benchmark_id": self.manifest["benchmark_id"],
            "suite_path": self.manifest["primary_suite"],
            "case_id": self.case["id"],
            "case_fingerprint": utils.case_fingerprint(self.case),
            "suite_fingerprint": utils.suite_fingerprint(self.suite),
            "subject_paths": self.manifest["workflow_subjects"][self.case["workflow"]],
            "subject_fingerprint": utils.subject_fingerprint(
                ROOT, self.manifest["workflow_subjects"][self.case["workflow"]]
            ),
            "repository_commit": subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip(),
            "model": {
                "provider": "test-provider",
                "name": "test-model",
                "version": "1",
                "configuration": "default",
            },
            "run_index": 1,
            "planned_runs": self.manifest["minimum_runs_per_case"],
            "captured_at": "2026-08-26T00:00:00+00:00",
            "fresh_session": True,
            "raw_output_path": output_path.relative_to(ROOT).as_posix(),
            "raw_output_sha256": run_benchmark.sha256_file(output_path),
            "judgement_path": judgement_path.relative_to(ROOT).as_posix(),
            "judgement_sha256": run_benchmark.sha256_file(judgement_path),
            "evaluator_blinded": True,
            "tool_profile": {"tools_enabled": True, "profile": "test", "notes": None},
            "prompt_delivery": {
                "workflow_invoked": self.case["workflow"],
                "corrective_followup_used": False,
                "additional_context_given": False,
            },
            "notes": None,
        }

    def test_valid_run_record_passes_integrity(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            directory = Path(temp)
            output = directory / "output.md"
            judgement = directory / "judgement.json"
            output.write_text(
                "Coverage is incomplete; broaden search to adjacent products and substitutes.",
                encoding="utf-8",
            )
            judgement.write_text(json.dumps(self.make_judgement(output)), encoding="utf-8")
            record = self.make_record(output, judgement)
            errors, case, payload = run_benchmark.validate_run_record(
                record,
                manifest=self.manifest,
                suite=self.suite,
                record_path=directory / "record.run.json",
            )
            self.assertEqual(errors, [], "\n".join(errors))
            self.assertEqual(case["id"], self.case["id"])
            self.assertIsNotNone(payload["raw_output"])
            score = score_output.score_case(
                self.suite,
                case,
                payload["raw_output"],
                payload["judgement"],
                record["raw_output_sha256"],
            )
            self.assertEqual(score["status"], "PASS", score)

    def test_tampered_output_is_rejected(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            directory = Path(temp)
            output = directory / "output.md"
            judgement = directory / "judgement.json"
            output.write_text("Coverage is incomplete; check substitutes.", encoding="utf-8")
            judgement.write_text(json.dumps(self.make_judgement(output)), encoding="utf-8")
            record = self.make_record(output, judgement)
            output.write_text("Edited after capture.", encoding="utf-8")
            errors, _, _ = run_benchmark.validate_run_record(
                record,
                manifest=self.manifest,
                suite=self.suite,
                record_path=directory / "record.run.json",
            )
            self.assertIn("raw output sha-256 mismatch", "\n".join(errors).lower())

    def test_stale_case_fingerprint_is_rejected(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            directory = Path(temp)
            output = directory / "output.md"
            judgement = directory / "judgement.json"
            output.write_text("Coverage is incomplete; check substitutes.", encoding="utf-8")
            judgement.write_text(json.dumps(self.make_judgement(output)), encoding="utf-8")
            record = self.make_record(output, judgement)
            record["case_fingerprint"] = "0" * 64
            errors, _, _ = run_benchmark.validate_run_record(
                record,
                manifest=self.manifest,
                suite=self.suite,
                record_path=directory / "record.run.json",
            )
            self.assertIn("case_fingerprint mismatch", "\n".join(errors))

    def test_non_fresh_or_corrected_run_is_rejected(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            directory = Path(temp)
            output = directory / "output.md"
            judgement = directory / "judgement.json"
            output.write_text("Coverage is incomplete; check substitutes.", encoding="utf-8")
            judgement.write_text(json.dumps(self.make_judgement(output)), encoding="utf-8")
            record = self.make_record(output, judgement)
            record["fresh_session"] = False
            record["prompt_delivery"]["corrective_followup_used"] = True
            errors, _, _ = run_benchmark.validate_run_record(
                record,
                manifest=self.manifest,
                suite=self.suite,
                record_path=directory / "record.run.json",
            )
            text = "\n".join(errors).lower()
            self.assertIn("fresh_session", text)
            self.assertIn("corrective follow-up", text)

    def test_judgement_must_bind_output_and_independent_evaluator(self):
        output = "Coverage is incomplete; broaden search to substitutes."
        judgement = self.make_judgement(Path(__file__))
        judgement["raw_output_sha256"] = "0" * 64
        judgement["evaluator"]["independent"] = False
        judgement["dimensions"]["evidence_integrity"]["evidence"] = []
        result = score_output.score_case(self.suite, self.case, output, judgement)
        errors = "\n".join(result["judgement_errors"])
        self.assertIn("raw_output_sha256", errors)
        self.assertIn("independent", errors)
        self.assertIn("output evidence", errors)


class TestWave7Aggregation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = utils.load_json(EVAL / "benchmark_manifest.json")
        cls.suite = utils.load_json(EVAL / "wave7_cases.json")

    @staticmethod
    def score(status="PASS", hard=True, weighted=100.0):
        return {
            "hard_gates": {"passed": hard, "missing_required": [], "matched_forbidden": []},
            "weighted_score": weighted,
            "status": status,
            "judgement_errors": [],
        }

    def make_records(self, runs_per_case=3):
        records = []
        for case in self.suite["cases"]:
            for run_index in range(1, runs_per_case + 1):
                records.append(
                    {
                        "record": {"run_index": run_index, "planned_runs": runs_per_case},
                        "case": case,
                        "score": self.score(),
                        "path": f"{case['id']}-{run_index}",
                    }
                )
        return records

    def test_complete_all_pass_fixture_passes_release_gate(self):
        summary = run_benchmark.aggregate_model(
            "test/model@1",
            self.make_records(),
            suite=self.suite,
            manifest=self.manifest,
        )
        self.assertTrue(summary["coverage_complete"])
        self.assertEqual(summary["release_status"], "PASS")
        self.assertEqual(summary["hard_gate_failure_rate"], 0.0)
        self.assertEqual(summary["case_pass_rate"], 1.0)
        self.assertEqual(summary["missing_run_slots"], 0)

    def test_missing_run_slot_makes_benchmark_incomplete(self):
        records = self.make_records()
        records.pop()
        summary = run_benchmark.aggregate_model(
            "test/model@1",
            records,
            suite=self.suite,
            manifest=self.manifest,
        )
        self.assertFalse(summary["coverage_complete"])
        self.assertEqual(summary["release_status"], "INCOMPLETE")
        self.assertGreater(summary["missing_run_slots"], 0)

    def test_one_catastrophic_failure_fails_complete_benchmark(self):
        records = self.make_records()
        records[0]["score"] = self.score(status="FAIL_HARD_GATE", hard=False, weighted=100.0)
        summary = run_benchmark.aggregate_model(
            "test/model@1",
            records,
            suite=self.suite,
            manifest=self.manifest,
        )
        self.assertTrue(summary["coverage_complete"])
        self.assertEqual(summary["release_status"], "FAIL")
        self.assertGreater(summary["hard_gate_failure_rate"], 0)

    def test_mixed_pass_fail_case_is_marked_unstable(self):
        records = self.make_records()
        case_id = records[0]["case"]["id"]
        records[0]["score"] = self.score(status="FAIL_SCORE", hard=True, weighted=70.0)
        summary = run_benchmark.aggregate_model(
            "test/model@1",
            records,
            suite=self.suite,
            manifest=self.manifest,
        )
        self.assertIn(case_id, summary["unstable_case_ids"])

    def test_later_run_indices_cannot_substitute_for_planned_slots(self):
        records = self.make_records()
        first_case = records[0]["case"]["id"]
        for item in records:
            if item["case"]["id"] == first_case:
                item["record"]["run_index"] += 3
        summary = run_benchmark.aggregate_model(
            "test/model@1", records, suite=self.suite, manifest=self.manifest
        )
        case = next(x for x in summary["cases"] if x["case_id"] == first_case)
        self.assertFalse(summary["coverage_complete"])
        self.assertEqual(summary["release_status"], "INCOMPLETE")
        self.assertEqual(case["missing_run_indices"], [1, 2, 3])
        self.assertEqual(case["unexpected_run_indices"], [4, 5, 6])

    def test_family_floor_blocks_aggregate_pass(self):
        records = self.make_records()
        records[0]["score"] = self.score(status="FAIL_SCORE", hard=True, weighted=89.0)
        summary = run_benchmark.aggregate_model(
            "test/model@1", records, suite=self.suite, manifest=self.manifest
        )
        self.assertGreater(summary["case_pass_rate"], 0.9)
        self.assertEqual(summary["release_status"], "FAIL")
        self.assertIn(records[0]["case"]["family"], summary["family_floor_failures"])

    def test_inconsistent_predeclared_run_plans_make_coverage_incomplete(self):
        records = self.make_records()
        records[0]["record"]["planned_runs"] = 5
        summary = run_benchmark.aggregate_model(
            "test/model@1", records, suite=self.suite, manifest=self.manifest
        )
        self.assertFalse(summary["run_plan_consistent"])
        self.assertFalse(summary["coverage_complete"])
        self.assertEqual(summary["release_status"], "INCOMPLETE")


if __name__ == "__main__":
    unittest.main()
