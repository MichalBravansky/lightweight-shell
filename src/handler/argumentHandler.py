from commands.argument import Argument
from utils.exceptions import UnknownCommandError

class ArgumentHandler:
    def __init__(self) -> None:
        self.default_arguments = {
            "echo": {
                "named_args": {},
                "positional_args": [Argument(Argument.LIST, "echo_text", [])],
                "stop_positional_args_after_named": True,
            },
            "cd": {
                "named_args": {},
                "positional_args": [Argument(Argument.STRING, "cd_path", "/")],
                "stop_positional_args_after_named": True,
            },
            "pwd": {
                "named_args": {},
                "positional_args": [],
                "stop_positional_args_after_named": True,
            },
            "ls": {
                "named_args": {},
                "positional_args": [
                    Argument(Argument.STRING, "directory", ".")
                ],
                "stop_positional_args_after_named": True,
            },
            "cat": {
                "named_args": {},
                "positional_args": [Argument(Argument.LIST, "files", [])],
                "stop_positional_args_after_named": True,
            },
            "grep": {
                "named_args": {},
                "positional_args": [
                    Argument(Argument.STRING, "pattern", ""),
                    Argument(Argument.LIST, "files", []),
                ],
                "stop_positional_args_after_named": True,
            },
            "head": {
                "named_args": {
                    "n": Argument(Argument.FLAG_WITH_INTEGER, "lines", 10),
                },
                "positional_args": [Argument(Argument.STRING, "file", None)],
                "stop_positional_args_after_named": True,
            },
            "tail": {
                "named_args": {
                    "n": Argument(Argument.FLAG_WITH_INTEGER, "lines", 10),
                },
                "positional_args": [Argument(Argument.STRING, "file", None)],
                "stop_positional_args_after_named": True,
            },
            "find": {
                "named_args": {
                    "name": Argument(Argument.FLAG_WITH_STRING, "name", None),
                },
                "positional_args": [
                    Argument(Argument.STRING, "directory", ".")
                ],
                "stop_positional_args_after_named": True,
            },
            "uniq": {
                "named_args": {
                    "i": Argument(Argument.FLAG, "ignore_case", False)
                },
                "positional_args": [Argument(Argument.STRING, "file", None)],
                "stop_positional_args_after_named": True,
            },
            "sort": {
                "named_args": {
                    "r": Argument(Argument.FLAG, "reverse", False)
                },
                "positional_args": [Argument(Argument.STRING, "file", None)],
                "stop_positional_args_after_named": True,
            },
            "cut": {
                "named_args": {
                    "b": Argument(
                        Argument.FLAG_WITH_STRING, "bytes", ""
                    ),
                },
                "positional_args": [Argument(Argument.STRING, "file", None)],
                "stop_positional_args_after_named": True,
            },
        }

    def assign_arguments(self, command_name, args) -> dict:
        if command_name.startswith("_"):
            command_name = command_name[1:]
        if command_name not in self.default_arguments:
            raise UnknownCommandError(command_name)
        else:
            args_info = dict(self.default_arguments[command_name])

            Argument.populate_args(args_info, args)
            args_info = Argument.set_keys_to_readable(args_info)

            return args_info
