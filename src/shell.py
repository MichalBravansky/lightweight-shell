from antlr4 import *
from src.parser.ShellLexer import ShellLexer
from src.parser.ShellParser import ShellParser
from src.parser.parser import CustomVisitor


def main():
    # Load the input
    while True:
        user_input = input("> ")

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

        output = root.evaluate()

        if output:
            print(output, end="")


if __name__ == "__main__":
    main()
