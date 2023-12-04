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
        arg = Argument(Argument.LIST, "files", ["/Users/george/foo.txt"])
        response = Cat().execute({"files": arg})

        expected = "This is file 1.\nSecond line."
        self.assertEqual(response, expected)

    # def test_cat_multiple_files(self):
    #     response = Cat().execute([str(self.temp_path / "file1.txt"), str(self.temp_path / "file2.txt")])
    #     expected = "This is file 1.\nSecond line.File 2 content."
    #     self.assertEqual(response, expected)

    # def test_cat_nonexistent_file(self):
    #     with self.assertRaises(FileNotFoundError):
    #         Cat().execute(["nonexistent.txt"])

    # Additional tests for handling empty files, reading from stdin, etc.

if __name__ == "__main__":
    unittest.main()
