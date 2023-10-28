# Generated from src/parser/Shell.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,41,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,4,0,17,8,0,11,0,12,0,18,1,1,4,1,22,8,1,11,1,12,1,23,1,
        2,1,2,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,6,4,6,36,8,6,11,6,12,6,37,1,
        6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,3,2,0,65,90,97,122,
        3,0,83,83,92,92,94,94,3,0,9,10,13,13,32,32,43,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,1,16,1,0,0,0,3,21,1,0,0,0,5,25,1,0,0,0,7,27,1,0,0,0,9,29,1,0,
        0,0,11,32,1,0,0,0,13,35,1,0,0,0,15,17,7,0,0,0,16,15,1,0,0,0,17,18,
        1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,2,1,0,0,0,20,22,7,1,0,0,21,
        20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,4,1,0,0,
        0,25,26,5,124,0,0,26,6,1,0,0,0,27,28,5,62,0,0,28,8,1,0,0,0,29,30,
        5,62,0,0,30,31,5,62,0,0,31,10,1,0,0,0,32,33,5,60,0,0,33,12,1,0,0,
        0,34,36,7,2,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,39,1,0,0,0,39,40,6,6,0,0,40,14,1,0,0,0,4,0,18,23,37,1,
        6,0,0
    ]

class ShellLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMAND = 1
    ARGUMENT = 2
    PIPE = 3
    REDIRECT_OUT = 4
    APPEND_OUT = 5
    REDIRECT_IN = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "'>'", "'>>'", "'<'" ]

    symbolicNames = [ "<INVALID>",
            "COMMAND", "ARGUMENT", "PIPE", "REDIRECT_OUT", "APPEND_OUT", 
            "REDIRECT_IN", "WS" ]

    ruleNames = [ "COMMAND", "ARGUMENT", "PIPE", "REDIRECT_OUT", "APPEND_OUT", 
                  "REDIRECT_IN", "WS" ]

    grammarFileName = "Shell.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


