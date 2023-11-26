from .command import Command
import os 
from os import listdir
import re

class CdCommand(Command):
    def __init__(self):
        super().__init__("cd", "change directory")

    def execute(self, args):
        if os.path.exists(args["cd_path"].value) and os.path.isdir(args["cd_path"].value):
            os.chdir(args["cd_path"].value)
        else:
            raise FileNotFoundError(f"cd: {args['cd_path'].value}: No such directory")
    
        