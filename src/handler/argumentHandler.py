from typing import Any
from src.commands.argument import Argument


class ArgumentHandler:
    def __init__(self) -> None:
        self.default_arguments = {
            "echo": {
                "named_args": {
                    "n": Argument(Argument.FLAG, "exclude_trailing_newline", False)
                },
                "positional_args": [Argument(Argument.LIST, "echo_text", [])],
            },
            "cd": {
                "named_args": {},
                "positional_args": [Argument(Argument.STRING, "cd_path", "/")],
            },
            "pwd": {
                "named_args": {},
                "positional_args": [],
            },
            "ls": {
                "named_args": {},
                "positional_args": [Argument(Argument.STRING, "directory", ".")],
            },
            "cat": {
                "named_args": {
                    "b": Argument(Argument.FLAG, "number_nonblank", False),
                    "n": Argument(Argument.FLAG, "number_output_lines", False),
                    "s": Argument(Argument.FLAG, "squeeze_blank", False),
                    "u": Argument(Argument.FLAG, "disable_output_buffering", False),
                    "v": Argument(Argument.FLAG, "display_non_printing_chars", False),
                    "e": Argument(Argument.FLAG, "display_non_printing_chars_and_dollar", False),
                    "t": Argument(Argument.FLAG, "display_non_printing_chars_and_tab", False)
                },
                "positional_args": [Argument(Argument.LIST, "files", [])],
            },
            "head": {
                "named_args": {
                    "n": Argument(Argument.FLAG_WITH_INTEGER, "lines", 10),
                    # "c": Argument(Argument.INTEGER, "bytes", None),
                    # "q": Argument(Argument.FLAG, "silent", False),
                    # "v": Argument(Argument.FLAG, "verbose", False)
                },
                "positional_args": [Argument(Argument.STRING, "file", None)],
            }
        }

    def assign_arguments(self, command_name, args) -> dict:
        if command_name not in self.default_arguments:
            print("Command not found")

        else:
            args_info = dict(self.default_arguments[command_name])

            Argument.populate_args(args_info, args)
            args_info = Argument.set_keys_to_readable(args_info)

            return args_info
