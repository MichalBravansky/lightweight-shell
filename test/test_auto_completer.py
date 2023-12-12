import unittest
import os
import tempfile
from src.utils.auto_completer import AutoCompleter


class TestAutoCompleter(unittest.TestCase):
    def setUp(self):
        self.auto_completer = AutoCompleter()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_cwd = os.getcwd()
        os.chdir(self.temp_dir.name)

    def tearDown(self):
        os.chdir(self.old_cwd)
        self.temp_dir.cleanup()

    def test_completer(self):
        # Create a dummy file for testing
        with open("test_file.txt", "w") as f:
            f.write("")

        # Test that the completer method returns the correct file
        self.assertEqual(
            self.auto_completer.completer("test", 0), "test_file.txt"
        )

        # Test that the completer method returns None when there are no more matches

    def test_completer_no_match(self):
        # Test that the completer method returns None when there are no matches
        self.assertIsNone(self.auto_completer.completer("no_match", 0))
