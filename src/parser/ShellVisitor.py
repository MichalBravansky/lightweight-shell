# Generated from Shell.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellParser import ShellParser
else:
    from ShellParser import ShellParser

# This class defines a complete generic visitor for a parse tree produced by ShellParser.

class ShellVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShellParser#commands.
    def visitCommands(self, ctx:ShellParser.CommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#command.
    def visitCommand(self, ctx:ShellParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#pipe.
    def visitPipe(self, ctx:ShellParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#redirection.
    def visitRedirection(self, ctx:ShellParser.RedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#arg.
    def visitArg(self, ctx:ShellParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#commandArg.
    def visitCommandArg(self, ctx:ShellParser.CommandArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#quotedArg.
    def visitQuotedArg(self, ctx:ShellParser.QuotedArgContext):
        return self.visitChildren(ctx)



del ShellParser