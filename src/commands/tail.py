from .command import Command
import os

class TailCommand(Command):
    def __init__(self):
        super().__init__("tail", "display the last part of a file")

    def execute(self, args, input=None):
        if args['lines'].value < 0:
            raise ValueError("tail: illegal line count -- " + str(args['lines'].value))
        
        if args['file'].value is None:
            if input is None:
                raise ValueError("tail: missing file operand\nTry 'tail --help' for more information.")
            lines = input.split('\n')
        else:
            if not os.path.isfile(args['file'].value):
                raise FileNotFoundError("tail: " + args['file'].value + ": No such file or directory")
            with open(args['file'].value, "r") as file:
                lines = file.readlines()
        
        if len(lines) < args['lines'].value:
            return "".join(lines)
        else:
            return "".join(lines[-args['lines'].value:])
