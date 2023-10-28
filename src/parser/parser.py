from antlr4 import *
from src.parser.ShellLexer import ShellLexer
from src.parser.ShellParser import ShellParser
from src.parser.ShellListener import ShellListener

from src.commands.echo import EchoCommand
from src.commands.cd import CdCommand
from src.commands.argument import Argument


class MyShellListener(ShellListener):
    def enterCommand(self, ctx):
        command_name = ctx.COMMAND().getText()
        args = [arg.getText() for arg in ctx.arg()]
        args_info = {"named_arguments": {"n": Argument(Argument.FLAG, "exclude_trailing_newline", False)}, "positional_arguments": [Argument(Argument.LIST, "echo_text", [])]}
        Argument.populate_args(args_info, args)
        Argument.set_keys_to_readable(args_info)
        self.execute_command(command_name, args_info)

    def execute_command(self, command_name, args):
        command_classes = {
            'echo': EchoCommand,
            'cd': CdCommand,
        }
        command_class = command_classes.get(command_name.lower())
        if command_class is None:
            print(f'Unknown command: {command_name}')
        else:
            command = command_class()
            command.execute(args)

def main():
    # Load the input
    while True:
        user_input = input("shell> ")

        input_stream = InputStream(user_input)

        # Create the lexer
        lexer = ShellLexer(input_stream)

        # Create a stream of tokens
        token_stream = CommonTokenStream(lexer)

        # Create the parser
        parser = ShellParser(token_stream)

        # Create a listener
        listener = MyShellListener()

        # Build the parse tree
        tree = parser.commands()

        # Walk the parse tree with the listener
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

if __name__ == '__main__':
    main()
