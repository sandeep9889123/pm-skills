"""Wave 5A semantic guard-regression tests.

These tests protect P0 runtime instructions for segmentation, feedback analysis,
cohorts, SQL, interview design, metrics, and their command wrappers.
They do not claim to grade arbitrary LLM outputs end-to-end.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONTRACTS = {
    "pm-market-research/skills/market-segments/SKILL.md": [
        "Do not force 3-5 segments",
        "No invented segment sizes",
        "Contradiction pass",
        "DO NOT SEGMENT YET",
        "Tool/search failure",
    ],
    "pm-market-research/skills/sentiment-analysis/SKILL.md": [
        "Do not invent a numeric sentiment score",
        "Do not create an NPS proxy",
        "Verify verbatim quotes",
        "selection-biased",
        "root-cause claim",
    ],
    "pm-data-analytics/skills/cohort-analysis/SKILL.md": [
        "eligible denominators",
        "NOT YET OBSERVABLE",
        "right-censored",
        "Descriptive difference",
        "Do not invent industry benchmarks",
    ],
    "pm-data-analytics/skills/sql-queries/SKILL.md": [
        "Never invent a table",
        "TEMPLATE - SCHEMA NOT VERIFIED",
        "Join cardinality",
        "Never fabricate query results",
        "production-ready",
    ],
    "pm-product-discovery/skills/interview-script/SKILL.md": [
        "Do not ask leading",
        "disconfirming probe",
        "small interview sample",
        "MUST ASK",
        "what cannot be inferred",
    ],
    "pm-product-discovery/skills/metrics-dashboard/SKILL.md": [
        "Do not invent current values",
        "NO VALID NSM YET",
        "Alert thresholds",
        "INSTRUMENTATION GAP",
        "Goodhart",
    ],
    "pm-market-research/commands/research-users.md": [
        "EVIDENCE MODE",
        "HYPOTHESIS MODE",
        "DO NOT CREATE PERSONAS YET",
        "DO NOT SEGMENT YET",
        "unsupported percentages",
    ],
    "pm-market-research/commands/analyze-feedback.md": [
        "Do not generate an arbitrary average sentiment score",
        "NPS proxy",
        "Verified Quotes",
        "Root-Cause Hypotheses",
        "selection mechanism",
    ],
    "pm-data-analytics/commands/analyze-cohorts.md": [
        "eligible denominators",
        "NOT YET OBSERVABLE",
        "industry benchmarks",
        "Alternative Explanations",
        "INCONCLUSIVE",
    ],
    "pm-data-analytics/commands/write-query.md": [
        "TEMPLATE - SCHEMA NOT VERIFIED",
        "do not infer plausible SaaS tables",
        "join cardinality",
        "Never fabricate execution results",
        "production-ready",
    ],
    "pm-product-discovery/commands/interview.md": [
        "preferred solution as a hypothesis",
        "verify every verbatim quote",
        "UNVERIFIED QUOTE",
        "population-level",
        "Never convert participant enthusiasm into demand proof",
    ],
    "pm-product-discovery/commands/setup-metrics.md": [
        "Do not force a North Star",
        "FIX DATA / INSTRUMENTATION FIRST",
        "Never invent current values",
        "Goodhart",
        "HYPOTHESIZED DRIVERS",
    ],
}


def normalize_markdown(text: str) -> str:
    """Ignore lightweight emphasis/code formatting while preserving semantics."""
    return text.lower().replace("*", "").replace("`", "")


class TestWave5AGuards(unittest.TestCase):
    def test_all_required_runtime_guards_exist(self):
        failures = []
        for rel_path, phrases in CONTRACTS.items():
            path = ROOT / rel_path
            if not path.is_file():
                failures.append(f"missing file: {rel_path}")
                continue
            text = normalize_markdown(path.read_text(encoding="utf-8"))
            for phrase in phrases:
                if normalize_markdown(phrase) not in text:
                    failures.append(f"{rel_path}: missing {phrase!r}")
        self.assertEqual(failures, [], "\n".join(failures))

    def test_forced_completion_regressions_are_absent(self):
        market_segments = normalize_markdown((ROOT / "pm-market-research/skills/market-segments/SKILL.md").read_text(encoding="utf-8"))
        sentiment = normalize_markdown((ROOT / "pm-market-research/skills/sentiment-analysis/SKILL.md").read_text(encoding="utf-8"))
        research_users = normalize_markdown((ROOT / "pm-market-research/commands/research-users.md").read_text(encoding="utf-8"))

        self.assertNotIn("create 3-5 distinct", market_segments)
        self.assertNotIn("identify at least 3 distinct", sentiment)
        self.assertNotIn("identify 3-4 distinct personas", research_users)

    def test_sql_no_schema_mode_is_explicitly_non_final(self):
        skill = normalize_markdown((ROOT / "pm-data-analytics/skills/sql-queries/SKILL.md").read_text(encoding="utf-8"))
        command = normalize_markdown((ROOT / "pm-data-analytics/commands/write-query.md").read_text(encoding="utf-8"))
        for text in (skill, command):
            self.assertIn("template - schema not verified", text)
            self.assertIn("do not", text)
            self.assertIn("invent", text)

    def test_feedback_does_not_use_text_as_nps(self):
        skill = normalize_markdown((ROOT / "pm-market-research/skills/sentiment-analysis/SKILL.md").read_text(encoding="utf-8"))
        command = normalize_markdown((ROOT / "pm-market-research/commands/analyze-feedback.md").read_text(encoding="utf-8"))
        self.assertIn("do not create an nps proxy", skill)
        self.assertIn("do not derive an nps proxy", command)

    def test_cohort_maturity_and_causality_are_both_guarded(self):
        skill = normalize_markdown((ROOT / "pm-data-analytics/skills/cohort-analysis/SKILL.md").read_text(encoding="utf-8"))
        self.assertIn("not yet observable", skill)
        self.assertIn("causal", skill)
        self.assertIn("same-age", skill)

    def test_wave5a_scenario_catalog_exists(self):
        text = (ROOT / "reliability/WAVE5A_SCENARIOS.md").read_text(encoding="utf-8")
        for scenario in ["MR8", "MR9", "MR10", "A7", "A8", "A9", "A10", "D6", "D7", "D8", "D9", "X1"]:
            self.assertIn(scenario + ".", text)


if __name__ == "__main__":
    unittest.main()
