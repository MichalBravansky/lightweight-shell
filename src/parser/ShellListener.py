# Generated from src/parser/Shell.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellParser import ShellParser
else:
    from ShellParser import ShellParser

# This class defines a complete listener for a parse tree produced by ShellParser.
class ShellListener(ParseTreeListener):

    # Enter a parse tree produced by ShellParser#commandLine.
    def enterCommandLine(self, ctx:ShellParser.CommandLineContext):
        pass

    # Exit a parse tree produced by ShellParser#commandLine.
    def exitCommandLine(self, ctx:ShellParser.CommandLineContext):
        pass


    # Enter a parse tree produced by ShellParser#pipeline.
    def enterPipeline(self, ctx:ShellParser.PipelineContext):
        pass

    # Exit a parse tree produced by ShellParser#pipeline.
    def exitPipeline(self, ctx:ShellParser.PipelineContext):
        pass


    # Enter a parse tree produced by ShellParser#simpleCommand.
    def enterSimpleCommand(self, ctx:ShellParser.SimpleCommandContext):
        pass

    # Exit a parse tree produced by ShellParser#simpleCommand.
    def exitSimpleCommand(self, ctx:ShellParser.SimpleCommandContext):
        pass


    # Enter a parse tree produced by ShellParser#command.
    def enterCommand(self, ctx:ShellParser.CommandContext):
        pass

    # Exit a parse tree produced by ShellParser#command.
    def exitCommand(self, ctx:ShellParser.CommandContext):
        pass


    # Enter a parse tree produced by ShellParser#redirection.
    def enterRedirection(self, ctx:ShellParser.RedirectionContext):
        pass

    # Exit a parse tree produced by ShellParser#redirection.
    def exitRedirection(self, ctx:ShellParser.RedirectionContext):
        pass



del ShellParser