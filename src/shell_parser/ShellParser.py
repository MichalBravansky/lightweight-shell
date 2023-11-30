# Generated from Shell.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,86,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,5,
        0,29,8,0,10,0,12,0,32,9,0,1,0,3,0,35,8,0,1,1,1,1,1,1,1,1,5,1,41,
        8,1,10,1,12,1,44,9,1,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,1,2,1,2,
        5,2,55,8,2,10,2,12,2,58,9,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,5,6,67,8,
        6,10,6,12,6,70,9,6,1,7,1,7,1,7,1,8,1,8,1,8,3,8,78,8,8,1,9,1,9,1,
        10,1,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,2,
        1,0,8,10,1,0,4,6,82,0,24,1,0,0,0,2,36,1,0,0,0,4,48,1,0,0,0,6,59,
        1,0,0,0,8,61,1,0,0,0,10,63,1,0,0,0,12,68,1,0,0,0,14,71,1,0,0,0,16,
        77,1,0,0,0,18,79,1,0,0,0,20,81,1,0,0,0,22,83,1,0,0,0,24,30,3,2,1,
        0,25,26,3,8,4,0,26,27,3,2,1,0,27,29,1,0,0,0,28,25,1,0,0,0,29,32,
        1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,
        33,35,3,8,4,0,34,33,1,0,0,0,34,35,1,0,0,0,35,1,1,0,0,0,36,42,3,4,
        2,0,37,38,3,10,5,0,38,39,3,4,2,0,39,41,1,0,0,0,40,37,1,0,0,0,41,
        44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,3,1,0,0,0,44,42,1,0,0,
        0,45,47,3,14,7,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,
        1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,56,5,2,0,0,52,55,3,16,8,0,
        53,55,3,14,7,0,54,52,1,0,0,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,
        0,0,0,56,57,1,0,0,0,57,5,1,0,0,0,58,56,1,0,0,0,59,60,5,10,0,0,60,
        7,1,0,0,0,61,62,5,3,0,0,62,9,1,0,0,0,63,64,5,1,0,0,64,11,1,0,0,0,
        65,67,3,16,8,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,
        0,0,0,69,13,1,0,0,0,70,68,1,0,0,0,71,72,3,22,11,0,72,73,3,16,8,0,
        73,15,1,0,0,0,74,78,5,7,0,0,75,78,3,20,10,0,76,78,3,18,9,0,77,74,
        1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,17,1,0,0,0,79,80,5,2,0,0,
        80,19,1,0,0,0,81,82,7,0,0,0,82,21,1,0,0,0,83,84,7,1,0,0,84,23,1,
        0,0,0,8,30,34,42,48,54,56,68,77
    ]

