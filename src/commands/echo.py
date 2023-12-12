from .command import Command


class EchoCommand(Command):
    """
    Represents the 'echo' command which outputs text to stdout.

    This command mimics the behavior of the Unix 'echo' command. It outputs
    the provided text without directly appending a newline character at the
    end.
    """

    def __init__(self):
        super().__init__('echo', 'output text to stdout')

    def execute(self, args, input=None):
        """
        Executes the 'echo' command with the provided arguments.

        Args:
            args (dict): A dictionary containing command arguments. The
                         expected key is 'echo_text' for the text to echo.
            input (str, optional): Not used in this command.

        Returns:
            str: The text to be echoed, optionally without a trailing newline.
        """
        echo_text = ' '.join(args['echo_text'].value)
        return echo_text
