"""Offline structural checks for the standalone prototype skill."""
import unittest,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
PLUGIN=ROOT/"pm-prototype-os"
CORE=PLUGIN/"skills"/"ai-product-prototype-os"
class TestPrototypeOSContracts(unittest.TestCase):
 def test_skill_and_command_counts(self):
  self.assertEqual(len([x for x in (PLUGIN/"skills").iterdir() if x.is_dir()]),6)
  self.assertEqual(len(list((PLUGIN/"commands").glob("*.md"))),5)
 def test_skill_self_contained(self):
  for name in ("governance","archetypes","references","workflows","templates","project-starter","provenance"):
   self.assertTrue((CORE/name).is_dir(),name)
  self.assertEqual(len(list((CORE/"archetypes").glob("*.md"))),9)
  t=(CORE/"SKILL.md").read_text(encoding="utf8")
  for phrase in ("Ask 5 to 10","AWAITING_APPROVAL","₹0 incremental spending","Never assert a verification happened without evidence"):
   self.assertIn(phrase,t)
 def test_zero_default_authorization(self):
  s=json.loads((CORE/"project-starter"/"PROJECT_STATE.json").read_text(encoding="utf8"))
  self.assertEqual(s["incremental_cost_limit_inr"],0)
  self.assertIsNone(s["authorized_next_action"])
 def test_question_and_approval_docs(self):
  self.assertIn("5–10",(CORE/"governance"/"question-protocol.md").read_text(encoding="utf8"))
  self.assertIn("human",(CORE/"governance"/"approval-state-machine.md").read_text(encoding="utf8"))
 def test_evaluation_definitions_only(self):
  e=json.loads((ROOT/"evaluation"/"prototype_os"/"scenarios.json").read_text(encoding="utf8"))
  r=json.loads((ROOT/"evaluation"/"prototype_os"/"rag_cases.json").read_text(encoding="utf8"))
  self.assertEqual(len(e["cases"]),51)
  self.assertEqual(len({x["id"] for x in e["cases"]}),51)
  self.assertEqual(len(r["cases"]),15)
  self.assertTrue(all(x["status"]=="NOT_RUN" for x in e["cases"]+r["cases"]))
if __name__=="__main__":unittest.main()
