import unittest
import tempfile
import os
from pathlib import Path
from src.commands.ls import LsCommand as Ls
from src.commands.argument import Argument


class TestLs(unittest.TestCase):
    def setUp(self):
        self.original_cwd = os.getcwd()
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        os.makedirs(self.temp_path / "subdir")
        with open(self.temp_path / "file1.txt", "w") as f:
            f.write("Test file 1")
        with open(self.temp_path / "file2.txt", "w") as f:
            f.write("Test file 2")
        os.chdir(self.temp_path)

    def tearDown(self):
        os.chdir(self.original_cwd)  # Restore original current working directory
        self.test_dir.cleanup()

    def test_ls_specified_directory(self):
        dir_arg = Argument(Argument.STRING, "directory", str(self.temp_path))
        response = Ls().execute({"directory": dir_arg})
        expected = "\n".join(os.listdir(self.temp_path))
        self.assertEqual(response, expected)

    def test_ls_default_directory(self):
        dir_arg = Argument(Argument.STRING, "directory", None)
        response = Ls().execute({"directory": dir_arg})
        expected = "\n".join(["subdir", "file2.txt", "file1.txt"])
        self.assertEqual(response, expected)

    def test_ls_empty_directory(self):
        empty_dir = tempfile.TemporaryDirectory()
        empty_path = Path(empty_dir.name)
        dir_arg = Argument(Argument.STRING, "directory", str(empty_path))
        response = Ls().execute({"directory": dir_arg})
        expected = ""
        self.assertEqual(response, expected)
        empty_dir.cleanup()

