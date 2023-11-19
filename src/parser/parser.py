from antlr4 import *
from src.parser.ShellLexer import ShellLexer
from src.parser.ShellParser import ShellParser
from src.parser.executors import Call, Pipe, Redirect

from src.commands.echo import EchoCommand
from src.commands.cd import CdCommand
from src.commands.argument import Argument
from src.parser.ShellVisitor import ShellVisitor

from src.commands.commandFactory import CommandFactory
from src.parser.executors import Call, Pipe, Redirect


class CustomVisitor(ShellVisitor):
    def visitCommand(self, ctx: ShellParser.CommandContext):
        command_name = ctx.COMMAND().getText()

        args = [self.visit(arg) for arg in ctx.arg()]

        return Call(command_name, args)

    def visitPipe(self, ctx: ShellParser.PipeContext):
        calls = [self.visit(command) for command in ctx.command()]

        return Pipe(calls)

    def visitQuotedArg(self, ctx: ShellParser.QuotedArgContext):
        if ctx.SINGLE_QUOTED_ARG():
            return ctx.SINGLE_QUOTED_ARG().getText()[1:-1].replace("\\'", "'")
        elif ctx.DOUBLE_QUOTED_ARG():
            return ctx.DOUBLE_QUOTED_ARG().getText()[1:-1].replace('\\"', '"')
        elif ctx.BACKQUOTED_ARG():
            return ctx.BACKQUOTED_ARG().getText()[1:-1].replace("\\`", "`")
        else:
            return ctx.getText()

    def visitArg(self, ctx: ShellParser.ArgContext):
        if ctx.quotedArg():
            return self.visit(ctx.quotedArg())

        return ctx.getText()


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
