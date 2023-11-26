from .command import Command
import os
import fnmatch

class FindCommand(Command):
    def __init__(self):
        super().__init__("find", "walk a file hierarchy")

    def execute(self, args, input=None):
        directory = args['directory'].value if args['directory'].value else "."
        pattern = args['name'].value

        if not os.path.isdir(directory):
            raise ValueError(f"find: Invalid directory: {directory}")

        if pattern is None:
            raise ValueError("find: No search pattern specified")

        found_files = []

        for root, _, files in os.walk(directory, topdown=True):
            for file in files:
                if fnmatch.fnmatch(file, pattern) or pattern == "*":
                    found_files.append(os.path.join(root, file))

        return "\n".join(found_files) + "\n"
