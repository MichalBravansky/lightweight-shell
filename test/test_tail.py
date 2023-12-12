import unittest
import tempfile
from pathlib import Path
from src.commands.tail import TailCommand as Tail
from src.commands.argument import Argument


class TestTail(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        with open(self.temp_path / "test_file.txt", "w") as f:
            f.write("\n".join(f"Line {i}" for i in range(1, 21)))

    def tearDown(self):
        self.test_dir.cleanup()

    def test_tail_default_lines(self):
        args = {
            "lines": Argument(Argument.FLAG_WITH_INTEGER, "lines", 10),
            "file": Argument(
                Argument.STRING, "file", str(self.temp_path / "test_file.txt")
            ),
        }
        expected = "\n".join(f"Line {i}" for i in range(11, 21))
        response = Tail().execute(args)
        self.assertEqual(response, expected)

    def test_tail_specific_lines(self):
        args = {
            "lines": Argument(Argument.FLAG_WITH_INTEGER, "lines", 5),
            "file": Argument(
                Argument.STRING, "file", str(self.temp_path / "test_file.txt")
            ),
        }
        expected = "\n".join(f"Line {i}" for i in range(16, 21))
        response = Tail().execute(args)
        self.assertEqual(response, expected)

    def test_tail_input_text(self):
        args = {
            "lines": Argument(Argument.FLAG_WITH_INTEGER, "lines", 3),
            "file": Argument(Argument.STRING, "file", None),
        }
        input_text = "\n".join(f"Line {i}" for i in range(1, 21))
        expected = "\n".join(f"Line {i}" for i in range(18, 21))
        response = Tail().execute(args, input_text)
        self.assertEqual(response, expected)

    def test_tail_invalid_line_count(self):
        args = {
            "lines": Argument(Argument.FLAG_WITH_INTEGER, "lines", -5),
            "file": Argument(
                Argument.STRING, "file", str(self.temp_path / "test_file.txt")
            ),
        }
        with self.assertRaises(ValueError):
            Tail().execute(args)

    def test_tail_invalid_file(self):
        args = {
            "lines": Argument(Argument.FLAG_WITH_INTEGER, "lines", 25),
            "file": Argument(Argument.STRING, "file", "invalid_file.txt"),
        }
        with self.assertRaises(FileNotFoundError):
            Tail().execute(args)

    def test_tail_no_file_no_input(self):
        args = {
            "lines": Argument(Argument.FLAG_WITH_INTEGER, "lines", 25),
            "file": Argument(Argument.STRING, "file", None),
        }
        with self.assertRaises(ValueError):
            Tail().execute(args)
