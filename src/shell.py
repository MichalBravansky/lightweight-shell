from antlr4 import *
from src.parser.ShellLexer import ShellLexer
from src.parser.ShellParser import ShellParser
from src.parser.parser import CustomVisitor


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
    tree = parser.commands()

    # Use the visitor to visit the parse tree
    visitor = CustomVisitor()
    root = visitor.visit(tree)

    return root.evaluate()


def main():
    # Load the input
    while True:
        user_input = input("> ")

        output = eval(user_input)

        if output:
            print(output, end="")


if __name__ == "__main__":
    main()
