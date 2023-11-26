from antlr4 import *
from src.parser.ShellLexer import ShellLexer
from src.parser.ShellParser import ShellParser
from src.parser.executors import Call, Pipe, Redirect, RedirectionType

from src.commands.echo import EchoCommand
from src.commands.cd import CdCommand
from src.parser.ShellListener import ShellListener
import glob
from src.commands.argument import Argument
from src.parser.ShellVisitor import ShellVisitor

from src.commands.commandFactory import CommandFactory
from src.parser.executors import Call, Pipe, Redirect


class CustomVisitor(ShellVisitor):
    def visitCommands(self, ctx: ShellParser.CommandsContext):
        commands = ctx.command()

        if len(commands) == 1:
            return self.visit(commands[0])

        return Pipe([self.visit(command) for command in commands])

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
        
        call = Call(command_name, flattened_args)

        if ctx.redirection():
            redirection_type, file = self.visit(ctx.redirection())
            return Redirect(call, file, redirection_type)
        else:
            return call

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
        text = ctx.getText()
        if '*' in text:
            matches = glob.glob(text)
            if matches:
                # returns a list of args if we are globbing
                return matches
        return text

    def visitRedirectionType(self, ctx: ShellParser.RedirectionTypeContext):
        if ctx.REDIRECTION_READ():
            return RedirectionType.READ
        elif ctx.REDIRECTION_APPEND():
            return RedirectionType.APPEND
        else:
            return RedirectionType.OVERWRITE

    def visitRedirection(self, ctx: ShellParser.RedirectionContext):
        file = self.visit(ctx.arg())
        redirection = self.visitRedirectionType(ctx.redirectionType())

        return (redirection, file)


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
            print(output, end="\n")


if __name__ == "__main__":
    main()
