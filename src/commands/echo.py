from .command import Command

class EchoCommand(Command):
    """
    Represents the 'echo' command which outputs text to stdout.

    This command mimics the behavior of the Unix 'echo' command. It outputs the provided text
    and, by default, appends a newline character at the end unless specified otherwise.
    """

    def __init__(self):
        super().__init__("echo", "output text to stdout")

    def execute(self, args, input=None):
        """
        Executes the 'echo' command with the provided arguments.

        Args:
            args (dict): A dictionary containing command arguments. Expected keys are 'echo_text' for the
                         text to echo and 'exclude_trailing_newline' to indicate if the trailing newline
                         should be omitted.
            input (str, optional): Not used in this command.

        Returns:
            str: The text to be echoed, optionally without a trailing newline.
        """
        echo_text = " ".join(args["echo_text"].value)
        return echo_text if args["exclude_trailing_newline"].value else echo_text + "\n"
