from antlr4 import InputStream, CommonTokenStream
from shell_parser.tools.ShellLexer import ShellLexer
from shell_parser.tools.ShellParser import ShellParser
from shell_parser.executors import (
    Call,
    Pipe,
    Redirect,
    RedirectionType,
    Sequence,
    Executor,
)
from utils.unsafe_decorator import UnsafeDecorator
import re
from glob import glob
from shell_parser.tools.ShellVisitor import ShellVisitor
from utils.custom_error_listener import CustomErrorListener


class _ConverterHelper:
    @classmethod
    def processShell(cls, shell: str) -> str:
        """
        Processes a given shell command string and converts it into a more manageable format.

        This method parses the input shell command, applies various transformations using a custom visitor pattern,
        and then compiles the results into a single string.

        Args:
            shell (str): The shell command string to be processed.

        Returns:
            str: A processed version of the input shell command.
        """

        input_stream = InputStream(shell)

        lexer = ShellLexer(input_stream)
        lexer.addErrorListener(CustomErrorListener())

        token_stream = CommonTokenStream(lexer)

        parser = ShellParser(token_stream)
        parser.addErrorListener(CustomErrorListener())

        inner_tree = parser.shell()
        inner_output = [
            output.strip('\n ')
            for output in Converter().visit(inner_tree).evaluate()
        ]

        return ' '.join(inner_output)


class Converter(ShellVisitor):
    def visitShell(self, ctx: ShellParser.ShellContext) -> Executor:
        """
        Visits the root node of the shell parse tree.

        This method is an entry point for visiting the shell parse tree. It delegates the processing to the child node.

        Args:
            ctx (ShellParser.ShellContext): The context of the shell parse tree.

        Returns:
            The result of visiting the first child of the shell context.
        """

        return self.visit(ctx.getChild(0))

    def visitSequence(self, ctx: ShellParser.SequenceContext) -> Sequence:
        """
        Processes a sequence of commands in the shell command.

        This method handles sequences of commands, allowing for the execution of multiple commands in order.

        Args:
            ctx (ShellParser.SequenceContext): The sequence context to process.

        Returns:
            Sequence: A Sequence object representing the series of commands.
        """

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

    def visitPipe(self, ctx: ShellParser.PipeContext) -> Pipe:
        """
        Processes a pipe context in the shell command.

        This method creates a Pipe object by visiting each command or pipe context within the given pipe context.

        Args:
            ctx (ShellParser.PipeContext): The pipe context to process.

        Returns:
            Pipe: A Pipe object representing the pipe operation in the shell command.
        """

        commands = iter(
            [
                self.visit(command)
                for command in ctx.getChildren()
                if isinstance(
                    command,
                    (ShellParser.CommandContext, ShellParser.PipeContext),
                )
            ]
        )

        return Pipe(next(commands, None), next(commands, None))

    def visitCommand(self, ctx: ShellParser.CommandContext) -> Call:
        """
        Processes a command context in the shell command.

        This method handles command parsing, including arguments and redirections, and constructs a Call object.

        Args:
            ctx (ShellParser.CommandContext): The command context to process.

        Returns:
            Call: A Call object representing the command in the shell command.
        """

        processed_args = []
        redirections = [self.visit(arg) for arg in ctx.redirection()]

        command = self.visit(ctx.argument())[0]

        for arg in ctx.atom():
            args, redirection = self.visit(arg)
            (
                processed_args.extend(args)
                if args
                else redirections.append(redirection)
            )

        input_redirection = next(
            (
                r
                for r in reversed(redirections)
                if r[0] == RedirectionType.READ
            ),
            None,
        )
        output_redirection = next(
            (
                r
                for r in reversed(redirections)
                if r[0] != RedirectionType.READ
            ),
            None,
        )

        call = (
            Call(command, processed_args)
            if command[0] != '_'
            else Call(command[1:], processed_args)
        )
        call = (
            Redirect(call, *output_redirection) if output_redirection else call
        )
        call = (
            Redirect(call, *input_redirection) if input_redirection else call
        )

        if command[0] == '_':
            call = UnsafeDecorator(call)

        return call

    def visitQuotedArg(self, ctx: ShellParser.QuotedArgContext) -> [str]:
        """
        Processes a quoted argument in the shell command.

        This method handles different types of quoted arguments (single, double, backquoted) and processes them accordingly.

        Args:
            ctx (ShellParser.QuotedArgContext): The quoted argument context to process.

        Returns:
            [str]: A list containing the processed quoted argument.
        """

        text = ctx.getText()
        if ctx.SINGLE_QUOTED_ARG():
            return [text[1:-1].replace("\\'", "'")]
        elif ctx.DOUBLE_QUOTED_ARG():
            replace_func = lambda x: _ConverterHelper.processShell(x.group(1))
            return re.sub(
                r'`([^`\n]*)`', replace_func, text[1:-1].replace('\\"', '"')
            )

        return _ConverterHelper.processShell(text[1:-1])

    def visitAtom(
        self, ctx: ShellParser.AtomContext
    ) -> ([str], (RedirectionType, str)):
        """
        Processes an atom in the shell command.

        This method handles individual atomic elements in the command, such as arguments and redirections.

        Args:
            ctx (ShellParser.AtomContext): The atom context to process.

        Returns:
            tuple: A tuple with processed argument or redirection.
        """

        child = ctx.getChild(0)
        return (
            (self.visit(child), None)
            if not isinstance(child, ShellParser.RedirectionContext)
            else (None, self.visit(child))
        )

    def visitArgument(self, ctx: ShellParser.ArgumentContext) -> [str]:
        """
        Processes an argument in the shell command.

        This method handles the arguments of a command, including globbing and concatenation.

        Args:
            ctx (ShellParser.ArgumentContext): The argument context to process.

        Returns:
            [str]: A list of processed arguments.
        """

        args = []
        globbing = False

        for arg in ctx.getChildren():
            if isinstance(arg, ShellParser.QuotedArgContext):
                argument = self.visit(arg)
            else:
                argument = [arg.getText()]

                if '*' in argument[0]:
                    globbing = True

            args += argument

        if globbing:
            return glob(''.join(args))

        return [''.join(args)]

    def visitRedirectionType(
        self, ctx: ShellParser.RedirectionTypeContext
    ) -> RedirectionType:
        """
        Identifies the type of redirection in the shell command.

        This method determines whether the redirection is for reading, appending, or overwriting.

        Args:
            ctx (ShellParser.RedirectionTypeContext): The redirection type context to process.

        Returns:
            RedirectionType: The type of the redirection.
        """

        if ctx.REDIRECTION_READ():
            return RedirectionType.READ
        elif ctx.REDIRECTION_APPEND():
            return RedirectionType.APPEND
        else:
            return RedirectionType.OVERWRITE

    def visitRedirection(self, ctx: ShellParser.RedirectionContext):
        """
        Processes a redirection in the shell command.

        This method handles the redirection by processing the file and the type of redirection.

        Args:
            ctx (ShellParser.RedirectionContext): The redirection context to process.

        Returns:
            tuple: A tuple containing the redirection type and the file involved.
        """

        file = self.visit(ctx.argument())[0]
        redirection = self.visitRedirectionType(ctx.redirectionType())

        return (redirection, file)
