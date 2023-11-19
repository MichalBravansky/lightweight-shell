from antlr4 import *
from src.parser.ShellLexer import ShellLexer
from src.parser.ShellParser import ShellParser
from src.parser.ShellListener import ShellListener
import glob
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

        # flatten args if they are lists. otherwise leave them as is
        flattened_args = []
        for arg in args:
            if isinstance(arg, list):
                flattened_args += arg
            else:
                flattened_args.append(arg)
                
        args_info = ArgumentHandler().assign_arguments(command_name, flattened_args)

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
        text = ctx.getText()
        if '*' in text:
            matches = glob.glob(text)
            if matches:
                # returns a list of args if we are globbing
                return matches
        return text


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
