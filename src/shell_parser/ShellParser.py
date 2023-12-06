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
        4,1,10,128,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,3,0,26,8,0,1,1,1,1,
        3,1,30,8,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,48,8,2,1,3,5,3,51,8,3,10,3,12,3,54,9,3,1,3,1,3,
        5,3,58,8,3,10,3,12,3,61,9,3,5,3,63,8,3,10,3,12,3,66,9,3,1,3,1,3,
        5,3,70,8,3,10,3,12,3,73,9,3,1,3,5,3,76,8,3,10,3,12,3,79,9,3,1,3,
        5,3,82,8,3,10,3,12,3,85,9,3,1,4,5,4,88,8,4,10,4,12,4,91,9,4,1,4,
        5,4,94,8,4,10,4,12,4,97,9,4,1,4,5,4,100,8,4,10,4,12,4,103,9,4,1,
        5,1,5,3,5,107,8,5,1,6,1,6,5,6,111,8,6,10,6,12,6,114,9,6,1,6,1,6,
        1,7,1,7,4,7,120,8,7,11,7,12,7,121,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,
        4,6,8,10,12,14,16,18,0,2,1,0,7,9,1,0,3,5,137,0,25,1,0,0,0,2,29,1,
        0,0,0,4,47,1,0,0,0,6,52,1,0,0,0,8,95,1,0,0,0,10,106,1,0,0,0,12,108,
        1,0,0,0,14,119,1,0,0,0,16,123,1,0,0,0,18,125,1,0,0,0,20,26,3,6,3,
        0,21,26,3,4,2,0,22,23,3,2,1,0,23,24,5,0,0,1,24,26,1,0,0,0,25,20,
        1,0,0,0,25,21,1,0,0,0,25,22,1,0,0,0,26,1,1,0,0,0,27,30,3,6,3,0,28,
        30,3,4,2,0,29,27,1,0,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,35,5,1,0,
        0,32,36,3,6,3,0,33,36,3,4,2,0,34,36,3,2,1,0,35,32,1,0,0,0,35,33,
        1,0,0,0,35,34,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,5,0,0,1,
        38,3,1,0,0,0,39,40,3,6,3,0,40,41,5,2,0,0,41,42,3,6,3,0,42,48,1,0,
        0,0,43,44,3,6,3,0,44,45,5,2,0,0,45,46,3,4,2,0,46,48,1,0,0,0,47,39,
        1,0,0,0,47,43,1,0,0,0,48,5,1,0,0,0,49,51,5,10,0,0,50,49,1,0,0,0,
        51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,64,1,0,0,0,54,52,1,
        0,0,0,55,59,3,12,6,0,56,58,5,10,0,0,57,56,1,0,0,0,58,61,1,0,0,0,
        59,57,1,0,0,0,59,60,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,62,55,1,
        0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,
        64,1,0,0,0,67,77,3,14,7,0,68,70,5,10,0,0,69,68,1,0,0,0,70,73,1,0,
        0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,76,
        3,10,5,0,75,71,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,
        78,83,1,0,0,0,79,77,1,0,0,0,80,82,5,10,0,0,81,80,1,0,0,0,82,85,1,
        0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,7,1,0,0,0,85,83,1,0,0,0,86,
        88,5,10,0,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,
        0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,94,3,14,7,0,93,89,1,0,0,0,94,
        97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,101,1,0,0,0,97,95,1,0,
        0,0,98,100,5,10,0,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,
        101,102,1,0,0,0,102,9,1,0,0,0,103,101,1,0,0,0,104,107,3,12,6,0,105,
        107,3,14,7,0,106,104,1,0,0,0,106,105,1,0,0,0,107,11,1,0,0,0,108,
        112,3,18,9,0,109,111,5,10,0,0,110,109,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,
        116,3,14,7,0,116,13,1,0,0,0,117,120,3,16,8,0,118,120,5,6,0,0,119,
        117,1,0,0,0,119,118,1,0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,
        122,1,0,0,0,122,15,1,0,0,0,123,124,7,0,0,0,124,17,1,0,0,0,125,126,
        7,1,0,0,126,19,1,0,0,0,17,25,29,35,47,52,59,64,71,77,83,89,95,101,
        106,112,119,121
    ]

