from .command import Command
import os

class UniqCommand(Command):
    def __init__(self):
        super().__init__("uniq", "remove duplicate lines")

    def execute(self, args):
        ignore_case = args['ignore_case'].value
        file = args['file'].value
        previous_line = None
        result = []
        
        if file:
            with open(file, 'r') as f:
                lines = f.readlines()
        else:
            lines = input().split('\n')

        for line in lines:
            if ignore_case:
                if previous_line is None or line.lower() != previous_line.lower():
                    result.append(line)
                    previous_line = line
            else:
                if line != previous_line:
                    result.append(line)
                    previous_line = line

        return "\n".join(result)