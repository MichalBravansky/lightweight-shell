from .command import Command

class SortCommand(Command):
    def __init__(self):
        super().__init__("sort", "sort lines")

    def execute(self, args):
        reverse = args['reverse'].value
        file = args['file'].value

        if file:
            with open(file, 'r') as f:
                lines = f.readlines()
        else:
            lines = input().split('\n')

        lines.sort(reverse=reverse)

        return "\n".join(lines)