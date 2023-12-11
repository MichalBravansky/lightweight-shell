import unittest
from src.commands.echo import EchoCommand as Echo
from src.commands.argument import Argument

class TestEcho(unittest.TestCase):
    def test_echo_single_text(self):
        echo_text_arg = Argument(Argument.LIST, "echo_text", ["Hello, World!"])
        flag = Argument(Argument.FLAG, "exclude_trailing_newline", False)
        response = Echo().execute({"echo_text": echo_text_arg, "exclude_trailing_newline": flag})
        expected = "Hello, World!\n"
        self.assertEqual(response, expected)

    def test_echo_multiple_text(self):
        echo_text_arg = Argument(Argument.LIST, "echo_text", ["Hello", "World!"])
        flag = Argument(Argument.FLAG, "exclude_trailing_newline", False)
        response = Echo().execute({"echo_text": echo_text_arg, "exclude_trailing_newline": flag})
        expected = "Hello World!\n"
        self.assertEqual(response, expected)

    def test_echo_exclude_trailing_newline(self):
        echo_text_arg = Argument(Argument.LIST, "echo_text", ["Hello, World!"])
        flag = Argument(Argument.FLAG, "exclude_trailing_newline", True)
        response = Echo().execute({"echo_text": echo_text_arg, "exclude_trailing_newline": flag})
        expected = "Hello, World!"
        self.assertEqual(response, expected)

    def test_echo_no_text(self):
        echo_text_arg = Argument(Argument.LIST, "echo_text", [])
        flag = Argument(Argument.FLAG, "exclude_trailing_newline", False)
        response = Echo().execute({"echo_text": echo_text_arg, "exclude_trailing_newline": flag})
        expected = "\n"
        self.assertEqual(response, expected)

    def test_echo_no_text_exclude_newline(self):
        echo_text_arg = Argument(Argument.LIST, "echo_text", [])
        flag = Argument(Argument.FLAG, "exclude_trailing_newline", True)
        response = Echo().execute({"echo_text": echo_text_arg, "exclude_trailing_newline": flag})
        expected = ""
        self.assertEqual(response, expected)
