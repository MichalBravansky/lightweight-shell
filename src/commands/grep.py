from .command import Command
import os
import re
import sys


class GrepCommand(Command):
    def __init__(self):
        super().__init__("grep", "file pattern search")

    def process_input(self, pattern, text_input, prefix=""):
        output = []
        for line in text_input.split('\n'):
            if pattern.search(line):
                output.append(prefix + line)
        return output

    def execute(self, args, input=None):
        output = []
        pattern = re.compile(args["pattern"].value)
        files = args['files']
        prefix_file_path = len(files.value) > 1
        if len(files.value) == 0:
            if input is None:
                raise ValueError("grep: missing file operand\nTry 'grep --help' for more information.")
            output += self.process_input(pattern, input)
        else:
            for file_arg in files.value:
                if os.path.exists(file_arg) and os.path.isfile(file_arg):
                    with open(file_arg, 'r') as file:
                        file_content = file.read()
                    file_name = (file_arg + ":") if prefix_file_path else ""
                else:
                    raise FileNotFoundError(f"grep: {file_arg}: No such file.")
                
                output += self.process_input(pattern, file_content, file_name)
        return "\n".join(output)