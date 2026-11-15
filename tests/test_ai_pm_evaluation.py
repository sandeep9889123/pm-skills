"""Offline measurement and portability checks for AI PM procedures."""
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def module(name):
    path = ROOT / "evaluation" / "ai_pm" / (name + ".py")
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


judge = module("score_judge")
tasks = module("task_metrics")


def label(ident, human="PASS", prediction="PASS", split="test", group=None):
    return dict(case_id=ident, group_id=group or ident, split=split,
                human_label=human, judge_label=prediction)


class TestJudgeArithmetic(unittest.TestCase):
    def test_failure_positive_confusion_matrix_and_rates(self):
        rows = [label("a", "FAIL", "FAIL"), label("b", "FAIL", "FAIL"),
                label("c", "FAIL", "PASS"), label("d", "PASS", "FAIL"),
                label("e", "PASS", "PASS")]
        r = judge.score_rows(rows, provenance="human-reviewed", heldout_attested=True)
        self.assertEqual(r["confusion_matrix"], dict(TP=2, FN=1, TN=1, FP=1))
        self.assertAlmostEqual(r["conditional_binary_rates"]["failure_recall"]["value"], 2/3)
        self.assertEqual(r["conditional_binary_rates"]["specificity"]["value"], 0.5)
        self.assertEqual(r["readiness"], "OWNER_REVIEW_REQUIRED")

    def test_always_pass_cannot_hide_missing_failure_detection(self):
        r = judge.score_rows([label(str(i)) for i in range(9)] + [label("bad", "FAIL")])
        self.assertEqual(r["conditional_binary_rates"]["agreement"]["value"], 0.9)
        self.assertEqual(r["conditional_binary_rates"]["failure_recall"]["value"], 0)
        self.assertEqual(r["status"], "UNVERIFIED_LABEL_PROVENANCE")

    def test_undefined_class_is_not_perfect(self):
        r = judge.score_rows([label("a")], provenance="human-reviewed", heldout_attested=True)
        self.assertIsNone(r["conditional_binary_rates"]["failure_recall"]["value"])
        self.assertEqual(r["status"], "INCOMPLETE_CLASS_COVERAGE")

    def test_unresolved_and_abstained_rows_remain_visible(self):
        r = judge.score_rows([label("a", "FAIL", "ABSTAIN"), label("b", "UNRESOLVED"), label("c")],
                             provenance="human-reviewed", heldout_attested=True)
        self.assertEqual(r["status"], "INCOMPLETE_LABELS")
        self.assertEqual(len(r["excluded_from_binary_matrix"]), 2)
        self.assertEqual(r["failure_detection_all_human_failures"]["value"], 0)
        self.assertEqual(r["binary_pair_coverage"]["denominator"], 3)

    def test_group_leakage_and_duplicates_are_rejected(self):
        for rows in ([label("a"), label("a")],
                     [label("a", split="dev", group="same"), label("b", group="same")]):
            with self.assertRaises(ValueError):
                judge.score_rows(rows)

    def test_development_and_synthetic_do_not_become_test_alignment(self):
        rows = [label("a", split="dev"), label("b", "FAIL", "FAIL", split="dev")]
        self.assertEqual(judge.score_rows(rows, split="dev", provenance="human-reviewed")["status"], "DEVELOPMENT_ONLY")
        self.assertEqual(judge.score_rows(rows, split="dev", provenance="synthetic")["status"], "FIXTURE_ONLY")

    def test_intervals_require_declared_independence_and_no_repeated_groups(self):
        rows = [label("a"), label("b", "FAIL", "FAIL")]
        self.assertIsNone(judge.score_rows(rows)["conditional_binary_rates"]["agreement"]["wilson_95"])
        lo, hi = judge.wilson(10, 10)
        self.assertAlmostEqual(lo, 0.7224672, places=6)
        self.assertAlmostEqual(hi, 1.0)
        repeated = [label("a", group="g"), label("b", group="g")]
        r = judge.score_rows(repeated, independent_groups_attested=True)
        self.assertIsNone(r["conditional_binary_rates"]["agreement"]["wilson_95"])

    def test_csv_cli_records_fixture_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / "labels.csv"
            p.write_text("case_id,group_id,split,human_label,judge_label\na,a,test,FAIL,PASS\nb,b,test,PASS,PASS\n")
            result = subprocess.run([sys.executable, str(ROOT/"evaluation/ai_pm/score_judge.py"), str(p), "--provenance", "synthetic"],
                                    text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["status"], "FIXTURE_ONLY")


