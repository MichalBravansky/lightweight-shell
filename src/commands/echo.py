from .command import Command


class EchoCommand(Command):
    def __init__(self):
        super().__init__("echo", "output text to stdout")

    def execute(self, args, input=None):
        echo_text = " ".join(args["echo_text"].value)
        if args["exclude_trailing_newline"].value:
            return echo_text
        else:
            return echo_text + "\n"
