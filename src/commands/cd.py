from .command import Command
import os 
from os import listdir
import re

class CD(Comamnd):
    def __init__(self):
        super().__init__("cd", "change directory", ["<directory>"])

    def execute(self):
        os.chdir(self.args[0])
        