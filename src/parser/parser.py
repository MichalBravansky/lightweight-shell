from antlr4 import *
from src.parser.ShellLexer import ShellLexer
from src.parser.ShellParser import ShellParser
from src.parser.executors import Call, Pipe, Redirect, RedirectionType, Sequence
import re
import glob
from src.parser.ShellVisitor import ShellVisitor


class CustomVisitor(ShellVisitor):
    def visitCommands(self, ctx: ShellParser.CommandsContext):
        commands = ctx.command()

        if len(commands) == 1:
            return self.visit(commands[0])

        return Pipe([self.visit(command) for command in commands])

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
        pattern = r"`([^`\n]*)`"

        args_to_str_func = (
            lambda result: " ".join(result) if isinstance(result, list) else result
        )
        replace_func = lambda x: args_to_str_func(
            self._processCommandSubstitution(x.group(1))
        )

        return re.sub(pattern, replace_func, text)

    def visitQuotedArg(self, ctx: ShellParser.QuotedArgContext):
        if ctx.SINGLE_QUOTED_ARG():
            return ctx.SINGLE_QUOTED_ARG().getText()[1:-1].replace("\\'", "'")
        elif ctx.DOUBLE_QUOTED_ARG():
            double_quoted_text = (
                ctx.DOUBLE_QUOTED_ARG().getText()[1:-1].replace("\\ ", '"')
            )  # Remove double quotes
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
            return self.visitCommandSubstitution(ctx.commandSubstitution())

        # Handle globbing
        text = ctx.getText()
        if "*" in text:
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

    def visitCommandSubstitution(self, ctx: ShellParser.CommandSubstitutionContext):
        command = ctx.BACKQUOTED_ARG().getText()[1:-1]
        return self._processCommandSubstitution(command)

    def visitSequence(self, ctx: ShellParser.SequenceContext):
        commands = ctx.commands()
        return Sequence([self.visit(command) for command in commands])

    def _processCommandOutputAsArgs(self, command_output: str) -> [str]:
        input_stream = InputStream(command_output)

        lexer = ShellLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ShellParser(token_stream)

        args_context = parser.args()
        processed_args = [self.visit(arg) for arg in args_context.arg()]

        return processed_args

    def _processCommandSubstitution(self, command_str: str) -> str:
        inner_input_stream = InputStream(command_str)

        inner_lexer = ShellLexer(inner_input_stream)
        inner_token_stream = CommonTokenStream(inner_lexer)
        inner_parser = ShellParser(inner_token_stream)

        inner_tree = inner_parser.sequence()
        inner_output = self.visit(inner_tree).evaluate()

        output = inner_output.replace("\n", " ")

        arg_output = self._processCommandOutputAsArgs(inner_output.replace("\n", " "))

        return arg_output if arg_output else output


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
