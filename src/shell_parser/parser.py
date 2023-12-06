from antlr4 import InputStream, CommonTokenStream
from shell_parser.ShellLexer import ShellLexer
from shell_parser.ShellParser import ShellParser
from shell_parser.executors import (
    Call,
    Pipe,
    Redirect,
    RedirectionType,
    Sequence,
)
import re
from glob import glob
from shell_parser.ShellVisitor import ShellVisitor
import itertools


class CustomVisitor(ShellVisitor):
    def visitShell(self, ctx: ShellParser.ShellContext):
        return self.visit(ctx.getChild(0))

    def visitPipe(self, ctx: ShellParser.PipeContext):
        commands = iter(
            [
                self.visit(command)
                for command in ctx.getChildren()
                if isinstance(
                    command, (ShellParser.CommandContext, ShellParser.PipeContext)
                )
            ]
        )

        return Pipe(next(commands, None), next(commands, None))

    def visitCommand(self, ctx: ShellParser.CommandContext):
        # Initialize an empty list for processed arguments
        processed_args = []
        redirections = []

        command = self.visit(ctx.argument())

        for arg in ctx.redirection():
            redirections.append(self.visit(arg))

        # Iterate over each argument
        for arg in ctx.atom():
            # Process each argument, which may include command substitutions
            args, redirection = self.visit(arg)

            if args:
                if isinstance(args, list):
                    processed_args += args
                else:
                    processed_args.append(args)
            else:
                redirections.append(redirection)

        input_redirection = next(
            (
                redirection
                for redirection in redirections[::-1]
                if redirection[0] == RedirectionType.READ
            ),
            None,
        )

        output_redirection = next(
            (
                redirection
                for redirection in redirections[::-1]
                if redirection[0] != RedirectionType.READ
            ),
            None,
        )

        call = Call(command, processed_args)

        if output_redirection:
            redirection_type, file = output_redirection
            call = Redirect(call, file, redirection_type)

        if input_redirection:
            redirection_type, file = input_redirection
            call = Redirect(call, file, redirection_type)

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
            return "".join(ctx.SINGLE_QUOTED_ARG().getText()[1:-1].replace("\\'", "'"))
        elif ctx.DOUBLE_QUOTED_ARG():
            double_quoted_text = (
                ctx.DOUBLE_QUOTED_ARG().getText()[1:-1].replace("\\ ", '"')
            )
            return "".join(self.processDoubleQuotedArg(double_quoted_text))
        elif ctx.BACKQUOTED_ARG():
            return self.visitCommandSubstitution(ctx.BACKQUOTED_ARG())
        else:
            return ctx.getText()

    def visitAtom(self, ctx: ShellParser.AtomContext):
        child = ctx.getChild(0)

        if isinstance(child, ShellParser.ArgumentContext):
            return (self.visit(child), None)
        else:
            return (None, self.visit(child))

    def visitArgument(self, ctx: ShellParser.ArgumentContext):
        args = []
        globbing = False

        for arg in ctx.getChildren():
            if isinstance(arg, ShellParser.QuotedArgContext):
                argument = self.visit(arg)
            else:
                argument = arg.getText()

                if "*" in argument:
                    globbing = True

            if isinstance(argument, list):
                args += argument
            else:
                args.append(argument)

        if globbing:
            return glob("".join(args))

        return "".join(args)

    def visitRedirectionType(self, ctx: ShellParser.RedirectionTypeContext):
        if ctx.REDIRECTION_READ():
            return RedirectionType.READ
        elif ctx.REDIRECTION_APPEND():
            return RedirectionType.APPEND
        else:
            return RedirectionType.OVERWRITE

    def visitRedirection(self, ctx: ShellParser.RedirectionContext):
        file = self.visit(ctx.argument())
        redirection = self.visitRedirectionType(ctx.redirectionType())

        return (redirection, file)

    def visitCommandSubstitution(self, ctx: ShellParser.CommandSubstitutionContext):
        command = ctx.getText()[1:-1]
        return self._processCommandSubstitution(command)

    def visitSequence(self, ctx: ShellParser.SequenceContext):
        commands = iter(
            [
                self.visit(command)
                for command in ctx.getChildren()
                if isinstance(
                    command,
                    (
                        ShellParser.CommandContext,
                        ShellParser.PipeContext,
                        ShellParser.SequenceContext,
                    ),
                )
            ]
        )

        return Sequence(next(commands, None), next(commands, None))

    def _processCommandOutputAsArgs(self, command_output: str) -> [str]:
        input_stream = InputStream(command_output)

        lexer = ShellLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ShellParser(token_stream)

        args_context = parser.args()
        data = args_context.argument()
        processed_args = [self.visit(arg) for arg in args_context.argument()]

        # Flattens the output
        if all(isinstance(i, list) for i in processed_args):
            return list(itertools.chain(*processed_args))

        return processed_args

    def _processCommandSubstitution(self, command_str: str) -> str:
        inner_input_stream = InputStream(command_str)

        inner_lexer = ShellLexer(inner_input_stream)
        inner_token_stream = CommonTokenStream(inner_lexer)
        inner_parser = ShellParser(inner_token_stream)

        inner_tree = inner_parser.shell()
        inner_output = self.visit(inner_tree).evaluate()

        output = inner_output.replace("\n", " ")

        arg_output = self._processCommandOutputAsArgs(inner_output.replace("\n", " "))

        return " ".join(arg_output) if arg_output else output
