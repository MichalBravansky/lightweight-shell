# Generated from Shell.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .ShellParser import ShellParser
else:
    from ShellParser import ShellParser

# This class defines a complete generic visitor for a parse tree produced by ShellParser.


class ShellVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by ShellParser#shell.
    def visitShell(self, ctx: ShellParser.ShellContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellParser#sequence.
    def visitSequence(self, ctx: ShellParser.SequenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellParser#pipe.
    def visitPipe(self, ctx: ShellParser.PipeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellParser#command.
    def visitCommand(self, ctx: ShellParser.CommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellParser#atom.
    def visitAtom(self, ctx: ShellParser.AtomContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellParser#redirection.
    def visitRedirection(self, ctx: ShellParser.RedirectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellParser#argument.
    def visitArgument(self, ctx: ShellParser.ArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellParser#quotedArg.
    def visitQuotedArg(self, ctx: ShellParser.QuotedArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellParser#redirectionType.
    def visitRedirectionType(self, ctx: ShellParser.RedirectionTypeContext):
        return self.visitChildren(ctx)


del ShellParser
