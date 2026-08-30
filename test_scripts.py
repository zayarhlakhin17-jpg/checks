import py_compile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class TestPracticeScripts(unittest.TestCase):

    def test_disk_usage_compiles(self):
        py_compile.compile(
            ROOT / "disk_usage.py",
            doraise=True
        )

    def test_free_memory_compiles(self):
        py_compile.compile(
            ROOT / "free_memory.py",
            doraise=True
        )


if __name__ == "__main__":
    unittest.main()
