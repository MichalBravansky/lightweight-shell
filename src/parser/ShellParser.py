# Generated from src/parser/Shell.g4 by ANTLR 4.13.1
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
        4,1,12,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,5,0,25,8,0,10,0,12,0,28,
        9,0,1,0,3,0,31,8,0,1,1,1,1,1,1,1,1,5,1,37,8,1,10,1,12,1,40,9,1,1,
        2,1,2,5,2,44,8,2,10,2,12,2,47,9,2,1,2,3,2,50,8,2,1,3,1,3,1,4,1,4,
        1,5,1,5,1,5,1,6,1,6,1,6,3,6,62,8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,
        0,10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,8,10,1,0,4,6,66,0,20,1,0,0,
        0,2,32,1,0,0,0,4,41,1,0,0,0,6,51,1,0,0,0,8,53,1,0,0,0,10,55,1,0,
        0,0,12,61,1,0,0,0,14,63,1,0,0,0,16,65,1,0,0,0,18,67,1,0,0,0,20,26,
        3,2,1,0,21,22,3,6,3,0,22,23,3,2,1,0,23,25,1,0,0,0,24,21,1,0,0,0,
        25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,30,1,0,0,0,28,26,1,
        0,0,0,29,31,3,6,3,0,30,29,1,0,0,0,30,31,1,0,0,0,31,1,1,0,0,0,32,
        38,3,4,2,0,33,34,3,8,4,0,34,35,3,4,2,0,35,37,1,0,0,0,36,33,1,0,0,
        0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,3,1,0,0,0,40,38,1,
        0,0,0,41,45,5,2,0,0,42,44,3,12,6,0,43,42,1,0,0,0,44,47,1,0,0,0,45,
        43,1,0,0,0,45,46,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,48,50,3,10,
        5,0,49,48,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,52,5,3,0,0,52,7,
        1,0,0,0,53,54,5,1,0,0,54,9,1,0,0,0,55,56,3,18,9,0,56,57,3,12,6,0,
        57,11,1,0,0,0,58,62,5,7,0,0,59,62,3,16,8,0,60,62,3,14,7,0,61,58,
        1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,13,1,0,0,0,63,64,5,2,0,0,
        64,15,1,0,0,0,65,66,7,0,0,0,66,17,1,0,0,0,67,68,7,1,0,0,68,19,1,
        0,0,0,6,26,30,38,45,49,61
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
    RULE_sequenceOp = 3
    RULE_pipe = 4
    RULE_redirection = 5
    RULE_arg = 6
    RULE_commandArg = 7
    RULE_quotedArg = 8
    RULE_redirectionType = 9

    ruleNames =  [ "sequence", "commands", "command", "sequenceOp", "pipe", 
                   "redirection", "arg", "commandArg", "quotedArg", "redirectionType" ]

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
            self.state = 20
            self.commands()
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 21
                    self.sequenceOp()
                    self.state = 22
                    self.commands() 
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 29
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
            self.state = 32
            self.command()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 33
                self.pipe()
                self.state = 34
                self.command()
                self.state = 40
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

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.ArgContext)
            else:
                return self.getTypedRuleContext(ShellParser.ArgContext,i)


        def redirection(self):
            return self.getTypedRuleContext(ShellParser.RedirectionContext,0)


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
            self.state = 41
            self.match(ShellParser.COMMAND)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1924) != 0):
                self.state = 42
                self.arg()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                self.state = 48
                self.redirection()


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
        self.enterRule(localctx, 6, self.RULE_sequenceOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
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
        self.enterRule(localctx, 8, self.RULE_pipe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ShellParser.T__0)
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


        def arg(self):
            return self.getTypedRuleContext(ShellParser.ArgContext,0)


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
        self.enterRule(localctx, 10, self.RULE_redirection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.redirectionType()
            self.state = 56
            self.arg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
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
            return ShellParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = ShellParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arg)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(ShellParser.UNQUOTED_ARG)
                pass
            elif token in [8, 9, 10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.quotedArg()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
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
        self.enterRule(localctx, 14, self.RULE_commandArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
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
        self.enterRule(localctx, 16, self.RULE_quotedArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
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
        self.enterRule(localctx, 18, self.RULE_redirectionType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
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