class ShellParser ( Parser ):

    grammarFileName = "Shell.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'|'", "'>'", "'>>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "REDIRECTION_OVERWRITE", 
                      "REDIRECTION_APPEND", "REDIRECTION_READ", "UNQUOTED_ARG", 
                      "SINGLE_QUOTED_ARG", "DOUBLE_QUOTED_ARG", "BACKQUOTED_ARG", 
                      "WS" ]

    RULE_shell = 0
    RULE_sequence = 1
    RULE_pipe = 2
    RULE_command = 3
    RULE_arguments = 4
    RULE_atom = 5
    RULE_redirection = 6
    RULE_argument = 7
    RULE_quotedArg = 8
    RULE_redirectionType = 9

    ruleNames =  [ "shell", "sequence", "pipe", "command", "arguments", 
                   "atom", "redirection", "argument", "quotedArg", "redirectionType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    REDIRECTION_OVERWRITE=3
    REDIRECTION_APPEND=4
    REDIRECTION_READ=5
    UNQUOTED_ARG=6
    SINGLE_QUOTED_ARG=7
    DOUBLE_QUOTED_ARG=8
    BACKQUOTED_ARG=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ShellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(ShellParser.CommandContext,0)


        def pipe(self):
            return self.getTypedRuleContext(ShellParser.PipeContext,0)


        def sequence(self):
            return self.getTypedRuleContext(ShellParser.SequenceContext,0)


        def EOF(self):
            return self.getToken(ShellParser.EOF, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_shell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShell" ):
                listener.enterShell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShell" ):
                listener.exitShell(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShell" ):
                return visitor.visitShell(self)
            else:
                return visitor.visitChildren(self)




    def shell(self):

        localctx = ShellParser.ShellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_shell)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.pipe()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.sequence()
                self.state = 23
                self.match(ShellParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ShellParser.EOF, 0)

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


        def sequence(self):
            return self.getTypedRuleContext(ShellParser.SequenceContext,0)


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
        self.enterRule(localctx, 2, self.RULE_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 27
                self.command()
                pass

            elif la_ == 2:
                self.state = 28
                self.pipe()
                pass


            self.state = 31
            self.match(ShellParser.T__0)
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 32
                self.command()

            elif la_ == 2:
                self.state = 33
                self.pipe()

            elif la_ == 3:
                self.state = 34
                self.sequence()


            self.state = 37
            self.match(ShellParser.EOF)
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

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.CommandContext)
            else:
                return self.getTypedRuleContext(ShellParser.CommandContext,i)


        def pipe(self):
            return self.getTypedRuleContext(ShellParser.PipeContext,0)


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
        self.enterRule(localctx, 4, self.RULE_pipe)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.command()
                self.state = 40
                self.match(ShellParser.T__1)
                self.state = 41
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.command()
                self.state = 44
                self.match(ShellParser.T__1)
                self.state = 45
                self.pipe()
                pass


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

        def argument(self):
            return self.getTypedRuleContext(ShellParser.ArgumentContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.WS)
            else:
                return self.getToken(ShellParser.WS, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(ShellParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.AtomContext)
            else:
                return self.getTypedRuleContext(ShellParser.AtomContext,i)


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
        self.enterRule(localctx, 6, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 49
                self.match(ShellParser.WS)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 55
                self.redirection()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 56
                    self.match(ShellParser.WS)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.argument()
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==10:
                        self.state = 68
                        self.match(ShellParser.WS)
                        self.state = 73
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 74
                    self.atom() 
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 80
                self.match(ShellParser.WS)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ShellParser.ArgumentContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.WS)
            else:
                return self.getToken(ShellParser.WS, i)

        def getRuleIndex(self):
            return ShellParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = ShellParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==10:
                        self.state = 86
                        self.match(ShellParser.WS)
                        self.state = 91
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 92
                    self.argument() 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 98
                self.match(ShellParser.WS)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(ShellParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(ShellParser.ArgumentContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ShellParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.redirection()
                pass
            elif token in [6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.argument()
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


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirectionType(self):
            return self.getTypedRuleContext(ShellParser.RedirectionTypeContext,0)


        def argument(self):
            return self.getTypedRuleContext(ShellParser.ArgumentContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.WS)
            else:
                return self.getToken(ShellParser.WS, i)

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
        self.enterRule(localctx, 12, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.redirectionType()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 109
                self.match(ShellParser.WS)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
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

        def quotedArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.QuotedArgContext)
            else:
                return self.getTypedRuleContext(ShellParser.QuotedArgContext,i)


        def UNQUOTED_ARG(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.UNQUOTED_ARG)
            else:
                return self.getToken(ShellParser.UNQUOTED_ARG, i)

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
        self.enterRule(localctx, 14, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 119
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7, 8, 9]:
                        self.state = 117
                        self.quotedArg()
                        pass
                    elif token in [6]:
                        self.state = 118
                        self.match(ShellParser.UNQUOTED_ARG)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 121 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 123
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
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
            self.state = 125
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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





