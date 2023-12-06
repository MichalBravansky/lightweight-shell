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
        4,1,10,132,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,3,0,28,8,
        0,1,1,1,1,3,1,32,8,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,3,5,3,53,8,3,10,3,12,3,56,9,
        3,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,5,3,65,8,3,10,3,12,3,68,9,
        3,1,3,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,5,3,78,8,3,10,3,12,3,81,
        9,3,1,3,5,3,84,8,3,10,3,12,3,87,9,3,1,4,1,4,1,5,5,5,92,8,5,10,5,
        12,5,95,9,5,1,5,5,5,98,8,5,10,5,12,5,101,9,5,1,5,5,5,104,8,5,10,
        5,12,5,107,9,5,1,6,1,6,3,6,111,8,6,1,7,1,7,5,7,115,8,7,10,7,12,7,
        118,9,7,1,7,1,7,1,8,1,8,4,8,124,8,8,11,8,12,8,125,1,9,1,9,1,10,1,
        10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,2,1,0,7,9,1,0,3,5,140,
        0,27,1,0,0,0,2,31,1,0,0,0,4,49,1,0,0,0,6,54,1,0,0,0,8,88,1,0,0,0,
        10,99,1,0,0,0,12,110,1,0,0,0,14,112,1,0,0,0,16,123,1,0,0,0,18,127,
        1,0,0,0,20,129,1,0,0,0,22,28,3,6,3,0,23,28,3,4,2,0,24,25,3,2,1,0,
        25,26,5,0,0,1,26,28,1,0,0,0,27,22,1,0,0,0,27,23,1,0,0,0,27,24,1,
        0,0,0,28,1,1,0,0,0,29,32,3,6,3,0,30,32,3,4,2,0,31,29,1,0,0,0,31,
        30,1,0,0,0,32,33,1,0,0,0,33,37,5,1,0,0,34,38,3,6,3,0,35,38,3,4,2,
        0,36,38,3,2,1,0,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,37,38,
        1,0,0,0,38,39,1,0,0,0,39,40,5,0,0,1,40,3,1,0,0,0,41,42,3,6,3,0,42,
        43,5,2,0,0,43,44,3,6,3,0,44,50,1,0,0,0,45,46,3,6,3,0,46,47,5,2,0,
        0,47,48,3,4,2,0,48,50,1,0,0,0,49,41,1,0,0,0,49,45,1,0,0,0,50,5,1,
        0,0,0,51,53,5,10,0,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,
        55,1,0,0,0,55,66,1,0,0,0,56,54,1,0,0,0,57,61,3,14,7,0,58,60,5,10,
        0,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,65,
        1,0,0,0,63,61,1,0,0,0,64,57,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,
        66,67,1,0,0,0,67,69,1,0,0,0,68,66,1,0,0,0,69,79,3,16,8,0,70,72,5,
        10,0,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,
        76,1,0,0,0,75,73,1,0,0,0,76,78,3,12,6,0,77,73,1,0,0,0,78,81,1,0,
        0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,85,1,0,0,0,81,79,1,0,0,0,82,84,
        5,10,0,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,
        86,7,1,0,0,0,87,85,1,0,0,0,88,89,5,9,0,0,89,9,1,0,0,0,90,92,5,10,
        0,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,
        1,0,0,0,95,93,1,0,0,0,96,98,3,16,8,0,97,93,1,0,0,0,98,101,1,0,0,
        0,99,97,1,0,0,0,99,100,1,0,0,0,100,105,1,0,0,0,101,99,1,0,0,0,102,
        104,5,10,0,0,103,102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,
        106,1,0,0,0,106,11,1,0,0,0,107,105,1,0,0,0,108,111,3,14,7,0,109,
        111,3,16,8,0,110,108,1,0,0,0,110,109,1,0,0,0,111,13,1,0,0,0,112,
        116,3,20,10,0,113,115,5,10,0,0,114,113,1,0,0,0,115,118,1,0,0,0,116,
        114,1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,116,1,0,0,0,119,
        120,3,16,8,0,120,15,1,0,0,0,121,124,3,18,9,0,122,124,5,6,0,0,123,
        121,1,0,0,0,123,122,1,0,0,0,124,125,1,0,0,0,125,123,1,0,0,0,125,
        126,1,0,0,0,126,17,1,0,0,0,127,128,7,0,0,0,128,19,1,0,0,0,129,130,
        7,1,0,0,130,21,1,0,0,0,17,27,31,37,49,54,61,66,73,79,85,93,99,105,
        110,116,123,125
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
    RULE_commandSubstitution = 4
    RULE_args = 5
    RULE_atom = 6
    RULE_redirection = 7
    RULE_argument = 8
    RULE_quotedArg = 9
    RULE_redirectionType = 10

    ruleNames =  [ "shell", "sequence", "pipe", "command", "commandSubstitution", 
                   "args", "atom", "redirection", "argument", "quotedArg", 
                   "redirectionType" ]

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
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.pipe()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.sequence()
                self.state = 25
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
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 29
                self.command()
                pass

            elif la_ == 2:
                self.state = 30
                self.pipe()
                pass


            self.state = 33
            self.match(ShellParser.T__0)
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 34
                self.command()

            elif la_ == 2:
                self.state = 35
                self.pipe()

            elif la_ == 3:
                self.state = 36
                self.sequence()


            self.state = 39
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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.command()
                self.state = 42
                self.match(ShellParser.T__1)
                self.state = 43
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.command()
                self.state = 46
                self.match(ShellParser.T__1)
                self.state = 47
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
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 51
                self.match(ShellParser.WS)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 57
                self.redirection()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 58
                    self.match(ShellParser.WS)
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.argument()
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==10:
                        self.state = 70
                        self.match(ShellParser.WS)
                        self.state = 75
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 76
                    self.atom() 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 82
                self.match(ShellParser.WS)
                self.state = 87
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
        self.enterRule(localctx, 8, self.RULE_commandSubstitution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ShellParser.BACKQUOTED_ARG)
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


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.WS)
            else:
                return self.getToken(ShellParser.WS, i)

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
        self.enterRule(localctx, 10, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==10:
                        self.state = 90
                        self.match(ShellParser.WS)
                        self.state = 95
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 96
                    self.argument() 
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 102
                self.match(ShellParser.WS)
                self.state = 107
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
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.redirection()
                pass
            elif token in [6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
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
        self.enterRule(localctx, 14, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.redirectionType()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 113
                self.match(ShellParser.WS)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
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
        self.enterRule(localctx, 16, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 123
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7, 8, 9]:
                        self.state = 121
                        self.quotedArg()
                        pass
                    elif token in [6]:
                        self.state = 122
                        self.match(ShellParser.UNQUOTED_ARG)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 125 
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
        self.enterRule(localctx, 18, self.RULE_quotedArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
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
        self.enterRule(localctx, 20, self.RULE_redirectionType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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





