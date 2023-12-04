import os
from .command import Command


class CatCommand(Command):
    def __init__(self):
        super().__init__("cat", "concatenate and print files")

    def execute(self, args, input=None):
        all_lines = []
        if not args["files"].value:
            if input is None:
                raise ValueError(
                    "cat: missing file operand\nTry 'cat --help' for more"
                    " information."
                )
            return input
        else:
            file_names = args["files"].value
        for file in file_names:
            if os.path.exists(file):
                with open(file, "r") as file:
                    lines = file.read().strip().split("\n")
                    all_lines += lines
            else:
                raise FileNotFoundError(
                    f"cat: {file}: No such file or directory"
                )
        return "\n".join(all_lines)
