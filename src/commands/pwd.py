from .command import Command
import os


class PwdCommand(Command):
    """
    Represents the 'pwd' command which prints the current working directory.

    This command mimics the behavior of the Unix 'pwd' command. It displays the path of the
    current working directory.
    """

    def __init__(self):
        super().__init__("pwd", "print working directory")

    def execute(self, args, input=None):
        """
        Executes the 'pwd' command.

        Args:
            args (dict): Not used in this command.
            input (str, optional): Not used in this command.

        Returns:
            str: The current working directory followed by a newline character.
        """
        return os.getcwd()
