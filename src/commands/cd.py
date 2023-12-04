from .command import Command
import os


class CdCommand(Command):
    def __init__(self):
        super().__init__("cd", "change directory")

    def execute(self, args, input=None):
        cd_path = args["cd_path"].value
        if os.path.exists(cd_path) and os.path.isdir(cd_path):
            os.chdir(cd_path)
        else:
            raise FileNotFoundError(f"cd: {cd_path}: No such directory")
