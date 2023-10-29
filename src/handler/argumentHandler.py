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
        }

    def assign_arguments(self, command_name, args) -> dict:
        if command_name not in self.default_arguments:
            print("Command not found")

        else:
            args_info = dict(self.default_arguments[command_name])

            Argument.populate_args(args_info, args)
            args_info = Argument.set_keys_to_readable(args_info)

            return args_info
