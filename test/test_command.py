import unittest
from unittest.mock import patch
from src.commands.command import Command

class TestCommand(unittest.TestCase):

    def setUp(self):
        self.command = Command('test', 'A test command')

    def test_execute_not_implemented(self):
        # Test that the execute method raises a NotImplementedError
        with self.assertRaises(NotImplementedError):
            self.command.execute([])

    def test_help(self):
        # Test the help method
        with patch('builtins.print') as mocked_print:
            self.command.help()
            mocked_print.assert_any_call('test: A test command')

if __name__ == "__main__":
    unittest.main()