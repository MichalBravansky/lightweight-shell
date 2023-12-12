from shell_parser.tools.ShellParser import ShellParser
from antlr4.Token import CommonToken
from antlr4.error.ErrorListener import ErrorListener
from utils.exceptions import ParsingError


class CustomErrorListener(ErrorListener):
    """
    The CustomErrorListener class is a custom implementation of the
    ErrorListener class from the ANTLR4 parsing library.

    This class overrides the syntaxError method from the ErrorListener class
    to provide custom error handling for syntax errors. When a syntax error is
    encountered during parsing, the syntaxError method is called with the
    following parameters:

    - recognizer: The parser that detected the error.
    - offendingSymbol: The token that caused the error.

    The syntaxError method in this class raises a ParsingError exception,
    which is a custom exception defined in the utils.exceptions module.
    """

    def syntaxError(
        self,
        recognizer: ShellParser,
        offendingSymbol: CommonToken,
        line: int,
        column: int,
        msg: str,
        e: Exception,
    ) -> None:
        raise ParsingError(msg)
