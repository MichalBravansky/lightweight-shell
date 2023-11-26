from .command import Command
import os 
from os import listdir
import re

class EchoCommand(Command):
    def __init__(self):
        super().__init__("echo", "output text to stdout")

    def execute(self, args, input = None):
        echo_text = " ".join(args['echo_text'].value) + input if input is not None else args['echo_text'].value
        if args['exclude_trailing_newline'].value:
            return echo_text
        else:
            return echo_text + "\n"

    
        