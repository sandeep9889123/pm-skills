"""Regression contracts for pm-prospect-discovery.

These tests protect the model-agnostic master prompt, discovery fail-closed behavior,
question discipline, anti-confirmation red-team, and proposal-readiness gates.
They do not prove end-to-end LLM output quality.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "pm-prospect-discovery"


class TestProspectDiscoveryStructure(unittest.TestCase):
    def test_model_agnostic_prompt_exists(self):
        prompt = PLUGIN / "prompts" / "prospect-discovery-master.md"
        self.assertTrue(prompt.is_file())
        text = prompt.read_text(encoding="utf-8")
        self.assertIn("any capable LLM", text)
        self.assertIn("coverage incomplete / UNKNOWN", text)
        self.assertIn("REFRAME USE CASE", text)

    def test_core_templates_exist(self):
        for rel in [
            "templates/discovery-brief.md",
            "templates/session-summary.md",
            "templates/proposal-handoff.md",
            "templates/discovery-session.html",
        ]:
            self.assertTrue((PLUGIN / rel).is_file(), rel)


class TestFailClosedContracts(unittest.TestCase):
    def _read(self, rel):
        return (PLUGIN / rel).read_text(encoding="utf-8").lower()

    def test_orchestrator_can_reject_preferred_use_case(self):
        text = self._read("skills/prospect-discovery-orchestrator/SKILL.md")
        self.assertIn("wrong use case", text)
        self.assertIn("second discovery required", text)
        self.assertIn("coverage incomplete / unknown", text)
        self.assertIn("strongest disconfirming evidence", text)

    def test_question_engine_prevents_questionnaire_bloat(self):
        text = self._read("skills/discovery-question-engine/SKILL.md")
        self.assertIn("minimum sufficient evidence", text)
        self.assertIn("must ask", text)
        self.assertIn("conditional logic", text)
        self.assertIn("material decision", text)
        self.assertIn("disconfirming questions", text)

    def test_red_team_checks_non_software_alternatives(self):
        text = self._read("skills/discovery-red-team/SKILL.md")
        self.assertIn("do nothing", text)
        self.assertIn("current system", text)
        self.assertIn("alternative root cause", text)
        self.assertIn("willingness", text)

    def test_readiness_has_hard_gate_precedence(self):
        text = self._read("skills/proposal-readiness/SKILL.md")
        self.assertIn("hard blockers", text)
        self.assertIn("unresolved p0", text)
        self.assertIn("high score cannot override a hard gate", text)
        self.assertIn("ready for estimation", text)


if __name__ == "__main__":
    unittest.main()
