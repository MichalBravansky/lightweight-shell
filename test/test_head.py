import unittest
import tempfile
import os
from pathlib import Path
from src.commands.head import HeadCommand as Head
from src.commands.argument import Argument

class TestHead(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        with open(self.temp_path / "test_file.txt", "w") as f:
            f.write("\n".join(f"Line {i}" for i in range(1, 21)))

    def tearDown(self):
        self.test_dir.cleanup()

    def test_head_specific_lines_from_file(self):
        lines_arg = Argument(Argument.FLAG_WITH_INTEGER, "lines", 5)
        file_arg = Argument(Argument.STRING, "file", str(self.temp_path / "test_file.txt"))
        response = Head().execute({"lines": lines_arg, "file": file_arg})
        expected = "\n".join(f"Line {i}" for i in range(1, 6))
        self.assertEqual(response, expected)

    def test_head_default_lines_from_file(self):
        lines_arg = Argument(Argument.FLAG_WITH_INTEGER, "lines", 10)  # Default value
        file_arg = Argument(Argument.STRING, "file", str(self.temp_path / "test_file.txt"))
        response = Head().execute({"lines": lines_arg, "file": file_arg})
        expected = "\n".join(f"Line {i}" for i in range(1, 11))
        self.assertEqual(response, expected)

    def test_head_nonexistent_file(self):
        lines_arg = Argument(Argument.FLAG_WITH_INTEGER, "lines", 5)
        file_arg = Argument(Argument.STRING, "file", str(self.temp_path / "nonexistent.txt"))
        with self.assertRaises(FileNotFoundError):
            Head().execute({"lines": lines_arg, "file": file_arg})

    def test_head_with_input_text(self):
        lines_arg = Argument(Argument.FLAG_WITH_INTEGER, "lines", 3)
        input_text = "\n".join(f"Input Line {i}" for i in range(1, 6))
        response = Head().execute({"lines": lines_arg, "file": Argument(Argument.STRING, "file", None)}, input=input_text)
        expected = "Input Line 1\nInput Line 2\nInput Line 3"
        self.assertEqual(response, expected)

    def test_head_negative_line_count(self):
        lines_arg = Argument(Argument.FLAG_WITH_INTEGER, "lines", -5)
        file_arg = Argument(Argument.STRING, "file", str(self.temp_path / "test_file.txt"))
        with self.assertRaises(ValueError):
            Head().execute({"lines": lines_arg, "file": file_arg})

    def test_head_no_file_no_input(self):
        lines_arg = Argument(Argument.FLAG_WITH_INTEGER, "lines", 5)
        with self.assertRaises(ValueError):
            Head().execute({"lines": lines_arg, "file": Argument(Argument.STRING, "file", None)})

