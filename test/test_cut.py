import unittest
from unittest.mock import patch
import tempfile
from pathlib import Path
from src.commands.cut import CutCommand as Cut
from src.commands.argument import Argument

class TestCut(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        with open(self.temp_path / "test_file.txt", "w") as f:
            f.write("Line1\nLine2\nLine3")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_cut_specific_bytes_from_file(self):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "1-4")
        file_arg = Argument(Argument.STRING, "file", f"{self.temp_path}/test_file.txt")
        response = Cut().execute({"bytes": byte_arg, "file": file_arg})
        expected = "Line\nLine\nLine\n"

        self.assertEqual(response, expected)

    def test_cut_specific_bytes_from_input(self):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "1-4")
        input_str = "TestLine1\nTestLine2\nTestLine3"
        response = Cut().execute({"bytes": byte_arg, "file": Argument(Argument.STRING, "file", None)}, input=input_str)
        expected = "Test\nTest\nTest\n"

        self.assertEqual(response, expected)

    def test_cut_with_invalid_byte_range(self):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "5-2")
        with self.assertRaises(ValueError):
            Cut().execute({"bytes": byte_arg, "file": Argument(Argument.STRING, "file", None)})

    def test_cut_without_byte_range(self):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "")
        with self.assertRaises(ValueError):
            Cut().execute({"bytes": byte_arg, "file": Argument(Argument.STRING, "file", None)})

    def test_cut_nonexistent_file(self):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "1-4")
        file_arg = Argument(Argument.STRING, "file", "nonexistent.txt")
        with self.assertRaises(FileNotFoundError):
            Cut().execute({"bytes": byte_arg, "file": file_arg})

    def test_cut_single_byte_range(self):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "3")
        file_arg = Argument(Argument.STRING, "file", f"{self.temp_path}/test_file.txt")
        response = Cut().execute({"bytes": byte_arg, "file": file_arg})
        expected = "n\nn\nn\n"  # Assuming the file has "Line1\nLine2\nLine3"

        self.assertEqual(response, expected)
    
    def test_cut_start_is_none(self):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "-4")
        file_arg = Argument(Argument.STRING, "file", f"{self.temp_path}/test_file.txt")
        response = Cut().execute({"bytes": byte_arg, "file": file_arg})
        expected = "Line\nLine\nLine\n"

        self.assertEqual(response, expected)

    def test_cut_entire_line(self):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "-")
        file_arg = Argument(Argument.STRING, "file", f"{self.temp_path}/test_file.txt")
        response = Cut().execute({"bytes": byte_arg, "file": file_arg})
        expected = "Line1\nLine2\nLine3\n"

        self.assertEqual(response, expected)

    def test_cut_invalid_byte_range(self):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "a")
        with self.assertRaises(ValueError):
            Cut().execute({"bytes": byte_arg, "file": Argument(Argument.STRING, "file", f"{self.temp_path}/test_file.txt")})

    @patch("builtins.open", side_effect=IOError("mocked error"))
    def test_cut_file_io_error(self, mock_open):
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", "1-4")
        file_arg = Argument(Argument.STRING, "file", "test_file.txt")
        with self.assertRaises(IOError):
            Cut().execute({"bytes": byte_arg, "file": file_arg})
