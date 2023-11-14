from .command import Command
import os

class LsCommand(Command):
    def __init__(self):
        super().__init__("ls", "list directory contents")

    def execute(self, args):
        directory = args['directory']
        if directory:
            directory = directory.value
        else:
            directory = os.getcwd()  # default to current directory if none is provided
        return "\n".join(os.listdir(directory))