from antlr4 import *
from src.parser.ShellLexer import ShellLexer
from src.parser.ShellParser import ShellParser
from src.parser.executors import Call, Pipe, Redirect, RedirectionType, Sequence
import re
import glob
from src.parser.ShellVisitor import ShellVisitor


class DummyBackquotedContext:
    def __init__(self, text):
        self.text = text

    def BACKQUOTED_ARG(self):
        # Creating a dummy inner class to mimic the structure
        class InnerDummy:
            def getText(inner_self):
                return self.text
        return InnerDummy()
    
class CustomVisitor(ShellVisitor):
    def visitCommands(self, ctx: ShellParser.CommandsContext):
        commands = ctx.command()

        if len(commands) == 1:
            return self.visit(commands[0])

        return Pipe([self.visit(command) for command in commands])


    def createDummyBackquotedContext(self, backquoted_text):
        return DummyBackquotedContext("`" + backquoted_text + "`")

    def visitCommand(self, ctx: ShellParser.CommandContext):
        command_name = ctx.COMMAND().getText()
        # Initialize an empty list for processed arguments
        processed_args = []

        # Iterate over each argument
        for arg in ctx.arg():
            # Process each argument, which may include command substitutions
            processed_arg = self.visit(arg)

            # Flatten args if they are lists, otherwise append them as is
            if isinstance(processed_arg, list):
                processed_args += processed_arg
            else:
                processed_args.append(processed_arg)

        # Create the call with the processed arguments
        call = Call(command_name, processed_args)

        # Handle redirection if present
        if ctx.redirection():
            redirection_type, file = self.visit(ctx.redirection())
            return Redirect(call, file, redirection_type)
        else:
            return call

    def processDoubleQuotedArg(self, text):
        pattern = r'`([^`\n]*)`'

        def replace_backquoted(match):
            backquoted_text = match.group(1)
            # Process the backquoted text as a command
            dummy_context = self.createDummyBackquotedContext(backquoted_text)
            # Use visitCommandSubstitution for processing
            command_output = self.visitCommandSubstitution(dummy_context)
            processed_output = self.processCommandOutputAsArgs(command_output)
            return ' '.join(processed_output) if isinstance(processed_output, list) else processed_output

        # Replace backquoted segments with their processed output
        return re.sub(pattern, replace_backquoted, text)
    
    def visitQuotedArg(self, ctx: ShellParser.QuotedArgContext):
        if ctx.SINGLE_QUOTED_ARG():
            return ctx.SINGLE_QUOTED_ARG().getText()[1:-1].replace("\\'", "'")
        elif ctx.DOUBLE_QUOTED_ARG():
            double_quoted_text = ctx.DOUBLE_QUOTED_ARG().getText()[1:-1].replace("\\ ", '"')  # Remove double quotes
            return self.processDoubleQuotedArg(double_quoted_text)
        elif ctx.BACKQUOTED_ARG():
            return self.visitCommandSubstitution(ctx.BACKQUOTED_ARG())
        else:
            return ctx.getText()

    def visitArg(self, ctx: ShellParser.ArgContext):
        # Handle quoted arguments
        if ctx.quotedArg():
            return self.visit(ctx.quotedArg())

        # Handle command substitutions
        if ctx.commandSubstitution():
            # Get the output of the command substitution
            command_output = self.visitCommandSubstitution(ctx.commandSubstitution())
            # Process the output as arguments
            processed_args = self.processCommandOutputAsArgs(command_output)
            return processed_args if processed_args else command_output

        # Handle globbing
        text = ctx.getText()
        if '*' in text:
            matches = glob.glob(text)
            if matches:
                # Returns a list of args if we are globbing
                return matches

        # Default return for unquoted and non-glob arguments
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
    
    def visitSequence(self, ctx: ShellParser.SequenceContext):
        commands = ctx.commands()
        return Sequence([self.visit(command) for command in commands])
    
    def visitCommandSubstitution(self, ctx):
        # Extract the command text within the backquotes
        inner_command_text = ctx.BACKQUOTED_ARG().getText()[1:-1]  # Remove the backquotes

        # Create a new InputStream for the inner comman
        inner_input_stream = InputStream(inner_command_text)

        # Create a lexer and parser for the inner command
        inner_lexer = ShellLexer(inner_input_stream)
        inner_token_stream = CommonTokenStream(inner_lexer)
        inner_parser = ShellParser(inner_token_stream)

        # Parse and visit the inner command
        inner_tree = inner_parser.sequence()  # Assuming the inner command is a sequence
        inner_output = self.visit(inner_tree).evaluate()

        # Process the output as needed
        return inner_output.replace("\n", " ")

    def processCommandOutputAsArgs(self, command_output):
        # Create a new InputStream for the command output
        input_stream = InputStream(command_output)

        # Create a lexer and parser for the command output
        lexer = ShellLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ShellParser(token_stream)

        # Parse the command output as arguments
        args_context = parser.args()  # Assuming 'args' is a rule in your grammar
        processed_args = [self.visit(arg) for arg in args_context.arg()]

        return processed_args


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
        tree = parser.sequence()

        # Use the visitor to visit the parse tree
        visitor = CustomVisitor()
        root = visitor.visit(tree)
        try:
            output = root.evaluate()
        except Exception as e:
            print(e)
            continue

        if output:
            print(output, end="")


if __name__ == "__main__":
    main()
