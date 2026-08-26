"""Wave 5B strategy/GTM semantic guard-regression tests.

These tests protect P0 runtime instructions against generic economics, forced
framework completion, unverified ICP/beachhead/channel assumptions, competitive
claim fabrication, and launch-readiness theatre. They do not grade arbitrary
LLM outputs end-to-end.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONTRACTS = {
    "pm-product-strategy/skills/business-model/SKILL.md": [
        "Do not invent customers",
        "LTV > 3x CAC",
        "DO NOTHING/current model",
        "Tool/search failure",
    ],
    "pm-product-strategy/skills/monetization-strategy/SKILL.md": [
        "Do not force 3-5 monetization strategies",
        "Do not invent WTP",
        "ECONOMICS UNKNOWN",
        "current model",
    ],
    "pm-product-strategy/skills/porters-five-forces/SKILL.md": [
        "defined market boundary",
        "UNKNOWN / MIXED",
        "Search by customer job",
        "Tool/search failure",
    ],
    "pm-go-to-market/skills/ideal-customer-profile/SKILL.md": [
        "survivorship bias",
        "Account ICP",
        "no-decision",
        "Anti-ICP",
    ],
    "pm-go-to-market/skills/beachhead-segment/SKILL.md": [
        "Do not force 3-5 candidate segments",
        "capture 60-70%",
        "NO BEACHHEAD READY",
        "successful PoC does not prove",
    ],
    "pm-go-to-market/skills/gtm-motions/SKILL.md": [
        "Do not force scoring of all seven motions",
        "Do not invent response rates",
        "pilot/demo lead is not equivalent",
        "UNKNOWN",
    ],
    "pm-product-strategy/commands/business-model.md": [
        "HYPOTHESIS MODE",
        "Agreement between frameworks is not independent corroborating evidence",
        "do not invent CAC",
        "NOT READY",
    ],
    "pm-product-strategy/commands/market-scan.md": [
        "Framework agreement is not independent corroboration",
        "Search/tool failure means coverage incomplete",
        "same-evidence repetition",
        "INSUFFICIENT EVIDENCE",
    ],
    "pm-product-strategy/commands/pricing.md": [
        "WTP UNKNOWN",
        "ECONOMICS UNKNOWN",
        "Never invent a price point",
        "TEST WTP",
    ],
    "pm-product-strategy/commands/strategy.md": [
        "credible alternative strategy",
        "strongest evidence against",
        "NO STRATEGY DECISION YET",
        "NOT YET ESTABLISHED",
    ],
    "pm-go-to-market/commands/battlecard.md": [
        "Never invent a competitor weakness",
        "PROOF GAP",
        "WIN/LOSS PATTERN UNKNOWN",
        "REFRESH EVIDENCE",
    ],
    "pm-go-to-market/commands/growth-strategy.md": [
        "Do not invent CAC",
        "CAC < 1/3 of LTV",
        "GROWTH ECONOMICS UNKNOWN",
        "FIX INSTRUMENTATION",
    ],
    "pm-go-to-market/commands/plan-launch.md": [
        "Do not invent TAM/SAM/SOM",
        "MARKET SIZE UNKNOWN",
        "BUYING JOURNEY UNKNOWN",
        "FIX P0 BLOCKERS",
        "deadline does not override",
    ],
}


def normalize_markdown(text: str) -> str:
    """Normalize formatting so Markdown syntax does not cause false failures."""
    text = text.lower()
    text = re.sub(r"[`*_>#]", "", text)
    text = re.sub(r"[“”‘’\"']", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


class TestWave5BGuards(unittest.TestCase):
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

    def test_generic_economics_rules_are_rejected_not_recommended(self):
        business = normalize_markdown((ROOT / "pm-product-strategy/skills/business-model/SKILL.md").read_text(encoding="utf-8"))
        growth = normalize_markdown((ROOT / "pm-go-to-market/commands/growth-strategy.md").read_text(encoding="utf-8"))
        self.assertIn(normalize_markdown("do not apply universal rules such as ltv > 3x cac"), business)
        self.assertIn(normalize_markdown("never use a universal rule such as cac < 1/3 of ltv"), growth)

    def test_pricing_without_wtp_fails_closed(self):
        pricing = normalize_markdown((ROOT / "pm-product-strategy/commands/pricing.md").read_text(encoding="utf-8"))
        self.assertIn("wtp unknown", pricing)
        self.assertIn("never invent a price point", pricing)
        self.assertIn("economics unknown", pricing)

    def test_framework_agreement_is_not_false_corroboration(self):
        business = normalize_markdown((ROOT / "pm-product-strategy/commands/business-model.md").read_text(encoding="utf-8"))
        scan = normalize_markdown((ROOT / "pm-product-strategy/commands/market-scan.md").read_text(encoding="utf-8"))
        self.assertIn("agreement between frameworks is not independent corroborating evidence", business)
        self.assertIn("framework agreement is not independent corroboration", scan)

    def test_icp_and_beachhead_do_not_use_survivorship_or_share_rules(self):
        icp = normalize_markdown((ROOT / "pm-go-to-market/skills/ideal-customer-profile/SKILL.md").read_text(encoding="utf-8"))
        beachhead = normalize_markdown((ROOT / "pm-go-to-market/skills/beachhead-segment/SKILL.md").read_text(encoding="utf-8"))
        self.assertIn("survivorship bias", icp)
        self.assertIn("no beachhead ready", beachhead)
        self.assertIn("remove arbitrary rules", beachhead)
        self.assertIn("capture 60-70%", beachhead)

    def test_battlecard_requires_evidence_or_proof_gap(self):
        text = normalize_markdown((ROOT / "pm-go-to-market/commands/battlecard.md").read_text(encoding="utf-8"))
        self.assertIn("never invent a competitor weakness", text)
        self.assertIn("proof gap", text)
        self.assertIn("win/loss pattern unknown", text)

    def test_launch_allows_block_and_no_go(self):
        text = normalize_markdown((ROOT / "pm-go-to-market/commands/plan-launch.md").read_text(encoding="utf-8"))
        for phrase in ["fix p0 blockers", "hold", "no-go", "market size unknown", "buying journey unknown"]:
            self.assertIn(phrase, text)

    def test_wave5b_scenario_catalog_exists(self):
        text = (ROOT / "reliability/WAVE5B_SCENARIOS.md").read_text(encoding="utf-8")
        for scenario in ["S6.", "S7.", "S8.", "S9.", "S10.", "S11.", "GTM6.", "GTM7.", "GTM8.", "GTM9.", "GTM10.", "GTM11.", "GTM12.", "GTM13.", "GTM14.", "GTM15."]:
            self.assertIn(scenario, text)


if __name__ == "__main__":
    unittest.main()
