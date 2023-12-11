import unittest
from src.shell_parser.tools.ShellLexer import ShellLexer
from antlr4 import InputStream


class TestLexer(unittest.TestCase):

    @staticmethod
    def get_tokens(command_line: str):
        lexer = ShellLexer(InputStream(command_line))
        return [token.text for token in lexer.getAllTokens()]

    def test_empty(self):
        self.assertEqual(self.get_tokens(""), [])

    def test_simple_command(self):
        self.assertEqual(self.get_tokens("pwd"), ["pwd"])

    def test_command_with_single_argument(self):
        self.assertEqual(self.get_tokens("cat file.txt"), ["cat", " ", "file.txt"])

    def test_command_with_multiple_arguments(self):
        self.assertEqual(
            self.get_tokens("cp source.txt dest.txt"),
            ["cp", " ", "source.txt", " ", "dest.txt"]
        )

    def test_command_with_redirection(self):
        self.assertEqual(
            self.get_tokens("echo hello > file.txt"),
            ["echo", " ", "hello", " ", ">", " ", "file.txt"]
        )

    def test_command_with_pipe(self):
        self.assertEqual(
            self.get_tokens("cat file.txt | grep search"),
            ["cat", " ", "file.txt", " ", "|", " ", "grep", " ", "search"]
        )

    def test_sequence_of_commands(self):
        self.assertEqual(
            self.get_tokens("ls; pwd"),
            ["ls", ";", " ", "pwd"]
        )

    def test_command_with_single_quotes(self):
        self.assertEqual(
            self.get_tokens("echo 'single quoted text'"),
            ["echo", " ", "'single quoted text'"]
        )

    def test_command_with_double_quotes(self):
        self.assertEqual(
            self.get_tokens('echo "double quoted text"'),
            ['echo', ' ', '"double quoted text"']
        )

    def test_command_with_back_quotes(self):
        self.assertEqual(
            self.get_tokens("echo `command`"),
            ["echo", " ", "`command`"]
        )

    def test_command_with_mixed_quotes(self):
        self.assertEqual(
            self.get_tokens("echo 'single'\"double\"`back`"),
            ["echo", " ", "'single'", '"double"', "`back`"]
        )

    def test_command_with_redirection_and_pipe(self):
        self.assertEqual(
            self.get_tokens("grep search file.txt > output.txt | wc -l"),
            ["grep", " ", "search", " ", "file.txt", " ", ">", " ", "output.txt", " ", "|", " ", "wc", " ", "-l"]
        )

    def test_command_with_semicolon_and_pipe(self):
        self.assertEqual(
            self.get_tokens("ls; cat file.txt | grep search"),
            ["ls", ";", " ", "cat", " ", "file.txt", " ", "|", " ", "grep", " ", "search"]
        )

    def test_command_with_complex_redirection(self):
        self.assertEqual(
            self.get_tokens("sort < input.txt > output.txt"),
            ["sort", " ", "<", " ", "input.txt", " ", ">", " ", "output.txt"]
        )

    def test_command_with_append_redirection(self):
        self.assertEqual(
            self.get_tokens("echo text >> file.txt"),
            ["echo", " ", "text", " ", ">>", " ", "file.txt"]
        )