class TestTaskEconomics(unittest.TestCase):
    def rows(self):
        return [dict(task_id="ok", success=True, cost="0.25", currency="USD", cost_basis="complete", duration_ms=100),
                dict(task_id="failed", success=False, cost="0.75", currency="USD", cost_basis="complete", duration_ms=900)]

    def test_failed_task_costs_are_in_success_denominator(self):
        r = tasks.summarize(self.rows(), provenance="synthetic")
        self.assertEqual(r["complete_cost_per_successful_task"], "1.00")
        self.assertEqual(r["reported_cost_per_attempted_task"], "0.50")
        self.assertEqual(r["latency_ms"]["p95"], "900")
        self.assertEqual(r["status"], "FIXTURE_ONLY")

    def test_zero_success_and_missing_costs_never_become_zero(self):
        rows = self.rows()
        rows[0]["success"] = False
        self.assertIsNone(tasks.summarize(rows)["complete_cost_per_successful_task"])
        rows = self.rows(); rows[0]["cost_basis"] = "partial"
        r = tasks.summarize(rows)
        self.assertIsNone(r["complete_cost_per_successful_task"])
        self.assertEqual(r["known_cost_per_successful_task"], "1.00")

    def test_invalid_or_nonfinite_inputs_and_mixed_currency_are_rejected(self):
        mutations = [("cost", "NaN"), ("cost", -1), ("duration_ms", float("inf")),
                     ("success", "true"), ("cost", None), ("currency", "EUR")]
        for field, value in mutations:
            with self.subTest(field=field, value=value):
                rows = self.rows(); rows[0][field] = value
                with self.assertRaises(ValueError): tasks.summarize(rows)
        rows = self.rows();rows[1]["task_id"] = "ok"
        with self.assertRaises(ValueError):tasks.summarize(rows)

    def test_jsonl_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)/"tasks.jsonl"
            p.write_text("\n".join(json.dumps(r) for r in self.rows()))
            result = subprocess.run([sys.executable,str(ROOT/"evaluation/ai_pm/task_metrics.py"),str(p),"--provenance","synthetic"],
                                    text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads(result.stdout)["attempted_tasks"],2)


class TestAiPmPortability(unittest.TestCase):
    def test_standalone_plugin_links_resolve_without_parent_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory) / "pm-prototype-os"
            shutil.copytree(ROOT / "pm-prototype-os", package)
            for p in package.rglob("*.md"):
                for target in re.findall(r"\]\(([^\s)]+)\)", p.read_text()):
                    if target.startswith(("https:", "http:", "#", "mailto:")):
                        continue
                    resolved = (p.parent / target.split("#")[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(package.resolve()),
                                    f"{p.relative_to(package)} escapes package: {target}")
                    self.assertTrue(resolved.exists(), f"missing installed-package target: {target}")

    def test_all_prototype_markdown_links_resolve(self):
        for p in (ROOT/"pm-prototype-os").rglob("*.md"):
            for target in re.findall(r"\]\(([^\s)]+)\)",p.read_text()):
                if target.startswith(("https:","http:","#","mailto:")):continue
                path=(p.parent/target.split("#")[0]).resolve()
                self.assertTrue(path.exists(),f"{p.relative_to(ROOT)} -> {target}")

    def test_new_skills_have_own_portable_contract_and_references(self):
        for name in ("eval-annotation-guidance","eval-error-discovery","llm-judge-calibration"):
            folder=ROOT/"pm-prototype-os/skills"/name
            text=(folder/"SKILL.md").read_text()
            self.assertIn("name: "+name,text)
            self.assertIn("UNKNOWN",text)
            self.assertTrue(list((folder/"references").glob("*.md")))

    def test_forward_case_fixture_remains_synthetic_and_unique(self):
        data=json.loads((ROOT/"evaluation/ai_pm/forward_cases.json").read_text())
        self.assertEqual(data["kind"],"synthetic_forward_tasks")
        self.assertTrue(data["frozen_before_changes"])
        self.assertEqual(len(data["cases"]),len({c["id"] for c in data["cases"]}))


if __name__=="__main__":unittest.main()
