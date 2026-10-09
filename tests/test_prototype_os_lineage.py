"""Evidence lineage compatibility with the existing PM Skills kernel."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parent.parent
CORE=ROOT/"pm-prototype-os"/"skills"/"ai-product-prototype-os"
class TestPrototypeLineage(unittest.TestCase):
 def test_kernel_exists(self):
  self.assertTrue((ROOT/"reliability"/"kernel"/"HANDOFF_PROTOCOL.md").is_file())
 def test_claim_status(self):
  t=(CORE/"governance"/"evidence-and-recommendations.md").read_text(encoding="utf8")
  for s in ("FACT","INFERENCE","ASSUMPTION","UNKNOWN","STALE","claim IDs"):
   self.assertIn(s,t)
 def test_fallback_documents(self):
  self.assertTrue((CORE/"templates"/"prd.md").is_file())
  self.assertTrue((CORE/"references"/"product-management.md").is_file())
if __name__=="__main__":unittest.main()
