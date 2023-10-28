from .command import Command
import os 
from os import listdir
import re

class Echo(Command):
    def __init__(self):
        super().__init__("echo", "output text to stdout")

    def execute(self, args):
        if args['trailing_newline']:
            print(args['echo_text'].arg_value)
        else:
            print(args['echo_text'].arg_value, end='')

    
        