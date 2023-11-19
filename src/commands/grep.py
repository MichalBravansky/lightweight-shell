from .command import Command
import os
import re
import sys


class GrepCommand(Command):
    def __init__(self):
        super().__init__("grep", "file pattern search")

    def execute(self, args):
        pattern = re.compile(args["pattern"].value)
        files = args.get("files", [{"value": None}])
        prefix_file_path = len(files) > 1
        for file_arg in files:
            if file_arg.value is None:
                file = sys.stdin
                file_name = ""
            elif os.path.exists(file_arg.value) and os.path.isfile(file_arg.value):
                file = open(file_arg.value, 'r')
                file_name = (file_arg.value + ": ") if prefix_file_path else ""
            else:
                print(file_arg.value + ": No such file or directory")
                continue
            lines = file.readlines()
            for line in lines:
                if pattern.search(line):
                    print(file_name + line, end='')
            if file is not sys.stdin:
                file.close()