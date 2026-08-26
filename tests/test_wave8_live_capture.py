"""Tests for tamper-evident, predeclared live benchmark capture."""

from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
EVAL = ROOT / "evaluation"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


capture = load_module("capture_baseline", EVAL / "capture_baseline.py")
run_benchmark = load_module("run_benchmark_wave8", EVAL / "run_benchmark.py")
utils = load_module("benchmark_utils_wave8", EVAL / "benchmark_utils.py")


class TestWave8PromptAndAdapters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = utils.load_json(EVAL / "benchmark_manifest.json")
        cls.suite = utils.load_json(EVAL / "wave7_cases.json")
        cls.case = cls.suite["cases"][0]

    def test_prompt_bundle_excludes_scoring_and_expected_behavior(self):
        bundle = capture.build_prompt_bundle(
            self.case,
            self.manifest["workflow_subjects"][self.case["workflow"]],
        )
        rendered = json.dumps(bundle)
        self.assertNotIn("expected_behaviors", rendered)
        self.assertNotIn("hard_gates", rendered)
        self.assertNotIn("rubric", rendered)
        self.assertIn(self.case["prompt"], bundle["model_visible"]["user"])
        self.assertIn(self.case["context"], bundle["model_visible"]["user"])

    def test_openai_request_and_response_use_all_text_blocks(self):
        bundle = capture.build_prompt_bundle(
            self.case,
            self.manifest["workflow_subjects"][self.case["workflow"]],
        )
        request = capture.build_request(
            "openai-responses", "gpt-test", bundle, 5000, reasoning_effort="low"
        )
        self.assertFalse(request["store"])
        self.assertEqual(request["reasoning"], {"effort": "low"})
        self.assertNotIn("tools", request)
        output, request_id, response_model = capture.extract_response(
            "openai-responses",
            {
                "id": "resp_1",
                "model": "gpt-test-2026-08-26",
                "output": [
                    {
                        "type": "message",
                        "content": [
                            {"type": "output_text", "text": "first"},
                            {"type": "output_text", "text": "second"},
                        ],
                    }
                ],
            },
        )
        self.assertEqual(output, "firstsecond")
        self.assertEqual(request_id, "resp_1")
        self.assertEqual(response_model, "gpt-test-2026-08-26")

    def test_anthropic_request_uses_top_level_system_and_no_tools(self):
        bundle = capture.build_prompt_bundle(
            self.case,
            self.manifest["workflow_subjects"][self.case["workflow"]],
        )
        request = capture.build_request(
            "anthropic-messages", "claude-test", bundle, 5000, temperature=0.2
        )
        self.assertEqual(request["messages"][0]["role"], "user")
        self.assertIn("system", request)
        self.assertNotIn("tools", request)
        output, _, _ = capture.extract_response(
            "anthropic-messages",
            {
                "id": "msg_1",
                "model": "claude-test-20260826",
                "content": [{"type": "text", "text": "answer"}],
            },
        )
        self.assertEqual(output, "answer")

    def test_empty_or_refusal_response_is_not_silently_dropped(self):
        empty, _, _ = capture.extract_response(
            "openai-responses",
            {"id": "resp_empty", "model": "gpt-test", "output": []},
        )
        self.assertEqual(empty, "")
        refusal, _, _ = capture.extract_response(
            "openai-responses",
            {
                "id": "resp_refusal",
                "model": "gpt-test",
                "output": [
                    {
                        "type": "message",
                        "content": [{"type": "refusal", "refusal": "Cannot comply."}],
                    }
                ],
            },
        )
        self.assertEqual(refusal, "Cannot comply.")

    def test_endpoint_rejects_embedded_credentials_or_query(self):
        with self.assertRaises(capture.CaptureError):
            capture.validate_endpoint("https://user:secret@example.com/v1/messages")
        with self.assertRaises(capture.CaptureError):
            capture.validate_endpoint("https://example.com/v1/messages?token=secret")


