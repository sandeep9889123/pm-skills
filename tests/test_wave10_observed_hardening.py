"""Regression contracts derived from the first zero-cost manual smoke baseline."""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class TestPrivacyPolicyObservedFailure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (ROOT / "pm-toolkit/skills/privacy-policy/SKILL.md").read_text(
            encoding="utf-8"
        )

    def test_unknown_practices_fail_closed(self):
        self.assertIn("DRAFT: NOT READY TO PUBLISH", self.text)
        self.assertIn("[UNKNOWN: VERIFY BEFORE PUBLICATION: owner/evidence needed]", self.text)
        self.assertIn("Legal review does not verify how the product is configured", self.text)

    def test_proposed_default_loophole_is_closed(self):
        self.assertIn("copy-forward risk", self.text)
        self.assertIn("labels such as", self.text)
        self.assertIn('"recommended," "proposed," or "default."', self.text)
        self.assertIn("keep any product or policy design proposal outside the policy", self.text)
        self.assertIn("exact retention periods", self.text)
        self.assertIn("sale/no-sale statements", self.text)

    def test_ready_to_publish_requires_implementation_and_legal_proof(self):
        self.assertIn("all material implementation facts are verified", self.text)
        self.assertIn("the public wording matches production behavior", self.text)
        self.assertIn("qualified privacy counsel", self.text)


if __name__ == "__main__":
    unittest.main()
