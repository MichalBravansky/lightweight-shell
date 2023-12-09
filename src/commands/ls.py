from .command import Command
import os


class LsCommand(Command):
    def __init__(self):
        super().__init__("ls", "list directory contents")

    def execute(self, args, input=None):
        directory = args["directory"].value
        return "\n".join(os.listdir(directory))
