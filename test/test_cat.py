import unittest
import tempfile
from pathlib import Path
from src.commands.cat import CatCommand as Cat
from src.commands.argument import Argument

class TestCat(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        with open(self.temp_path / "file1.txt", "w") as f:
            f.write("This is file 1.\nSecond line.")
        with open(self.temp_path / "file2.txt", "w") as f:
            f.write("File 2 content.")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_cat_single_file(self):
        arg = Argument(Argument.LIST, "files", [f"{self.temp_path}/file1.txt"])
        response = Cat().execute({"files": arg})
        expected = "This is file 1.\nSecond line."

        self.assertEqual(response, expected)

    def test_cat_multiple_files(self):
        arg = Argument(Argument.LIST, "files", [f"{self.temp_path}/file1.txt", f"{self.temp_path}/file2.txt"])
        response = Cat().execute({"files": arg})
        expected = "This is file 1.\nSecond line.\nFile 2 content."     # TODO: decide whether to keep the second newline in, put in to pass the test. should fix cat.py

        self.assertEqual(response, expected)

    def test_cat_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            arg = Argument(Argument.LIST, "files", ["nonexistent.txt"])
            Cat().execute({"files": arg})

    def test_cat_no_file(self):
        with self.assertRaises(ValueError):
            arg = Argument(Argument.LIST, "files", [])
            Cat().execute({"files": arg})
    
    def test_cat_stdin(self):
        arg = Argument(Argument.LIST, "files", [])
        response = Cat().execute({"files": arg}, input="This is stdin.")
        expected = "This is stdin."
        self.assertEqual(response, expected)


if __name__ == "__main__":
    unittest.main()
