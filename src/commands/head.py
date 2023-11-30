from .command import Command
import os

class HeadCommand(Command):
    def __init__(self):
        super().__init__("head", "display first lines of a file")

    def execute(self, args, input=None):
        if args['lines'].value < 0:
            raise ValueError("head: illegal line count -- " + str(args['lines'].value))
        
        if args['file'].value is None:
            if input is None:
                raise ValueError("head: missing file operand\nTry 'head --help' for more information.")
            lines = input.split('\n')
        else:
            if not os.path.isfile(args['file'].value):
                raise FileNotFoundError("head: " + args['file'].value + ": No such file or directory")
            with open(args['file'].value, "r") as file:
                lines = file.readlines()
        
        if len(lines) < args['lines'].value:
            return "\n".join(lines)
        else:
            return "\n".join(lines[:args['lines'].value])
