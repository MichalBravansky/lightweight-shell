from .command import Command
import os 
from os import listdir
import re

class EchoCommand(Command):
    def __init__(self):
        super().__init__("echo", "output text to stdout")

    def execute(self, args):
        named_args = args['named_arguments']
        positional_args = args['positional_arguments']
        echo_text = " ".join(args['positional_arguments'][0].value)
        if named_args['exclude_trailing_newline'].value:
            print(echo_text, end='')
        else:
            print(echo_text)

    
        