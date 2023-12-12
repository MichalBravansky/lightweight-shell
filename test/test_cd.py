import unittest
import os
from src.commands.cd import CdCommand as Cd
from src.commands.argument import Argument


class TestCd(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.getcwd()

    def tearDown(self):
        os.chdir(self.current_directory)

    def test_cd_valid_directory(self):
        args = {"cd_path": Argument(Argument.STRING, "cd_path", "/tmp")}
        expected_directory = "/tmp"
        Cd().execute(args)
        current_directory = os.getcwd()
        self.assertEqual(current_directory, expected_directory)

    def test_cd_invalid_directory(self):
        args = {
            "cd_path": Argument(Argument.STRING, "cd_path", "/nonexistent")
        }
        with self.assertRaises(NotADirectoryError):
            Cd().execute(args)

    def test_cd_default_path(self):
        args = {"cd_path": Argument(Argument.STRING, "cd_path", "/")}
        expected_directory = "/"
        Cd().execute(args)
        current_directory = os.getcwd()
        self.assertEqual(current_directory, expected_directory)
