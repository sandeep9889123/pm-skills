"""Provider adapter parity and stand-alone structure checks; no network."""
from pathlib import Path
import unittest,json
ROOT=Path(__file__).resolve().parent.parent
P=ROOT/"pm-prototype-os"
class TestPrototypePackaging(unittest.TestCase):
 def test_manifests(self):
  a=json.loads((P/".claude-plugin"/"plugin.json").read_text())
  b=json.loads((P/".codex-plugin"/"plugin.json").read_text())
  self.assertEqual(a["name"],b["name"])
  self.assertEqual(a["version"],b["version"])
  self.assertEqual(b["skills"],"./skills/")
 def test_adapters(self):
  for x in ("adapters/claude/README.md","adapters/chatgpt/PROJECT_INSTRUCTIONS.md","adapters/codex/README.md","adapters/portable-direct-chat/START_HERE.md"):
   self.assertTrue((P/x).is_file(),x)
 def test_main_skill_is_standalone(self):
  c=P/"skills"/"ai-product-prototype-os"
  self.assertTrue((c/"SKILL.md").exists())
  self.assertTrue((c/"references"/"product-management.md").exists())
  self.assertTrue((c/"governance"/"approval-state-machine.md").exists())
 def test_no_bundled_executables(self):
  for x in P.rglob("*"):
   if x.is_file():self.assertIn(x.suffix,(".md",".json"),str(x))
if __name__=="__main__":unittest.main()
