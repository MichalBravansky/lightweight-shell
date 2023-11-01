from .command import Command
import os

class PwdCommand(Command):
    def __init__(self):
        super().__init__("pwd", "print working directory")

    def execute(self, args, input=None):
        return os.getcwd() + "\n"