from shell_parser.executors.executor import Executor
from commands.commandFactory import CommandFactory
from handler.argumentHandler import ArgumentHandler


class UnsafeCall(Call):
    """
    An unsafe version of the Call class that returns the error message if the command fails.
    """

    def __init__(self, command: str, args: [str]) -> None:
        """
        Initializes a new instance of the UnsafeCall class.

        Args:
            command (str): The command to be executed.
            args ([str]): A list of arguments for the command.
        """
        super().__init__(command, args)

    def evaluate(self, input: str = None) -> str:
        """
        Executes the command with the provided arguments and optional additional input.

        This method uses the CommandFactory to execute the command and returns the result or the error message.

        Args:
            input (str, optional): Additional input that may be required for command execution.
                                    Defaults to None

        Returns:
            str: The output from the executed command or the error message if the command fails.
        """
        try:
            return super.evaluate(input)
        except Exception as e:
            return str(e)
