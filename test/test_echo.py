import unittest
from src.commands.echo import EchoCommand as Echo
from src.commands.argument import Argument


class TestEcho(unittest.TestCase):
    def test_echo_single_text(self):
        echo_text_arg = Argument(Argument.LIST, "echo_text", ["Hello, World!"])
        response = Echo().execute({"echo_text": echo_text_arg})
        expected = "Hello, World!"
        self.assertEqual(response, expected)

    def test_echo_multiple_text(self):
        echo_text_arg = Argument(Argument.LIST, "echo_text", ["Hello", "World!"])
        response = Echo().execute({"echo_text": echo_text_arg})
        expected = "Hello World!"
        self.assertEqual(response, expected)

    def test_echo_no_text(self):
        echo_text_arg = Argument(Argument.LIST, "echo_text", [])
        response = Echo().execute({"echo_text": echo_text_arg})
        expected = ""
        self.assertEqual(response, expected)
