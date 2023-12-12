import unittest
from src.commands.commandFactory import CommandFactory
from utils.exceptions import UnknownCommandError


class TestCommandFactory(unittest.TestCase):
    def setUp(self):
        self.command_factory = CommandFactory()

    def test_create_not_found(self):
        # Test that the create method raises a ValueError when the command is not found
        with self.assertRaises(UnknownCommandError):
            self.command_factory.execute_command('no_match', [])
