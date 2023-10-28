from .command import Command
import os 
from os import listdir
import re

class CD(Command):
    def __init__(self):
        super().__init__("cd", "change directory")

    def execute(self, args):
        os.chdir(args["file_path"])
    
        