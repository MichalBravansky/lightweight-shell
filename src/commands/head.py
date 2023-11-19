from .command import Command
import os

class HeadCommand(Command):
    def __init__(self):
        super().__init__("head", "display first lines of a file")

    def execute(self, args, input=None):
        if args['lines'].value < 0:
            return "head: illegal line count -- " + str(args['lines'].value) + "\n"
        if args['file'].value is None:
            if input is None:
                return "head: missing file operand\nTry 'head --help' for more information.\n"
            lines = input.split('\n')
        else:
            if not os.path.isfile(args['file'].value):
                return "head: " + args['file'].value + ": No such file or directory\n"
            file = open(args['file'].value, "r")
            lines = file.readlines()
            file.close()
        
        if len(lines) < args['lines'].value:
            return "".join(lines)
        else:
            return "".join(lines[:args['lines'].value])