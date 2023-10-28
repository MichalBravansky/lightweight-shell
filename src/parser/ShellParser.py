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
        4,1,7,39,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,1,2,5,2,24,8,2,10,2,12,2,
        27,9,2,1,3,1,3,5,3,31,8,3,10,3,12,3,34,9,3,1,4,1,4,1,4,1,4,0,0,5,
        0,2,4,6,8,0,1,1,0,4,6,36,0,10,1,0,0,0,2,13,1,0,0,0,4,21,1,0,0,0,
        6,28,1,0,0,0,8,35,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,
        0,13,18,3,4,2,0,14,15,5,3,0,0,15,17,3,4,2,0,16,14,1,0,0,0,17,20,
        1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,0,20,18,1,0,0,0,21,
        25,3,6,3,0,22,24,3,8,4,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,
        0,25,26,1,0,0,0,26,5,1,0,0,0,27,25,1,0,0,0,28,32,5,1,0,0,29,31,5,
        2,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,
        7,1,0,0,0,34,32,1,0,0,0,35,36,7,0,0,0,36,37,5,2,0,0,37,9,1,0,0,0,
        3,18,25,32
    ]

class ShellParser ( Parser ):

    grammarFileName = "Shell.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'|'", "'>'", 
                     "'>>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "COMMAND", "ARGUMENT", "PIPE", "REDIRECT_OUT", 
                      "APPEND_OUT", "REDIRECT_IN", "WS" ]

    RULE_commandLine = 0
    RULE_pipeline = 1
    RULE_simpleCommand = 2
    RULE_command = 3
    RULE_redirection = 4

    ruleNames =  [ "commandLine", "pipeline", "simpleCommand", "command", 
                   "redirection" ]

    EOF = Token.EOF
    COMMAND=1
    ARGUMENT=2
    PIPE=3
    REDIRECT_OUT=4
    APPEND_OUT=5
    REDIRECT_IN=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipeline(self):
            return self.getTypedRuleContext(ShellParser.PipelineContext,0)


        def EOF(self):
            return self.getToken(ShellParser.EOF, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_commandLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandLine" ):
                listener.enterCommandLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandLine" ):
                listener.exitCommandLine(self)




    def commandLine(self):

        localctx = ShellParser.CommandLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_commandLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.pipeline()
            self.state = 11
            self.match(ShellParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipelineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.SimpleCommandContext)
            else:
                return self.getTypedRuleContext(ShellParser.SimpleCommandContext,i)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.PIPE)
            else:
                return self.getToken(ShellParser.PIPE, i)

        def getRuleIndex(self):
            return ShellParser.RULE_pipeline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipeline" ):
                listener.enterPipeline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipeline" ):
                listener.exitPipeline(self)




    def pipeline(self):

        localctx = ShellParser.PipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pipeline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.simpleCommand()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 14
                self.match(ShellParser.PIPE)
                self.state = 15
                self.simpleCommand()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(ShellParser.CommandContext,0)


        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(ShellParser.RedirectionContext,i)


        def getRuleIndex(self):
            return ShellParser.RULE_simpleCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleCommand" ):
                listener.enterSimpleCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleCommand" ):
                listener.exitSimpleCommand(self)




    def simpleCommand(self):

        localctx = ShellParser.SimpleCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simpleCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.command()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                self.state = 22
                self.redirection()
                self.state = 27
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

        def ARGUMENT(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.ARGUMENT)
            else:
                return self.getToken(ShellParser.ARGUMENT, i)

        def getRuleIndex(self):
            return ShellParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = ShellParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ShellParser.COMMAND)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 29
                self.match(ShellParser.ARGUMENT)
                self.state = 34
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

        def ARGUMENT(self):
            return self.getToken(ShellParser.ARGUMENT, 0)

        def REDIRECT_OUT(self):
            return self.getToken(ShellParser.REDIRECT_OUT, 0)

        def APPEND_OUT(self):
            return self.getToken(ShellParser.APPEND_OUT, 0)

        def REDIRECT_IN(self):
            return self.getToken(ShellParser.REDIRECT_IN, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)




    def redirection(self):

        localctx = ShellParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 36
            self.match(ShellParser.ARGUMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





