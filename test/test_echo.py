import unittest
from src.commands.echo import EchoCommand as Echo
from src.commands.argument import Argument
from hypothesis import given
from hypothesis.strategies import text, characters

def valid_string() -> str:
    return text(
        characters(max_codepoint=200, blacklist_categories=("Cc", "Cs")),
        min_size=1
    ).map(lambda s: s.strip()).filter(
        lambda s: len(s) > 0 and all(char.isalpha() or char.isspace() for char in s)
    )

class TestEcho(unittest.TestCase):

    def test_echo_single_text(self):
        echo_text_arg = Argument(Argument.LIST, 'echo_text', ['Hello, World!'])
        response = Echo().execute({'echo_text': echo_text_arg})
        expected = 'Hello, World!'
        self.assertEqual(response, expected)

    def test_echo_multiple_text(self):
        echo_text_arg = Argument(
            Argument.LIST, 'echo_text', ['Hello', 'World!']
        )
        response = Echo().execute({'echo_text': echo_text_arg})
        expected = 'Hello World!'
        self.assertEqual(response, expected)

    def test_echo_no_text(self):
        echo_text_arg = Argument(Argument.LIST, 'echo_text', [])
        response = Echo().execute({'echo_text': echo_text_arg})
        expected = ''
        self.assertEqual(response, expected)

    @given(valid_string())
    def test_complex_string(self, word):
        echo_text = "foo" + word.replace("\xa0", " ").replace(" ", "") + "   bar"
        echo_text_arg = Argument(
            Argument.LIST, 'echo_text', [echo_text]
        )
        self.assertEqual(Echo().execute({'echo_text': echo_text_arg}), echo_text)

    @given(valid_string())
    def test_basic_string_generated(self, word):

        echo_text = word.replace("\xa0", " ").replace(" ", "")
        echo_text_arg = Argument(
            Argument.LIST, 'echo_text', [echo_text]
        )
        self.assertEqual(Echo().execute({'echo_text': echo_text_arg}), echo_text)