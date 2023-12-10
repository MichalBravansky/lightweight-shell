import unittest
from antlr4 import InputStream, CommonTokenStream
from shell_parser.tools.ShellLexer import ShellLexer
from shell_parser.tools.ShellParser import ShellParser
from shell_parser.converter import Converter
from src.shell_parser.executors import ( Call, Pipe, Redirect, RedirectionType, Sequence, UnsafeCall, Executor )
from src.commands.argument import Argument
import unittest
import tempfile
from pathlib import Path
import os

class TestConverter(unittest.TestCase):

    @staticmethod
    def parse_command_line(command_line: str):
        input_stream = InputStream(command_line)
        lexer = ShellLexer(input_stream)
        token_stream = CommonTokenStream(lexer)

        parser = ShellParser(token_stream)
        tree = parser.shell()

        return tree.accept(Converter())

    def assertCallEqual(self, call: Call, expected_command: str, expected_args: dict):
        self.assertEqual(call._command, expected_command)
        self.assertCountEqual(call._args.keys(), expected_args.keys())

        for arg in call._args.keys():
            self.assertEqual(call._args[arg].type, expected_args[arg].type)
            self.assertEqual(call._args[arg].name, expected_args[arg].name)
            self.assertEqual(call._args[arg].value, expected_args[arg].value)

    def assertRedirectionEqual(self, redirection: Redirect, expected_type: RedirectionType, expected_file_name: str):
        self.assertEqual(redirection.redirect_type.name, expected_type.name)
        self.assertEqual(redirection.file_name, expected_file_name)

    def test_empty(self):
        call = self.parse_command_line("")
        self.assertIsNone(call)

    def test_semicon(self):
        call = self.parse_command_line(";")
        self.assertIsNone(call)

    def test_call_empty(self):
        call = self.parse_command_line("pwd")
        self.assertCallEqual(call, "pwd", {})

    def test_call_default(self):
        call = self.parse_command_line("ls")
        self.assertCallEqual(call, "ls", {"directory": Argument(Argument.STRING, "directory", ".")})

    def test_call_semicon(self):
        call = self.parse_command_line("ls;")
        self.assertCallEqual(call, "ls", {"directory": Argument(Argument.STRING, "directory", ".")})

    def test_call_whitespace(self):
        call = self.parse_command_line("   ls   ")
        self.assertCallEqual(call, "ls", {"directory": Argument(Argument.STRING, "directory", ".")})
    
    def test_call_non_quoted(self):
        call = self.parse_command_line("echo -n foo")
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", True), "echo_text": Argument(Argument.LIST, "echo_text", ["foo"])})

    def test_call_single_quoted(self):
        call = self.parse_command_line("echo ' foo '")
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [" foo "])})

    def test_call_double_quoted(self):
        call = self.parse_command_line('echo " foo "')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [" foo "])})
    
    def test_call_quoted_inside_double_quoted(self):
        call = self.parse_command_line('echo " foo \' bar "')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [" foo ' bar "])})

    def test_call_quoted_inside_non_quoted(self):
        call = self.parse_command_line('echo foo\'bar\'baz')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foobarbaz"])})

    def test_call_substitution(self):
        call = self.parse_command_line('echo `echo foo`')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foo"])})

    def test_call_substitution_inside_double_quoted(self):
        call = self.parse_command_line('echo "foo `echo bar`"')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foo bar"])})

    def test_call_nested_double_quoted(self):
        call = self.parse_command_line('echo "foo `echo "bar"`"')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foo bar"])})

    def test_call_substitution_split(self):
        call = self.parse_command_line('echo `echo foo  bar`')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foo bar"])})

    def test_call_substitution_inside_non_quoted(self):
        call = self.parse_command_line('echo foo`echo bar`baz')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foobarbaz"])})

    def test_call_substitution_command(self):
        call = self.parse_command_line('`echo echo` foo')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foo"])})

    def test_call_substitution_sequence(self):
        call = self.parse_command_line('echo `echo foo; echo bar`')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foo bar"])})

    def test_call_substitution_pipe(self):
        call = self.parse_command_line('echo `echo foo | echo bar`')
        self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["bar"])})

    def test_redirection_read(self):
        redirection = self.parse_command_line('echo < foo.txt')
        self.assertRedirectionEqual(redirection, RedirectionType.READ, "foo.txt")
        self.assertCallEqual(redirection.call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})

    def test_redirection_overwrite(self):
        redirection = self.parse_command_line('echo > foo.txt')
        self.assertRedirectionEqual(redirection, RedirectionType.OVERWRITE, "foo.txt")
        self.assertCallEqual(redirection.call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})
    
    def test_redirection_append(self):
        redirection = self.parse_command_line('echo >> foo.txt')
        self.assertRedirectionEqual(redirection, RedirectionType.APPEND, "foo.txt")
        self.assertCallEqual(redirection.call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})

    def test_redirection_red_overwrite(self):
        redirection = self.parse_command_line('echo < foo.txt > bar.txt')
        self.assertRedirectionEqual(redirection, RedirectionType.READ, "foo.txt")
        self.assertRedirectionEqual(redirection.call, RedirectionType.OVERWRITE, "bar.txt")
        self.assertCallEqual(redirection.call.call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})
    
    def test_redirection_in_front(self):
        redirection = self.parse_command_line('< foo.txt echo')
        self.assertRedirectionEqual(redirection, RedirectionType.READ, "foo.txt")
        self.assertCallEqual(redirection.call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})

    def test_redirection_single_quoted(self):
        redirection = self.parse_command_line('echo < foo.txt')
        self.assertRedirectionEqual(redirection, RedirectionType.READ, "foo.txt")
        self.assertCallEqual(redirection.call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})

    def test_redirection_no_whitespace(self):
        redirection = self.parse_command_line('echo<foo.txt')
        self.assertRedirectionEqual(redirection, RedirectionType.READ, "foo.txt")
        self.assertCallEqual(redirection.call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})

    def test_pipe_single(self):
        pipe = self.parse_command_line('echo foo | echo bar')
        self.assertCallEqual(pipe._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foo"])})
        self.assertCallEqual(pipe._right_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["bar"])})

    def test_pipe_multiple(self):
        pipe = self.parse_command_line('echo | echo | echo')
        self.assertCallEqual(pipe._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})
        self.assertCallEqual(pipe._right_executor._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})
        self.assertCallEqual(pipe._right_executor._right_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})

    def test_pipe_multiple_arguments(self):
        pipe = self.parse_command_line('echo foo"bar" | echo | echo baz')
        self.assertCallEqual(pipe._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ["foobar"])})
        self.assertCallEqual(pipe._right_executor._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", [])})
        self.assertCallEqual(pipe._right_executor._right_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST, "echo_text", ['baz'])})
    
    def test_sequence(self):
        sequence = self.parse_command_line('echo foo; echo bar')
        self.assertCallEqual(sequence._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,"echo_text", ["foo"])})
        self.assertCallEqual(sequence._right_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,"echo_text", ["bar"])})

    def test_sequence_multiple(self):
        sequence = self.parse_command_line('echo; echo; echo')
        self.assertCallEqual(sequence._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,"echo_text", [])})
        self.assertCallEqual(sequence._right_executor._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,"echo_text", [])})
        self.assertCallEqual(sequence._right_executor._right_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,"echo_text", [])})
    
    def test_sequence_multiple_arguments(self):
        sequence = self.parse_command_line('echo foo"bar"; echo; echo baz')
        self.assertCallEqual(sequence._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,"echo_text", ["foobar"])})
        self.assertCallEqual(sequence._right_executor._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,"echo_text", [])})
        self.assertCallEqual(sequence._right_executor._right_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,'echo_text', ['baz'])})

    def test_sequence_pipe(self):
        sequence = self.parse_command_line('echo foo | echo bar; echo baz')
        self.assertCallEqual(sequence._left_executor._left_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,'echo_text', ['foo'])})
        self.assertCallEqual(sequence._left_executor._right_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,'echo_text', ['bar'])})
        self.assertCallEqual(sequence._right_executor, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,'echo_text', ['baz'])})

    def test_globbing(self):
        with tempfile.TemporaryDirectory() as test_dir:
            test_file = os.path.join(test_dir, "test.txt")

            with open(test_file, "w") as f:
                pass

            call = self.parse_command_line(f"echo {test_dir}/*.txt")

            self.assertCallEqual(call, "echo", {"exclude_trailing_newline": Argument(Argument.FLAG, "exclude_trailing_newline", False), "echo_text": Argument(Argument.LIST,'echo_text', [os.path.join(test_dir, "test.txt")])})

if __name__ == "__main__":
    unittest.main()