from .command import Command

class SortCommand(Command):
    def __init__(self):
        super().__init__("sort", "sort lines")

    def execute(self, args, input=None):
        reverse = args['reverse'].value
        file = args['file'].value

        if file:
            with open(file, 'r') as f:
                lines = f.read().splitlines()
        elif input:
            lines = input.split('\n')
        else:
            raise ValueError("sort: no input provided")

        lines.sort(reverse=reverse)

        return "\n".join(lines)