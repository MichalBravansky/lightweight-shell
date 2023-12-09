from shell_parser.tools.ShellParser import ShellParser
from antlr4.Token import CommonToken
from antlr4.error.ErrorListener import ErrorListener
from utils.exceptions import ParsingError


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer: ShellParser, offendingSymbol: CommonToken, line: int, column: int, msg: str, e: Exception) -> None:
        raise ParsingError(msg)