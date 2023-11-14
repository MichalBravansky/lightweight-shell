from .command import Command
import os

class LsCommand(Command):
    def __init__(self):
        super().__init__("ls", "list directory contents")

    def execute(self, args):
        directory = args['directory'].value
        return os.listdir(directory)