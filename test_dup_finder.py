import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest, tempfile
from pathlib import Path
from dup_finder import find_duplicates
class T(unittest.TestCase):
    def test_finds_dupes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/"a.txt").write_text("same"); (p/"b.txt").write_text("same"); (p/"c.txt").write_text("diff")
            groups = find_duplicates(str(p))
            self.assertEqual(len(groups), 1)
            self.assertEqual(len(list(groups.values())[0]), 2)
if __name__ == "__main__": unittest.main()
