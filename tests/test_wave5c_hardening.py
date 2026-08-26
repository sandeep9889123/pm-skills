"""Wave 5C semantic guard-regression tests.

Protects operational truth, evidence-calibrated red-teaming, meeting integrity,
test-oracle traceability, account expansion discipline, and shipping coverage.
These tests protect runtime contracts; they do not grade arbitrary LLM output.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONTRACTS = {
    "pm-execution/skills/strategy-red-team/SKILL.md": [
        "NEGATIVE EVIDENCE",
        "EVIDENCE GAP",
        "HOLDS UNDER CURRENT EVIDENCE",
        "PASS",
        "Do not force 3-5 risks",
    ],
    "pm-execution/commands/red-team-prd.md": [
        "do not default to",
        "NEGATIVE EVIDENCE",
        "EVIDENCE GAP",
        "zero material objections",
        "PASS",
    ],
    "pm-execution/skills/summarize-meeting/SKILL.md": [
        "OWNER UNKNOWN",
        "DUE DATE UNKNOWN",
        "Do not infer that silence equals agreement",
        "Verify every verbatim quote",
        "PARTIAL TRANSCRIPT",
    ],
    "pm-execution/commands/meeting-notes.md": [
        "OWNER UNKNOWN",
        "DUE DATE UNKNOWN",
        "Silence is not approval",
        "Suggested is not Assigned",
        "coverage",
    ],
    "pm-execution/skills/test-scenarios/SKILL.md": [
        "Never invent expected behavior",
        "SPEC GAP",
        "Oracle Source",
        "BLOCKED BY SPEC GAP",
        "NOT ASSESSED",
    ],
    "pm-execution/commands/test-scenarios.md": [
        "never invent expected behavior",
        "SPEC GAP",
        "Oracle Source",
        "COVERAGE INCOMPLETE",
        "BLOCKED BY SPEC GAPS",
    ],
    "pm-enterprise-transformation/skills/account-expansion-play/SKILL.md": [
        "Positive relationship sentiment",
        "commercial commitment",
        "STABILIZE FIRST",
        "account concentration",
        "DO NOT PURSUE",
    ],
    "pm-ai-shipping/commands/security-audit-static.md": [
        "COMPLETE FOR DECLARED SCOPE",
        "COVERAGE INCOMPLETE",
        "NO SURVIVING FINDINGS IN INSPECTED SCOPE",
        "does not mean",
        "tool/subagent",
    ],
    "pm-ai-shipping/commands/performance-audit-static.md": [
        "COMPLETE FOR DECLARED SCOPE",
        "COVERAGE INCOMPLETE",
        "NO MATERIAL STATIC FINDINGS IN INSPECTED SCOPE",
        "not proof that the system will scale",
        "STATIC RISK",
    ],
    "pm-ai-shipping/commands/ship-check.md": [
        "COMPLETE FOR DECLARED SCOPE",
        "COVERAGE INCOMPLETE",
        "READY FOR HUMAN REVIEW",
        "PROPOSED TEST",
        "PINNED BY EXECUTED TEST",
        "does not mean guaranteed safe",
    ],
}


def normalize_markdown(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[`*_>#]", "", text)
    text = re.sub(r"[“”‘’\"']", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


class TestWave5CGuards(unittest.TestCase):
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

    def test_red_team_distinguishes_gap_from_negative_evidence(self):
        skill = normalize_markdown((ROOT / "pm-execution/skills/strategy-red-team/SKILL.md").read_text(encoding="utf-8"))
        command = normalize_markdown((ROOT / "pm-execution/commands/red-team-prd.md").read_text(encoding="utf-8"))
        for text in (skill, command):
            self.assertIn("negative evidence", text)
            self.assertIn("evidence gap", text)
            self.assertIn("pass", text)
        self.assertNotIn("default the risk is real", command)

    def test_meeting_does_not_invent_owner_date_or_consensus(self):
        skill = normalize_markdown((ROOT / "pm-execution/skills/summarize-meeting/SKILL.md").read_text(encoding="utf-8"))
        self.assertIn("owner unknown", skill)
        self.assertIn("due date unknown", skill)
        self.assertIn("silence equals agreement", skill)
        self.assertIn("verify every verbatim quote", skill)

    def test_test_oracles_require_source_and_spec_gaps(self):
        skill = normalize_markdown((ROOT / "pm-execution/skills/test-scenarios/SKILL.md").read_text(encoding="utf-8"))
        command = normalize_markdown((ROOT / "pm-execution/commands/test-scenarios.md").read_text(encoding="utf-8"))
        for text in (skill, command):
            self.assertIn("spec gap", text)
            self.assertIn("oracle source", text)
        self.assertIn("never invent expected behavior", skill)
        self.assertIn("blocked by spec gap", skill)

    def test_account_expansion_has_stabilization_gate(self):
        text = normalize_markdown((ROOT / "pm-enterprise-transformation/skills/account-expansion-play/SKILL.md").read_text(encoding="utf-8"))
        self.assertIn("positive relationship sentiment", text)
        self.assertIn("not commercial commitment", text)
        self.assertIn("stabilize first", text)
        self.assertIn("account concentration", text)

    def test_security_zero_findings_is_not_security_claim(self):
        text = normalize_markdown((ROOT / "pm-ai-shipping/commands/security-audit-static.md").read_text(encoding="utf-8"))
        self.assertIn("no surviving findings in inspected scope", text)
        self.assertIn("does not mean secure", text)
        self.assertIn("coverage incomplete", text)

    def test_performance_static_review_is_not_scalability_proof(self):
        text = normalize_markdown((ROOT / "pm-ai-shipping/commands/performance-audit-static.md").read_text(encoding="utf-8"))
        self.assertIn("not proof that the system will scale", text)
        self.assertIn("no material static findings in inspected scope", text)
        self.assertIn("runtime validation", text)

    def test_ship_check_preserves_partial_coverage_and_test_state(self):
        text = normalize_markdown((ROOT / "pm-ai-shipping/commands/ship-check.md").read_text(encoding="utf-8"))
        self.assertIn("coverage incomplete", text)
        self.assertIn("proposed test", text)
        self.assertIn("pinned by executed test", text)
        self.assertIn("ready for human review", text)
        self.assertIn("does not mean guaranteed safe", text)

    def test_wave5c_scenario_catalog_exists(self):
        text = (ROOT / "reliability/WAVE5C_SCENARIOS.md").read_text(encoding="utf-8")
        ids = [
            "E6.", "E7.", "E8.", "E9.", "E10.", "E11.", "E12.", "E13.", "E14.",
            "ET11.", "ET12.", "AI6.", "AI7.", "AI8.", "AI9.", "AI10.",
        ]
        for scenario_id in ids:
            self.assertIn(scenario_id, text)


if __name__ == "__main__":
    unittest.main()
