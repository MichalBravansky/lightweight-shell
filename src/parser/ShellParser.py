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
        4,1,9,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,5,2,
        28,8,2,10,2,12,2,31,9,2,1,2,3,2,34,8,2,1,3,1,3,1,4,1,4,1,4,1,5,1,
        5,1,5,3,5,44,8,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,2,4,45,
        0,14,1,0,0,0,2,16,1,0,0,0,4,25,1,0,0,0,6,35,1,0,0,0,8,37,1,0,0,0,
        10,43,1,0,0,0,12,45,1,0,0,0,14,15,3,2,1,0,15,1,1,0,0,0,16,22,3,4,
        2,0,17,18,3,6,3,0,18,19,3,4,2,0,19,21,1,0,0,0,20,17,1,0,0,0,21,24,
        1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,3,1,0,0,0,24,22,1,0,0,0,25,
        29,5,5,0,0,26,28,3,10,5,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,
        0,0,29,30,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,32,34,3,8,4,0,33,32,
        1,0,0,0,33,34,1,0,0,0,34,5,1,0,0,0,35,36,5,1,0,0,36,7,1,0,0,0,37,
        38,7,0,0,0,38,39,5,8,0,0,39,9,1,0,0,0,40,44,5,6,0,0,41,44,5,7,0,
        0,42,44,3,12,6,0,43,40,1,0,0,0,43,41,1,0,0,0,43,42,1,0,0,0,44,11,
        1,0,0,0,45,46,5,5,0,0,46,13,1,0,0,0,4,22,29,33,43
    ]

class ShellParser ( Parser ):

    grammarFileName = "Shell.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'>'", "'>>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMAND", "ARG", "QUOTED_ARG", "FILE", 
                      "WS" ]

    RULE_commands = 0
    RULE_commandLine = 1
    RULE_command = 2
    RULE_pipe = 3
    RULE_redirection = 4
    RULE_arg = 5
    RULE_commandArg = 6

    ruleNames =  [ "commands", "commandLine", "command", "pipe", "redirection", 
                   "arg", "commandArg" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    COMMAND=5
    ARG=6
    QUOTED_ARG=7
    FILE=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commandLine(self):
            return self.getTypedRuleContext(ShellParser.CommandLineContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)




    def commands(self):

        localctx = ShellParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_commands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.commandLine()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandLineContext(ParserRuleContext):
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
            return ShellParser.RULE_commandLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandLine" ):
                listener.enterCommandLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandLine" ):
                listener.exitCommandLine(self)




    def commandLine(self):

        localctx = ShellParser.CommandLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commandLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.command()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 17
                self.pipe()
                self.state = 18
                self.command()
                self.state = 24
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




    def command(self):

        localctx = ShellParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ShellParser.COMMAND)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0):
                self.state = 26
                self.arg()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 32
                self.redirection()


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




    def pipe(self):

        localctx = ShellParser.PipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pipe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
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

        def FILE(self):
            return self.getToken(ShellParser.FILE, 0)

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
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 38
            self.match(ShellParser.FILE)
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

        def ARG(self):
            return self.getToken(ShellParser.ARG, 0)

        def QUOTED_ARG(self):
            return self.getToken(ShellParser.QUOTED_ARG, 0)

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




    def arg(self):

        localctx = ShellParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arg)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(ShellParser.ARG)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(ShellParser.QUOTED_ARG)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
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




    def commandArg(self):

        localctx = ShellParser.CommandArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_commandArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(ShellParser.COMMAND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





