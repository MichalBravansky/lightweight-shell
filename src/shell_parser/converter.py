from antlr4 import InputStream, CommonTokenStream
from shell_parser.tools.ShellLexer import ShellLexer
from shell_parser.tools.ShellParser import ShellParser
from shell_parser.executors import (
    Call,
    Pipe,
    Redirect,
    RedirectionType,
    Sequence,
    UnsafeCall
)
import re
from glob import glob
from shell_parser.tools.ShellVisitor import ShellVisitor
import itertools

class Converter(ShellVisitor):

    def visitShell(self, ctx: ShellParser.ShellContext):
        return self.visit(ctx.getChild(0))

    def visitPipe(self, ctx: ShellParser.PipeContext):
        commands = iter([self.visit(command) for command in ctx.getChildren()
                if isinstance(command, (ShellParser.CommandContext, ShellParser.PipeContext))]
        )

        return Pipe(next(commands, None), next(commands, None))

    def visitCommand(self, ctx: ShellParser.CommandContext):
        processed_args = []
        redirections = [self.visit(arg) for arg in ctx.redirection()]

        command = self.visit(ctx.argument())[0]

        for arg in ctx.atom():
            args, redirection = self.visit(arg)
            processed_args.extend(args) if args else redirections.append(redirection)

        input_redirection = next((r for r in reversed(redirections) if r[0] == RedirectionType.READ), None)
        output_redirection = next((r for r in reversed(redirections) if r[0] != RedirectionType.READ), None)

        call = Call(command, processed_args) if command[0] != "_" else UnsafeCall(command[1:], processed_args)
        call = Redirect(call, *output_redirection) if output_redirection else call
        call = Redirect(call, *input_redirection) if input_redirection else call

        return call

    def _processDoubleQuotedArg(self, text):
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
            return "".join(self._processDoubleQuotedArg(double_quoted_text))
        elif ctx.BACKQUOTED_ARG():
            return self._processCommandSubstitution(
                ctx.BACKQUOTED_ARG().getText()[1:-1]
            )
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

        return ["".join(args)]

    def visitRedirectionType(self, ctx: ShellParser.RedirectionTypeContext):
        if ctx.REDIRECTION_READ():
            return RedirectionType.READ
        elif ctx.REDIRECTION_APPEND():
            return RedirectionType.APPEND
        else:
            return RedirectionType.OVERWRITE

    def visitRedirection(self, ctx: ShellParser.RedirectionContext):
        file = self.visit(ctx.argument())[0]
        redirection = self.visitRedirectionType(ctx.redirectionType())

        return (redirection, file)

    def visitSequence(self, ctx: ShellParser.SequenceContext):
        commands = iter([self.visit(command) for command in ctx.getChildren()
                         if isinstance(command, (ShellParser.CommandContext, ShellParser.PipeContext, ShellParser.SequenceContext))])

        return Sequence(next(commands, None), next(commands, None))
    
    def _getParserFromShell(self, shell: str) -> ShellParser:
        input_stream = InputStream(shell)

        lexer = ShellLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ShellParser(token_stream)

        return parser

    def _convertStringToArguments(self, command_output: str) -> [str]:

        args_context = self._getParserFromShell(command_output).arguments()
        processed_args = [self.visit(arg) for arg in args_context.argument()]

        if all(isinstance(i, list) for i in processed_args):
            return list(itertools.chain(*processed_args))

        return processed_args

    def _processCommandSubstitution(self, command_str: str) -> str:

        inner_tree = self._getParserFromShell(command_str).shell()
        inner_output = self.visit(inner_tree).evaluate()

        arg_output = self._convertStringToArguments(inner_output.replace("\n", " "))

        return " ".join(arg_output) if arg_output else inner_output.replace("\n", " ")