class ShellParser ( Parser ):

    grammarFileName = "Shell.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "<INVALID>", "';'", "'>'", "'>>'", 
                     "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMAND", "SEQUENCE_OP", 
                      "REDIRECTION_OVERWRITE", "REDIRECTION_APPEND", "REDIRECTION_READ", 
                      "UNQUOTED_ARG", "SINGLE_QUOTED_ARG", "DOUBLE_QUOTED_ARG", 
                      "BACKQUOTED_ARG", "FILE", "WS" ]

    RULE_sequence = 0
    RULE_commands = 1
    RULE_command = 2
    RULE_commandSubstitution = 3
    RULE_sequenceOp = 4
    RULE_pipe = 5
    RULE_args = 6
    RULE_redirection = 7
    RULE_argument = 8
    RULE_commandArg = 9
    RULE_quotedArg = 10
    RULE_redirectionType = 11

    ruleNames =  [ "sequence", "commands", "command", "commandSubstitution", 
                   "sequenceOp", "pipe", "args", "redirection", "argument", 
                   "commandArg", "quotedArg", "redirectionType" ]

    EOF = Token.EOF
    T__0=1
    COMMAND=2
    SEQUENCE_OP=3
    REDIRECTION_OVERWRITE=4
    REDIRECTION_APPEND=5
    REDIRECTION_READ=6
    UNQUOTED_ARG=7
    SINGLE_QUOTED_ARG=8
    DOUBLE_QUOTED_ARG=9
    BACKQUOTED_ARG=10
    FILE=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commands(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.CommandsContext)
            else:
                return self.getTypedRuleContext(ShellParser.CommandsContext,i)


        def sequenceOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.SequenceOpContext)
            else:
                return self.getTypedRuleContext(ShellParser.SequenceOpContext,i)


        def getRuleIndex(self):
            return ShellParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = ShellParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.commands()
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 25
                    self.sequenceOp()
                    self.state = 26
                    self.commands() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 33
                self.sequenceOp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.CommandContext)
            else:
                return self.getTypedRuleContext(ShellParser.CommandContext,i)


        def pipe(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.PipeContext)
            else:
                return self.getTypedRuleContext(ShellParser.PipeContext,i)


        def getRuleIndex(self):
            return ShellParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommands" ):
                return visitor.visitCommands(self)
            else:
                return visitor.visitChildren(self)




    def commands(self):

        localctx = ShellParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.command()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 37
                self.pipe()
                self.state = 38
                self.command()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(ShellParser.COMMAND, 0)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(ShellParser.RedirectionContext,i)


        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ShellParser.ArgumentContext,i)


        def getRuleIndex(self):
            return ShellParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ShellParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                self.state = 45
                self.redirection()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(ShellParser.COMMAND)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2036) != 0):
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 7, 8, 9, 10]:
                    self.state = 52
                    self.argument()
                    pass
                elif token in [4, 5, 6]:
                    self.state = 53
                    self.redirection()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandSubstitutionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKQUOTED_ARG(self):
            return self.getToken(ShellParser.BACKQUOTED_ARG, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_commandSubstitution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandSubstitution" ):
                listener.enterCommandSubstitution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandSubstitution" ):
                listener.exitCommandSubstitution(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandSubstitution" ):
                return visitor.visitCommandSubstitution(self)
            else:
                return visitor.visitChildren(self)




    def commandSubstitution(self):

        localctx = ShellParser.CommandSubstitutionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_commandSubstitution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ShellParser.BACKQUOTED_ARG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEQUENCE_OP(self):
            return self.getToken(ShellParser.SEQUENCE_OP, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_sequenceOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequenceOp" ):
                listener.enterSequenceOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequenceOp" ):
                listener.exitSequenceOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceOp" ):
                return visitor.visitSequenceOp(self)
            else:
                return visitor.visitChildren(self)




    def sequenceOp(self):

        localctx = ShellParser.SequenceOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sequenceOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ShellParser.SEQUENCE_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShellParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipe" ):
                return visitor.visitPipe(self)
            else:
                return visitor.visitChildren(self)




    def pipe(self):

        localctx = ShellParser.PipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pipe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ShellParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ShellParser.ArgumentContext,i)


        def getRuleIndex(self):
            return ShellParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = ShellParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1924) != 0):
                self.state = 65
                self.argument()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirectionType(self):
            return self.getTypedRuleContext(ShellParser.RedirectionTypeContext,0)


        def argument(self):
            return self.getTypedRuleContext(ShellParser.ArgumentContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirection" ):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)




    def redirection(self):

        localctx = ShellParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_redirection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.redirectionType()
            self.state = 72
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNQUOTED_ARG(self):
            return self.getToken(ShellParser.UNQUOTED_ARG, 0)

        def quotedArg(self):
            return self.getTypedRuleContext(ShellParser.QuotedArgContext,0)


        def commandArg(self):
            return self.getTypedRuleContext(ShellParser.CommandArgContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ShellParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argument)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(ShellParser.UNQUOTED_ARG)
                pass
            elif token in [8, 9, 10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.quotedArg()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.commandArg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(ShellParser.COMMAND, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_commandArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandArg" ):
                listener.enterCommandArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandArg" ):
                listener.exitCommandArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandArg" ):
                return visitor.visitCommandArg(self)
            else:
                return visitor.visitChildren(self)




    def commandArg(self):

        localctx = ShellParser.CommandArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_commandArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ShellParser.COMMAND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTED_ARG(self):
            return self.getToken(ShellParser.SINGLE_QUOTED_ARG, 0)

        def DOUBLE_QUOTED_ARG(self):
            return self.getToken(ShellParser.DOUBLE_QUOTED_ARG, 0)

        def BACKQUOTED_ARG(self):
            return self.getToken(ShellParser.BACKQUOTED_ARG, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_quotedArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotedArg" ):
                listener.enterQuotedArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotedArg" ):
                listener.exitQuotedArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuotedArg" ):
                return visitor.visitQuotedArg(self)
            else:
                return visitor.visitChildren(self)




    def quotedArg(self):

        localctx = ShellParser.QuotedArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_quotedArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REDIRECTION_OVERWRITE(self):
            return self.getToken(ShellParser.REDIRECTION_OVERWRITE, 0)

        def REDIRECTION_APPEND(self):
            return self.getToken(ShellParser.REDIRECTION_APPEND, 0)

        def REDIRECTION_READ(self):
            return self.getToken(ShellParser.REDIRECTION_READ, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_redirectionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirectionType" ):
                listener.enterRedirectionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirectionType" ):
                listener.exitRedirectionType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirectionType" ):
                return visitor.visitRedirectionType(self)
            else:
                return visitor.visitChildren(self)




    def redirectionType(self):

        localctx = ShellParser.RedirectionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_redirectionType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





