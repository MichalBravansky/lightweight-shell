from antlr4 import InputStream, CommonTokenStream
from shell_parser.ShellLexer import ShellLexer
from shell_parser.ShellParser import ShellParser
from shell_parser.parser import CustomVisitor
import sys


def eval(user_input: str) -> str:
    input_stream = InputStream(user_input)

    # Create the lexer
    lexer = ShellLexer(input_stream)

    # Create a stream of tokens
    token_stream = CommonTokenStream(lexer)

    # Create the parser
    parser = ShellParser(token_stream)

    # Create a listener
    visitor = CustomVisitor()

    # Build the parse tree
    tree = parser.shell()

    # Use the visitor to visit the parse tree
    visitor = CustomVisitor()
    root = visitor.visit(tree)

    return root.evaluate()


def main():
    args_num = len(sys.argv) - 1

    if args_num == 0:
        while True:
            user_input = input("> ")

            output = eval(user_input)

            if output:
                print(output, end="")
    else:
        command = sys.argv[2]

        output = eval(command)

        print(output, end="")


if __name__ == "__main__":
    main()
