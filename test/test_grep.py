import unittest
import tempfile
from pathlib import Path
from src.commands.grep import GrepCommand as Grep
from src.commands.argument import Argument


class TestGrep(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        with open(self.temp_path / "file1.txt", "w") as f:
            f.write("Hello World\nTest Line 1\nAnother Test Line")
        with open(self.temp_path / "file2.txt", "w") as f:
            f.write("Test Line 2\nSample Text\nMore Test Lines")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_grep_single_file(self):
        pattern_arg = Argument(Argument.STRING, "pattern", "Test")
        file_arg = Argument(
            Argument.LIST, "files", [str(self.temp_path / "file1.txt")]
        )
        response = Grep().execute({"pattern": pattern_arg, "files": file_arg})
        expected = "Test Line 1\nAnother Test Line"
        self.assertEqual(response, expected)

    def test_grep_multiple_files(self):
        pattern_arg = Argument(Argument.STRING, "pattern", "Test")
        files_arg = Argument(
            Argument.LIST,
            "files",
            [
                str(self.temp_path / "file1.txt"),
                str(self.temp_path / "file2.txt"),
            ],
        )
        response = Grep().execute({"pattern": pattern_arg, "files": files_arg})
        expected = (
            f"{self.temp_path}/file1.txt:Test Line 1\n"
            f"{self.temp_path}/file1.txt:Another Test Line\n"
            f"{self.temp_path}/file2.txt:Test Line 2\n"
            f"{self.temp_path}/file2.txt:More Test Lines"
        )
        self.assertEqual(response, expected)

    def test_grep_no_file_with_input(self):
        pattern_arg = Argument(Argument.STRING, "pattern", "Sample")
        input_text = "Sample Line 1\nAnother Line\nSample Line 2"
        response = Grep().execute(
            {
                "pattern": pattern_arg,
                "files": Argument(Argument.LIST, "files", []),
            },
            input=input_text,
        )
        expected = "Sample Line 1\nSample Line 2"
        self.assertEqual(response, expected)

    def test_grep_nonexistent_file(self):
        pattern_arg = Argument(Argument.STRING, "pattern", "Test")
        files_arg = Argument(Argument.LIST, "files", ["nonexistent.txt"])
        with self.assertRaises(FileNotFoundError):
            Grep().execute({"pattern": pattern_arg, "files": files_arg})

    def test_grep_no_file_no_input(self):
        pattern_arg = Argument(Argument.STRING, "pattern", "Test")
        with self.assertRaises(ValueError):
            Grep().execute({
                "pattern": pattern_arg,
                "files": Argument(Argument.LIST, "files", []),
            })
