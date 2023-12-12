from .command import Command
import os


class ClearCommand(Command):
    """
    Represents a command that clears the terminal screen.
    """

    def __init__(self) -> None:
        """
        Initializes the ClearCommand object.
        """

        super().__init__("clear", "clears the terminal screen")

    def execute(self, args, input=None) -> None:
        """
        Executes the 'clear' command, which clears the terminal screen.

        Args:
            args (list): List of command arguments.
            input (str, optional): Standard input string. Defaults to None.
        """

        os.system("cls" if os.name == "nt" else "clear")
