# Generated from Shell.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellParser import ShellParser
else:
    from ShellParser import ShellParser

# This class defines a complete listener for a parse tree produced by ShellParser.
class ShellListener(ParseTreeListener):

    # Enter a parse tree produced by ShellParser#commands.
    def enterCommands(self, ctx:ShellParser.CommandsContext):
        pass

    # Exit a parse tree produced by ShellParser#commands.
    def exitCommands(self, ctx:ShellParser.CommandsContext):
        pass


    # Enter a parse tree produced by ShellParser#command.
    def enterCommand(self, ctx:ShellParser.CommandContext):
        pass

    # Exit a parse tree produced by ShellParser#command.
    def exitCommand(self, ctx:ShellParser.CommandContext):
        pass


    # Enter a parse tree produced by ShellParser#pipe.
    def enterPipe(self, ctx:ShellParser.PipeContext):
        pass

    # Exit a parse tree produced by ShellParser#pipe.
    def exitPipe(self, ctx:ShellParser.PipeContext):
        pass


    # Enter a parse tree produced by ShellParser#redirection.
    def enterRedirection(self, ctx:ShellParser.RedirectionContext):
        pass

    # Exit a parse tree produced by ShellParser#redirection.
    def exitRedirection(self, ctx:ShellParser.RedirectionContext):
        pass


    # Enter a parse tree produced by ShellParser#arg.
    def enterArg(self, ctx:ShellParser.ArgContext):
        pass

    # Exit a parse tree produced by ShellParser#arg.
    def exitArg(self, ctx:ShellParser.ArgContext):
        pass


    # Enter a parse tree produced by ShellParser#commandArg.
    def enterCommandArg(self, ctx:ShellParser.CommandArgContext):
        pass

    # Exit a parse tree produced by ShellParser#commandArg.
    def exitCommandArg(self, ctx:ShellParser.CommandArgContext):
        pass


    # Enter a parse tree produced by ShellParser#quotedArg.
    def enterQuotedArg(self, ctx:ShellParser.QuotedArgContext):
        pass

    # Exit a parse tree produced by ShellParser#quotedArg.
    def exitQuotedArg(self, ctx:ShellParser.QuotedArgContext):
        pass



del ShellParser