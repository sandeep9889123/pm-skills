"""Tests for zero-cost manual UI benchmark capture."""

from __future__ import annotations

import importlib.util
import hashlib
import json
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


manual_capture = load_module("manual_capture_wave9", EVAL / "manual_capture.py")
run_benchmark = load_module("run_benchmark_wave9", EVAL / "run_benchmark.py")
utils = load_module("benchmark_utils_wave9", EVAL / "benchmark_utils.py")


class TestWave9ManualCapture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = utils.load_json(EVAL / "benchmark_manifest.json")
        cls.suite = utils.load_json(EVAL / "wave7_cases.json")
        cls.case = cls.suite["cases"][0]

    def make_prepare_args(self, output_root: Path, **overrides):
        values = {
            "provider": "ChatGPT",
            "model": "GPT-5.6",
            "version": "manual-ui-2026-08-26",
            "interface": "chatgpt-web",
            "case_ids": self.case["id"],
            "allow_all": False,
            "planned_runs": 3,
            "exploratory": False,
            "tools_enabled": False,
            "tool_profile": "manual-ui-no-external-tools",
            "tool_notes": "Manual UI run; no paid API calls.",
            "output_root": output_root,
            "manifest": EVAL / "benchmark_manifest.json",
            "resume": False,
        }
        values.update(overrides)
        return type("Args", (), values)()

    def test_prepare_creates_prompt_packs_without_rubric_leakage(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            cell = manual_capture.prepare_manual(self.make_prepare_args(Path(temp)))
            plan = json.loads((cell / "manual-plan.json").read_text(encoding="utf-8"))
            self.assertEqual(plan["capture_mode"], "manual_ui")
            self.assertEqual(plan["cost_policy"], "zero paid API calls; manual subscription UI or local model only")
            prompt_path = cell / self.case["id"] / "run-1.manual-prompt.md"
            prompt = prompt_path.read_text(encoding="utf-8")
            self.assertIn("## SYSTEM", prompt)
            self.assertIn("## USER", prompt)
            self.assertIn(self.case["prompt"], prompt)
            self.assertNotIn("expected_behaviors", prompt)
            self.assertNotIn("hard_gates", prompt)
            self.assertNotIn("evidence_integrity", prompt)
            self.assertNotIn("decision_usefulness", prompt)

    def test_exploratory_mode_allows_one_run_without_weakening_qualification(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            with self.assertRaises(manual_capture.ManualCaptureError):
                manual_capture.prepare_manual(
                    self.make_prepare_args(Path(temp), planned_runs=1)
                )

        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            cell = manual_capture.prepare_manual(
                self.make_prepare_args(Path(temp), planned_runs=1, exploratory=True)
            )
            plan = json.loads((cell / "manual-plan.json").read_text(encoding="utf-8"))
            self.assertEqual(plan["qualification_scope"], "exploratory")
            self.assertEqual(plan["planned_runs"], 1)
            output = cell / self.case["id"] / "run-1.md"
            output.write_text(
                "Coverage is incomplete; broaden search to substitutes before claiming no competitors.",
                encoding="utf-8",
            )
            manual_capture.record_manual(
                type("Args", (), {"cell": cell, "manifest": EVAL / "benchmark_manifest.json"})()
            )
            record_path = cell / self.case["id"] / "run-1.run.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            self.assertEqual(record["qualification_scope"], "exploratory")
            errors, _, _ = run_benchmark.validate_run_record(
                record,
                manifest=self.manifest,
                suite=self.suite,
                record_path=record_path,
            )
            self.assertEqual(errors, [], "\n".join(errors))

    def test_run_record_schema_covers_manual_and_automated_capture(self):
        schema = json.loads((EVAL / "run_record.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(
            schema["properties"]["qualification_scope"]["enum"],
            ["qualification", "exploratory"],
        )
        capture_variants = schema["properties"]["capture"]["oneOf"]
        modes = {variant["properties"]["mode"]["const"] for variant in capture_variants}
        self.assertEqual(modes, {"automated_api", "manual_ui"})

    def test_manual_record_is_valid_incomplete_until_judged(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            cell = manual_capture.prepare_manual(self.make_prepare_args(Path(temp)))
            for run_index in range(1, 4):
                output = cell / self.case["id"] / f"run-{run_index}.md"
                output.write_text(
                    "Coverage is incomplete; broaden search to substitutes before claiming no competitors.",
                    encoding="utf-8",
                )
            manual_capture.record_manual(type("Args", (), {"cell": cell, "manifest": EVAL / "benchmark_manifest.json"})())

            record_path = cell / self.case["id"] / "run-1.run.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            self.assertEqual(record["capture"]["mode"], "manual_ui")
            self.assertTrue(record["capture"]["operator_attestation"]["first_response_only"])
            errors, case, payload = run_benchmark.validate_run_record(
                record,
                manifest=self.manifest,
                suite=self.suite,
                record_path=record_path,
            )
            self.assertEqual(errors, [], "\n".join(errors))
            score = run_benchmark.score_case(
                self.suite,
                case,
                payload["raw_output"],
                payload["judgement"],
                record["raw_output_sha256"],
            )
            self.assertEqual(score["status"], "HARD_GATE_PASS_UNSCORED")

    def test_manual_record_preserves_post_capture_tool_observation(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            cell = manual_capture.prepare_manual(self.make_prepare_args(Path(temp)))
            for run_index in range(1, 4):
                output = cell / self.case["id"] / f"run-{run_index}.md"
                output.write_text(
                    "Coverage is incomplete; broaden search to substitutes before claiming no competitors.",
                    encoding="utf-8",
                )
            manual_capture.record_manual(
                type(
                    "Args",
                    (),
                    {
                        "cell": cell,
                        "manifest": EVAL / "benchmark_manifest.json",
                        "actual_tools": "enabled",
                        "actual_tool_profile": "manual-ui-web-observed",
                        "tool_observation_notes": "Source links in the raw output indicate provider-driven browsing.",
                        "overwrite_records": False,
                    },
                )()
            )

            record_path = cell / self.case["id"] / "run-1.run.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            self.assertTrue(record["tool_profile"]["tools_enabled"])
            self.assertEqual(record["tool_profile"]["profile"], "manual-ui-web-observed")
            deviation = record["capture"]["execution_deviation"]
            self.assertFalse(deviation["planned_tools_enabled"])
            self.assertTrue(deviation["observed_tools_enabled"])
            errors, _, _ = run_benchmark.validate_run_record(
                record,
                manifest=self.manifest,
                suite=self.suite,
                record_path=record_path,
            )
            self.assertEqual(errors, [], "\n".join(errors))

    def test_manual_record_attaches_adjacent_valid_judgement(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            cell = manual_capture.prepare_manual(self.make_prepare_args(Path(temp)))
            rubric = self.suite["rubric"]
            for run_index in range(1, 4):
                output = cell / self.case["id"] / f"run-{run_index}.md"
                output.write_text(
                    "Coverage is incomplete; broaden search to substitutes before claiming no competitors.",
                    encoding="utf-8",
                )
                judgement = {
                    "case_id": self.case["id"],
                    "rubric_version": self.suite["rubric_version"],
                    "raw_output_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                    "evaluator": {
                        "id": "independent-test-reviewer",
                        "type": "model",
                        "version": "test",
                        "independent": True,
                        "blinded": False,
                    },
                    "dimensions": {
                        name: {
                            "score": 5,
                            "rationale": "Fixture meets the declared criterion.",
                            "evidence": ["The output preserves incomplete coverage."],
                        }
                        for name in rubric
                    },
                }
                (cell / self.case["id"] / f"run-{run_index}.judgement.json").write_text(
                    json.dumps(judgement), encoding="utf-8"
                )
            manual_capture.record_manual(
                type("Args", (), {"cell": cell, "manifest": EVAL / "benchmark_manifest.json"})()
            )
            record = json.loads(
                (cell / self.case["id"] / "run-1.run.json").read_text(encoding="utf-8")
            )
            self.assertTrue(record["judgement_path"].endswith("run-1.judgement.json"))
            self.assertFalse(record["evaluator_blinded"])

    def test_manual_record_rejects_placeholder_outputs(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            cell = manual_capture.prepare_manual(self.make_prepare_args(Path(temp)))
            with self.assertRaises(manual_capture.ManualCaptureError):
                manual_capture.record_manual(type("Args", (), {"cell": cell, "manifest": EVAL / "benchmark_manifest.json"})())

    def test_manual_capture_integrity_detects_prompt_tampering(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            cell = manual_capture.prepare_manual(self.make_prepare_args(Path(temp)))
            for run_index in range(1, 4):
                output = cell / self.case["id"] / f"run-{run_index}.md"
                output.write_text(
                    "Coverage is incomplete; broaden search to substitutes before claiming no competitors.",
                    encoding="utf-8",
                )
            manual_capture.record_manual(type("Args", (), {"cell": cell, "manifest": EVAL / "benchmark_manifest.json"})())
            prompt_path = cell / self.case["id"] / "run-1.manual-prompt.md"
            prompt_path.write_text(prompt_path.read_text(encoding="utf-8") + "\nTampered.\n", encoding="utf-8")

            record_path = cell / self.case["id"] / "run-1.run.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            errors, _, _ = run_benchmark.validate_run_record(
                record,
                manifest=self.manifest,
                suite=self.suite,
                record_path=record_path,
            )
            self.assertIn("capture.manual_prompt_sha256 mismatch", errors)


if __name__ == "__main__":
    unittest.main()
