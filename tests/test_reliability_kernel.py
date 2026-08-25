"""Repository-wide PM Reliability Kernel invariants.

The goal is not to prove model correctness. These tests make reliability debt
visible: every skill/workflow must be classified, core kernel contracts must be
parseable, and evidence-lineage rules may not silently permit claim promotion.
"""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KERNEL = ROOT / "reliability" / "kernel"
RISK_MAP = KERNEL / "risk_tiers.json"
CONTEXT_SCHEMA = KERNEL / "context_frame.schema.json"
CLAIM_SCHEMA = KERNEL / "claim_lineage.schema.json"
SCENARIO_MATRIX = ROOT / "reliability" / "scenario_matrix.json"
TIERS = ("P0", "P1", "P2")


def plugin_dirs():
    return sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and p.name.startswith("pm-") and (p / "skills").is_dir()
    )


def disk_inventory(kind):
    inventory = {}
    for plugin in plugin_dirs():
        if kind == "skills":
            names = sorted(p.parent.name for p in (plugin / "skills").glob("*/SKILL.md"))
        elif kind == "workflows":
            command_dir = plugin / "commands"
            names = sorted(p.stem for p in command_dir.glob("*.md")) if command_dir.is_dir() else []
        else:
            raise ValueError(kind)
        inventory[plugin.name] = names
    return inventory


class TestRiskClassification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.risk = json.loads(RISK_MAP.read_text(encoding="utf-8"))

    def test_inventory_header_matches_disk(self):
        skills = disk_inventory("skills")
        workflows = disk_inventory("workflows")
        self.assertEqual(self.risk["inventory"]["plugins"], len(plugin_dirs()))
        self.assertEqual(self.risk["inventory"]["skills"], sum(map(len, skills.values())))
        self.assertEqual(self.risk["inventory"]["workflows"], sum(map(len, workflows.values())))

    def test_every_skill_and_workflow_is_classified_once(self):
        for kind in ("skills", "workflows"):
            disk = disk_inventory(kind)
            mapped = self.risk[kind]
            self.assertEqual(set(mapped), set(disk), f"{kind}: plugin set drift")

            for plugin, actual in disk.items():
                tier_map = mapped[plugin]
                self.assertEqual(set(tier_map), set(TIERS), f"{kind}/{plugin}: invalid tiers")
                flattened = [name for tier in TIERS for name in tier_map[tier]]
                self.assertEqual(
                    len(flattened), len(set(flattened)),
                    f"{kind}/{plugin}: artifact classified in more than one tier",
                )
                self.assertEqual(
                    sorted(flattened), actual,
                    f"{kind}/{plugin}: missing or stale reliability classification",
                )

    def test_tier_policy_has_required_controls(self):
        policy = self.risk["tier_policy"]
        self.assertEqual(set(policy), set(TIERS))
        for tier in TIERS:
            self.assertTrue(policy[tier]["required_controls"], f"{tier} has no controls")
        p0 = set(policy["P0"]["required_controls"])
        for required in {
            "context_resolution",
            "evidence_states",
            "source_precedence",
            "contradiction_pass",
            "tool_failure_fail_closed",
            "cross_skill_lineage",
            "decision_gate",
            "behavioral_evaluation_plan",
        }:
            self.assertIn(required, p0)

    def test_current_tier_distribution_is_intentional(self):
        skill_counts = {
            tier: sum(len(v[tier]) for v in self.risk["skills"].values()) for tier in TIERS
        }
        workflow_counts = {
            tier: sum(len(v[tier]) for v in self.risk["workflows"].values()) for tier in TIERS
        }
        self.assertEqual(skill_counts, {"P0": 65, "P1": 28, "P2": 3})
        self.assertEqual(workflow_counts, {"P0": 45, "P1": 9, "P2": 1})


class TestKernelSchemas(unittest.TestCase):
    def test_schemas_are_parseable_json(self):
        for path in (CONTEXT_SCHEMA, CLAIM_SCHEMA):
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["$schema"], "https://json-schema.org/draft/2020-12/schema")
            self.assertEqual(data["type"], "object")

    def test_context_schema_captures_decision_sensitive_context(self):
        schema = json.loads(CONTEXT_SCHEMA.read_text(encoding="utf-8"))
        props = schema["properties"]
        for field in {
            "decision",
            "audience_or_actor",
            "geography_or_market",
            "stage",
            "constraints",
            "evidence",
            "material_unknowns",
            "working_assumptions",
        }:
            self.assertIn(field, props)

    def test_claim_schema_has_evidence_states_and_no_silent_promotion(self):
        schema = json.loads(CLAIM_SCHEMA.read_text(encoding="utf-8"))
        states = set(schema["properties"]["state"]["enum"])
        self.assertTrue({
            "FACT", "INFERENCE", "ASSUMPTION", "ESTIMATE", "UNKNOWN",
            "STALE", "TARGET", "PROPOSAL", "DECISION_THRESHOLD",
        }.issubset(states))
        promotion = schema["properties"]["downstream_policy"]["properties"]
        self.assertEqual(promotion["may_promote_without_new_evidence"].get("const"), False)

    def test_estimates_require_method_contract(self):
        schema = json.loads(CLAIM_SCHEMA.read_text(encoding="utf-8"))
        serialized = json.dumps(schema)
        self.assertIn('"ESTIMATE"', serialized)
        self.assertIn('"estimate_method"', serialized)


class TestKernelScenarioCompatibility(unittest.TestCase):
    def test_risk_map_and_scenario_matrix_cover_same_plugins(self):
        risk = json.loads(RISK_MAP.read_text(encoding="utf-8"))
        matrix = json.loads(SCENARIO_MATRIX.read_text(encoding="utf-8"))
        self.assertEqual(set(risk["skills"]), set(matrix["plugin_scenarios"]))

    def test_p0_has_nontrivial_deep_guard_coverage(self):
        """Wave 4 classifies all P0 work; Wave 5 expands deep contracts progressively."""
        risk = json.loads(RISK_MAP.read_text(encoding="utf-8"))
        matrix = json.loads(SCENARIO_MATRIX.read_text(encoding="utf-8"))
        contracts = matrix.get("high_risk_contracts", {})
        p0_paths = set()
        for plugin, tiers in risk["skills"].items():
            for name in tiers["P0"]:
                p0_paths.add(f"{plugin}/skills/{name}/SKILL.md")
        for plugin, tiers in risk["workflows"].items():
            for name in tiers["P0"]:
                p0_paths.add(f"{plugin}/commands/{name}.md")

        guarded = p0_paths.intersection(contracts)
        self.assertGreaterEqual(
            len(guarded), 30,
            "Deep P0 guard coverage regressed materially; expand contracts instead of weakening the gate",
        )


if __name__ == "__main__":
    unittest.main()
