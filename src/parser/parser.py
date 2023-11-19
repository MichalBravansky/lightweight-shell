from antlr4 import *
from src.parser.ShellLexer import ShellLexer
from src.parser.ShellParser import ShellParser
from src.parser.ShellListener import ShellListener

from src.commands.echo import EchoCommand
from src.commands.cd import CdCommand
from src.commands.argument import Argument

from src.parser.ShellVisitor import ShellVisitor

from src.handler.argumentHandler import ArgumentHandler
from src.commands.commandFactory import CommandFactory


class CustomVisitor(ShellVisitor):
    def visitCommand(self, ctx: ShellParser.CommandContext):
        command_name = ctx.COMMAND().getText()

        args = [self.visit(arg) for arg in ctx.arg()]

        args_info = ArgumentHandler().assign_arguments(command_name, args)

        return CommandFactory().execute_command(command_name, args_info)

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
        data = visitor.visit(tree)

        if data:
            print(data, end="")


if __name__ == "__main__":
    main()
