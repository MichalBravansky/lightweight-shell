from antlr4 import InputStream, CommonTokenStream
from shell_parser.tools.ShellLexer import ShellLexer
from shell_parser.tools.ShellParser import ShellParser
from shell_parser.converter import Converter
from utils.custom_error_listener import CustomErrorListener
import sys
import os
from utils.exceptions import (
    ParsingError,
    UnknownCommandError
)

import readline
from utils.auto_completer import AutoCompleter

def process(cmdline: str) -> str:
    input_stream = InputStream(cmdline)

    # Create the lexer
    lexer = ShellLexer(input_stream)
    lexer.addErrorListener(CustomErrorListener())

    # Create a stream of tokens
    token_stream = CommonTokenStream(lexer)

    # Create the parser
    parser = ShellParser(token_stream)
    parser.addErrorListener(CustomErrorListener())

    # Create a listener
    visitor = Converter()

    # Build the parse tree
    tree = parser.shell()

    # Use the visitor to visit the parse tree
    visitor = Converter()
    root = tree.accept(Converter())

    if root:
        return "\n".join(root.evaluate()) 

    return ""


def eval(user_input: str) -> str:

    try:
        return process(user_input) 
    except (
        ParsingError,
        UnknownCommandError
    ) as error:
        return str(error)
    except Exception as error:
        sys.exit(str(error))


def main():

    readline.parse_and_bind("tab: complete")
    readline.set_completer(AutoCompleter().completer)

    args_num = len(sys.argv) - 1

    if args_num == 0:

        while True:
            user_input = input(os.getcwd() + "> ")

            output = eval(user_input)

            if output:
                print(output, end="\n")
    else:
        command = sys.argv[2]

        output = eval(command)

        print(output, end="\n")


if __name__ == "__main__":
    main()