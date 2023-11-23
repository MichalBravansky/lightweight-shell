# Generated from Shell.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,81,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,5,1,26,8,1,10,1,12,
        1,29,9,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,5,4,5,39,8,5,11,5,12,5,40,
        1,6,1,6,4,6,45,8,6,11,6,12,6,46,1,6,1,6,1,7,1,7,1,7,1,7,1,7,4,7,
        56,8,7,11,7,12,7,57,5,7,60,8,7,10,7,12,7,63,9,7,1,7,1,7,1,8,1,8,
        4,8,69,8,8,11,8,12,8,70,1,8,1,8,1,9,4,9,76,8,9,11,9,12,9,77,1,9,
        1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,1,0,7,3,
        0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,8,0,9,10,32,32,
        34,34,39,39,59,60,62,62,96,96,124,124,2,0,10,10,39,39,3,0,10,10,
        34,34,96,96,2,0,10,10,96,96,3,0,9,10,13,13,32,32,89,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,23,
        1,0,0,0,5,30,1,0,0,0,7,32,1,0,0,0,9,35,1,0,0,0,11,38,1,0,0,0,13,
        42,1,0,0,0,15,50,1,0,0,0,17,66,1,0,0,0,19,75,1,0,0,0,21,22,5,124,
        0,0,22,2,1,0,0,0,23,27,7,0,0,0,24,26,7,1,0,0,25,24,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,4,1,0,0,0,29,27,1,0,0,0,30,
        31,5,62,0,0,31,6,1,0,0,0,32,33,5,62,0,0,33,34,5,62,0,0,34,8,1,0,
        0,0,35,36,5,60,0,0,36,10,1,0,0,0,37,39,8,2,0,0,38,37,1,0,0,0,39,
        40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,12,1,0,0,0,42,44,5,39,
        0,0,43,45,8,3,0,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,48,1,0,0,0,48,49,5,39,0,0,49,14,1,0,0,0,50,61,5,34,0,
        0,51,60,3,17,8,0,52,56,8,4,0,0,53,54,5,92,0,0,54,56,5,34,0,0,55,
        52,1,0,0,0,55,53,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,
        0,58,60,1,0,0,0,59,51,1,0,0,0,59,55,1,0,0,0,60,63,1,0,0,0,61,59,
        1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,34,0,0,
        65,16,1,0,0,0,66,68,5,96,0,0,67,69,8,5,0,0,68,67,1,0,0,0,69,70,1,
        0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,96,0,0,73,
        18,1,0,0,0,74,76,7,6,0,0,75,74,1,0,0,0,76,77,1,0,0,0,77,75,1,0,0,
        0,77,78,1,0,0,0,78,79,1,0,0,0,79,80,6,9,0,0,80,20,1,0,0,0,10,0,27,
        40,46,55,57,59,61,70,77,1,6,0,0
    ]

class ShellLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMAND = 2
    REDIRECTION_OVERWRITE = 3
    REDIRECTION_APPEND = 4
    REDIRECTION_READ = 5
    UNQUOTED_ARG = 6
    SINGLE_QUOTED_ARG = 7
    DOUBLE_QUOTED_ARG = 8
    BACKQUOTED_ARG = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "'>'", "'>>'", "'<'" ]

    symbolicNames = [ "<INVALID>",
            "COMMAND", "REDIRECTION_OVERWRITE", "REDIRECTION_APPEND", "REDIRECTION_READ", 
            "UNQUOTED_ARG", "SINGLE_QUOTED_ARG", "DOUBLE_QUOTED_ARG", "BACKQUOTED_ARG", 
            "WS" ]

    ruleNames = [ "T__0", "COMMAND", "REDIRECTION_OVERWRITE", "REDIRECTION_APPEND", 
                  "REDIRECTION_READ", "UNQUOTED_ARG", "SINGLE_QUOTED_ARG", 
                  "DOUBLE_QUOTED_ARG", "BACKQUOTED_ARG", "WS" ]

    grammarFileName = "Shell.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


