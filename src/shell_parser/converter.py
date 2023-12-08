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
from utils.custom_error_listener import CustomErrorListener

class _ConverterHelper:

    @classmethod
    def processShell(cls, shell: str) -> str:

        input_stream = InputStream(shell)

        lexer = ShellLexer(input_stream)
        lexer.addErrorListener(CustomErrorListener())

        token_stream = CommonTokenStream(lexer)

        parser = ShellParser(token_stream)
        parser.addErrorListener(CustomErrorListener())

        inner_tree = parser.shell()
        inner_output = [output.strip("\n ") for output in Converter().visit(inner_tree).evaluate()]

        return " ".join(inner_output)
    

class Converter(ShellVisitor):

    def visitShell(self, ctx: ShellParser.ShellContext):
        return self.visit(ctx.getChild(0))

    def visitPipe(self, ctx: ShellParser.PipeContext):
        commands = iter([self.visit(command) for command in ctx.getChildren()
                if isinstance(command, (ShellParser.CommandContext, ShellParser.PipeContext))])

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

    def visitQuotedArg(self, ctx: ShellParser.QuotedArgContext):
        text = ctx.getText()
        if ctx.SINGLE_QUOTED_ARG():
            return [text[1:-1].replace("\\'", "'")]
        elif ctx.DOUBLE_QUOTED_ARG():
            replace_func = lambda x: _ConverterHelper.processShell(x.group(1))
            return re.sub(r"`([^`\n]*)`", replace_func, text[1:-1].replace('\\"', '"'))
        elif ctx.BACKQUOTED_ARG():
            return _ConverterHelper.processShell(text[1:-1])
        return [text]

    def visitAtom(self, ctx: ShellParser.AtomContext):
        child = ctx.getChild(0)
        return (self.visit(child), None) if isinstance(child, ShellParser.ArgumentContext) else (None, self.visit(child))

    def visitArgument(self, ctx: ShellParser.ArgumentContext):
        args = []
        globbing = False

        for arg in ctx.getChildren():
            if isinstance(arg, ShellParser.QuotedArgContext):
                argument = self.visit(arg)
            else:
                argument = [arg.getText()]

                if "*" in argument[0]:
                    globbing = True

            args += argument

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