class TestWave8CaptureLifecycle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = utils.load_json(EVAL / "benchmark_manifest.json")
        cls.suite = utils.load_json(EVAL / "wave7_cases.json")
        cls.case = cls.suite["cases"][0]

    def make_args(self, output_root: Path, **overrides):
        values = {
            "adapter": "openai-responses",
            "model": "gpt-test",
            "endpoint": "https://example.test/v1/responses",
            "api_key_env": "WAVE8_TEST_API_KEY",
            "case_ids": self.case["id"],
            "allow_all": False,
            "planned_runs": 3,
            "max_output_tokens": 5000,
            "temperature": None,
            "reasoning_effort": "low",
            "timeout_seconds": 30,
            "output_root": output_root,
            "manifest": EVAL / "benchmark_manifest.json",
            "resume": False,
            "dry_run": False,
        }
        values.update(overrides)
        return type("Args", (), values)()

    def test_capture_predeclares_plan_and_unjudged_records_are_valid_incomplete(self):
        calls = []

        def fake_transport(endpoint, headers, body, timeout):
            calls.append((endpoint, headers, body, timeout))
            index = len(calls)
            return {
                "id": f"resp_{index}",
                "model": "gpt-test-2026-08-26",
                "output": [
                    {
                        "type": "message",
                        "content": [
                            {
                                "type": "output_text",
                                "text": "Coverage is incomplete; broaden search to substitutes.",
                            }
                        ],
                    }
                ],
            }

        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            output_root = Path(temp) / "runs"
            args = self.make_args(output_root)
            with mock.patch.dict(os.environ, {"WAVE8_TEST_API_KEY": "test-secret"}):
                cell_dir = capture.run_capture(args, transport=fake_transport)

            self.assertEqual(len(calls), 3)
            plan = json.loads((cell_dir / "run-plan.json").read_text(encoding="utf-8"))
            self.assertEqual(plan["planned_runs"], 3)
            self.assertEqual(plan["case_ids"], [self.case["id"]])
            self.assertEqual(plan["retry_policy"], "no automatic retries")

            record_path = cell_dir / self.case["id"] / "run-1.run.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            self.assertIsNone(record["evaluator_blinded"])
            self.assertEqual(record["capture"]["provider_request_id"], "resp_1")
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

    def test_resume_rejects_a_changed_predeclared_plan(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            output_root = Path(temp) / "runs"
            args = self.make_args(output_root, dry_run=True)
            capture.run_capture(args)
            changed = self.make_args(
                output_root,
                dry_run=True,
                resume=True,
                planned_runs=4,
            )
            with self.assertRaises(capture.CaptureError):
                capture.run_capture(changed)

    def test_complete_raw_capture_without_judgements_is_incomplete_not_invalid(self):
        records = []
        for case in self.suite["cases"]:
            for run_index in range(1, 4):
                records.append(
                    {
                        "record": {"run_index": run_index, "planned_runs": 3},
                        "case": case,
                        "score": {
                            "hard_gates": {
                                "passed": True,
                                "missing_required": [],
                                "matched_forbidden": [],
                            },
                            "weighted_score": None,
                            "status": "HARD_GATE_PASS_UNSCORED",
                            "judgement_errors": [],
                        },
                        "path": f"{case['id']}-{run_index}",
                    }
                )
        summary = run_benchmark.aggregate_model(
            "test/model@1", records, suite=self.suite, manifest=self.manifest
        )
        self.assertTrue(summary["capture_complete"])
        self.assertFalse(summary["coverage_complete"])
        self.assertEqual(summary["release_status"], "INCOMPLETE")
        self.assertIsNone(summary["case_pass_rate"])
        self.assertEqual(summary["evaluator_profiles"], [])

    def test_unjudged_mixed_hard_gate_outcomes_are_unstable(self):
        case = self.suite["cases"][0]
        results = [
            {
                "hard_gates": {
                    "passed": value,
                    "missing_required": [] if value else ["required"],
                    "matched_forbidden": [],
                },
                "weighted_score": None,
                "status": "HARD_GATE_PASS_UNSCORED" if value else "HARD_GATE_FAIL",
            }
            for value in (True, False, True)
        ]
        summary = run_benchmark.summarize_case_results(
            case, results, minimum_runs=3, run_indices={1, 2, 3}
        )
        self.assertTrue(summary["mixed_hard_gate"])
        self.assertTrue(summary["mixed_pass_fail"])


if __name__ == "__main__":
    unittest.main()
