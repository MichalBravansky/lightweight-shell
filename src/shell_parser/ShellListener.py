# Generated from Shell.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellParser import ShellParser
else:
    from ShellParser import ShellParser

# This class defines a complete listener for a parse tree produced by ShellParser.
class ShellListener(ParseTreeListener):

    # Enter a parse tree produced by ShellParser#shell.
    def enterShell(self, ctx:ShellParser.ShellContext):
        pass

    # Exit a parse tree produced by ShellParser#shell.
    def exitShell(self, ctx:ShellParser.ShellContext):
        pass


    # Enter a parse tree produced by ShellParser#sequence.
    def enterSequence(self, ctx:ShellParser.SequenceContext):
        pass

    # Exit a parse tree produced by ShellParser#sequence.
    def exitSequence(self, ctx:ShellParser.SequenceContext):
        pass


    # Enter a parse tree produced by ShellParser#pipe.
    def enterPipe(self, ctx:ShellParser.PipeContext):
        pass

    # Exit a parse tree produced by ShellParser#pipe.
    def exitPipe(self, ctx:ShellParser.PipeContext):
        pass


    # Enter a parse tree produced by ShellParser#command.
    def enterCommand(self, ctx:ShellParser.CommandContext):
        pass

    # Exit a parse tree produced by ShellParser#command.
    def exitCommand(self, ctx:ShellParser.CommandContext):
        pass


    # Enter a parse tree produced by ShellParser#arguments.
    def enterArguments(self, ctx:ShellParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by ShellParser#arguments.
    def exitArguments(self, ctx:ShellParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by ShellParser#atom.
    def enterAtom(self, ctx:ShellParser.AtomContext):
        pass

    # Exit a parse tree produced by ShellParser#atom.
    def exitAtom(self, ctx:ShellParser.AtomContext):
        pass


    # Enter a parse tree produced by ShellParser#redirection.
    def enterRedirection(self, ctx:ShellParser.RedirectionContext):
        pass

    # Exit a parse tree produced by ShellParser#redirection.
    def exitRedirection(self, ctx:ShellParser.RedirectionContext):
        pass


    # Enter a parse tree produced by ShellParser#argument.
    def enterArgument(self, ctx:ShellParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ShellParser#argument.
    def exitArgument(self, ctx:ShellParser.ArgumentContext):
        pass


    # Enter a parse tree produced by ShellParser#quotedArg.
    def enterQuotedArg(self, ctx:ShellParser.QuotedArgContext):
        pass

    # Exit a parse tree produced by ShellParser#quotedArg.
    def exitQuotedArg(self, ctx:ShellParser.QuotedArgContext):
        pass


    # Enter a parse tree produced by ShellParser#redirectionType.
    def enterRedirectionType(self, ctx:ShellParser.RedirectionTypeContext):
        pass

    # Exit a parse tree produced by ShellParser#redirectionType.
    def exitRedirectionType(self, ctx:ShellParser.RedirectionTypeContext):
        pass



del ShellParser