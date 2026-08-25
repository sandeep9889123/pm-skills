"""Semantic reliability regression tests for the PM Skills fork.

These tests do not claim to evaluate LLM output quality end to end. They protect
critical behavior guards and scenario coverage from silently disappearing during
future edits or upstream syncs.
"""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "reliability" / "scenario_matrix.json"


def plugin_dirs():
    return sorted(
        p
        for p in ROOT.iterdir()
        if p.is_dir() and p.name.startswith("pm-") and (p / "skills").is_dir()
    )


def skill_files(plugin: Path):
    return sorted((plugin / "skills").glob("*/SKILL.md"))


class TestScenarioCoverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matrix = json.loads(MATRIX.read_text(encoding="utf-8"))

    def test_global_scenarios_are_defined(self):
        scenarios = self.matrix.get("global_scenarios", [])
        self.assertGreaterEqual(
            len(scenarios),
            10,
            "Reliability matrix should cover broad adversarial scenario families",
        )
        self.assertIn("G6_ZERO_RESULT_FIRST_PASS", scenarios)
        self.assertIn("G3_FALSE_USER_PREMISE", scenarios)
        self.assertIn("G11_TOOL_FAILURE", scenarios)

    def test_every_plugin_has_domain_specific_scenarios(self):
        mapped = self.matrix.get("plugin_scenarios", {})
        on_disk = {p.name for p in plugin_dirs()}
        self.assertEqual(
            set(mapped),
            on_disk,
            f"Scenario mapping must match plugin set. mapped={sorted(mapped)}, disk={sorted(on_disk)}",
        )
        for plugin_name, scenarios in mapped.items():
            self.assertGreaterEqual(
                len(scenarios),
                4,
                f"{plugin_name} needs at least four domain-specific adversarial scenarios",
            )

    def test_every_skill_inherits_scenario_coverage(self):
        """Every skill is covered by global + plugin-specific scenario families."""
        global_scenarios = self.matrix["global_scenarios"]
        mapped = self.matrix["plugin_scenarios"]
        uncovered = []
        total = 0
        for plugin in plugin_dirs():
            plugin_scenarios = mapped.get(plugin.name, [])
            for skill in skill_files(plugin):
                total += 1
                if not global_scenarios or not plugin_scenarios:
                    uncovered.append(str(skill.relative_to(ROOT)))
        self.assertGreater(total, 0, "No skills discovered")
        self.assertEqual(uncovered, [], f"Skills without scenario coverage: {uncovered}")


class TestHighRiskBehaviorGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matrix = json.loads(MATRIX.read_text(encoding="utf-8"))

    def test_required_behavior_guards_exist(self):
        failures = []
        contracts = self.matrix.get("high_risk_contracts", {})
        self.assertTrue(contracts, "No high-risk behavior contracts defined")

        for rel_path, contract in contracts.items():
            path = ROOT / rel_path
            if not path.is_file():
                failures.append(f"missing file: {rel_path}")
                continue
            text = path.read_text(encoding="utf-8")
            lower = text.lower()
            for required in contract.get("must_contain", []):
                if required.lower() not in lower:
                    failures.append(f"{rel_path}: missing guard phrase {required!r}")

        self.assertEqual(failures, [], "\n".join(failures))

    def test_competitor_analysis_has_negative_conclusion_guard(self):
        text = (
            ROOT
            / "pm-market-research"
            / "skills"
            / "competitor-analysis"
            / "SKILL.md"
        ).read_text(encoding="utf-8").lower()

        self.assertIn("never say there are no competitors", text)
        self.assertIn("first-pass search", text)
        self.assertIn("search exhaustion gate", text)
        self.assertIn("contradiction pass", text)
        self.assertIn("substitutes", text)
        self.assertIn("in-house", text)
        self.assertIn("regional", text)
        self.assertIn("emerging", text)
        self.assertIn("never accept a user-supplied competitor as fact without verification", text)

    def test_interview_quotes_require_verification(self):
        text = (
            ROOT
            / "pm-product-discovery"
            / "skills"
            / "summarize-interview"
            / "SKILL.md"
        ).read_text(encoding="utf-8").lower()

        self.assertIn("verify every verbatim quote", text)
        self.assertIn("unverified quote", text)
        self.assertIn("quote verification", text)
        self.assertIn("observed", text)
        self.assertIn("inference", text)

    def test_ab_power_claim_requires_beta_term(self):
        text = (
            ROOT
            / "pm-data-analytics"
            / "skills"
            / "ab-test-analysis"
            / "SKILL.md"
        ).read_text(encoding="utf-8").lower()

        self.assertIn("z_(1-beta)", text)
        self.assertIn("sample ratio mismatch", text)
        self.assertIn("optional stopping", text)
        self.assertIn("post-hoc observed power", text)
        self.assertIn("non-significance", text)


class TestForkIdentity(unittest.TestCase):
    def test_readme_is_fork_specific_and_attributed(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Reliability-First Enterprise AI Edition", text)
        self.assertIn("phuryn/pm-skills", text)
        self.assertIn("sandeep9889123/pm-skills", text)
        self.assertIn("Search → Challenge → Expand → Verify → Conclude", text)


if __name__ == "__main__":
    unittest.main()
