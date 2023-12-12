import unittest
from unittest.mock import patch
from src.commands.command import Command


class FakeCommand(Command):
    def __init__(self):
        super().__init__('test', 'A test command')

    def execute(self, args, input=None):
        return 'FakeCommand'


class TestCommand(unittest.TestCase):
    def setUp(self):
        self.command = FakeCommand()

    def test_help(self):
        # Test the help method
        with patch('builtins.print') as mocked_print:
            self.command.help()
            mocked_print.assert_any_call('test: A test command')

    def test_execute(self):
        args = {}
        self.assertEqual(self.command.execute(args), 'FakeCommand')
