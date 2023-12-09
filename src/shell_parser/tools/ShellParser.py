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
        4,1,10,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,3,0,24,8,0,1,1,1,1,3,1,28,
        8,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,44,8,2,1,3,5,3,47,8,3,10,3,12,3,50,9,3,1,3,1,3,5,3,54,8,3,10,3,
        12,3,57,9,3,5,3,59,8,3,10,3,12,3,62,9,3,1,3,1,3,5,3,66,8,3,10,3,
        12,3,69,9,3,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,5,3,78,8,3,10,3,
        12,3,81,9,3,1,4,1,4,3,4,85,8,4,1,5,1,5,5,5,89,8,5,10,5,12,5,92,9,
        5,1,5,1,5,1,6,1,6,4,6,98,8,6,11,6,12,6,99,1,7,1,7,1,8,1,8,1,8,0,
        0,9,0,2,4,6,8,10,12,14,16,0,2,1,0,7,9,1,0,3,5,113,0,23,1,0,0,0,2,
        27,1,0,0,0,4,43,1,0,0,0,6,48,1,0,0,0,8,84,1,0,0,0,10,86,1,0,0,0,
        12,97,1,0,0,0,14,101,1,0,0,0,16,103,1,0,0,0,18,24,3,6,3,0,19,24,
        3,4,2,0,20,21,3,2,1,0,21,22,5,0,0,1,22,24,1,0,0,0,23,18,1,0,0,0,
        23,19,1,0,0,0,23,20,1,0,0,0,24,1,1,0,0,0,25,28,3,6,3,0,26,28,3,4,
        2,0,27,25,1,0,0,0,27,26,1,0,0,0,28,29,1,0,0,0,29,33,5,1,0,0,30,34,
        3,6,3,0,31,34,3,4,2,0,32,34,3,2,1,0,33,30,1,0,0,0,33,31,1,0,0,0,
        33,32,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,0,35,36,3,6,3,0,36,37,5,2,
        0,0,37,38,3,6,3,0,38,44,1,0,0,0,39,40,3,6,3,0,40,41,5,2,0,0,41,42,
        3,4,2,0,42,44,1,0,0,0,43,35,1,0,0,0,43,39,1,0,0,0,44,5,1,0,0,0,45,
        47,5,10,0,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,
        0,0,49,60,1,0,0,0,50,48,1,0,0,0,51,55,3,10,5,0,52,54,5,10,0,0,53,
        52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,59,1,0,0,
        0,57,55,1,0,0,0,58,51,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,
        1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,73,3,12,6,0,64,66,5,10,0,
        0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,
        1,0,0,0,69,67,1,0,0,0,70,72,3,8,4,0,71,67,1,0,0,0,72,75,1,0,0,0,
        73,71,1,0,0,0,73,74,1,0,0,0,74,79,1,0,0,0,75,73,1,0,0,0,76,78,5,
        10,0,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,
        7,1,0,0,0,81,79,1,0,0,0,82,85,3,10,5,0,83,85,3,12,6,0,84,82,1,0,
        0,0,84,83,1,0,0,0,85,9,1,0,0,0,86,90,3,16,8,0,87,89,5,10,0,0,88,
        87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,
        0,92,90,1,0,0,0,93,94,3,12,6,0,94,11,1,0,0,0,95,98,3,14,7,0,96,98,
        5,6,0,0,97,95,1,0,0,0,97,96,1,0,0,0,98,99,1,0,0,0,99,97,1,0,0,0,
        99,100,1,0,0,0,100,13,1,0,0,0,101,102,7,0,0,0,102,15,1,0,0,0,103,
        104,7,1,0,0,104,17,1,0,0,0,14,23,27,33,43,48,55,60,67,73,79,84,90,
        97,99
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
    RULE_atom = 4
    RULE_redirection = 5
    RULE_argument = 6
    RULE_quotedArg = 7
    RULE_redirectionType = 8

    ruleNames =  [ "shell", "sequence", "pipe", "command", "atom", "redirection", 
                   "argument", "quotedArg", "redirectionType" ]

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
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.pipe()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.sequence()
                self.state = 21
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
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 25
                self.command()
                pass

            elif la_ == 2:
                self.state = 26
                self.pipe()
                pass


            self.state = 29
            self.match(ShellParser.T__0)
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 30
                self.command()

            elif la_ == 2:
                self.state = 31
                self.pipe()

            elif la_ == 3:
                self.state = 32
                self.sequence()


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
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.command()
                self.state = 36
                self.match(ShellParser.T__1)
                self.state = 37
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.command()
                self.state = 40
                self.match(ShellParser.T__1)
                self.state = 41
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
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 45
                self.match(ShellParser.WS)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 51
                self.redirection()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 52
                    self.match(ShellParser.WS)
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.argument()
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==10:
                        self.state = 64
                        self.match(ShellParser.WS)
                        self.state = 69
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 70
                    self.atom() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 76
                self.match(ShellParser.WS)
                self.state = 81
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
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.redirection()
                pass
            elif token in [6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
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
        self.enterRule(localctx, 10, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.redirectionType()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 87
                self.match(ShellParser.WS)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
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
        self.enterRule(localctx, 12, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 97
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7, 8, 9]:
                        self.state = 95
                        self.quotedArg()
                        pass
                    elif token in [6]:
                        self.state = 96
                        self.match(ShellParser.UNQUOTED_ARG)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 99 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_quotedArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
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
        self.enterRule(localctx, 16, self.RULE_redirectionType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
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





