from .command import Command
import os


class HeadCommand(Command):
    """
    Represents the 'head' command which is used to display the first lines of a file.

    The command mimics the behavior of the Unix 'head' command. It can either take a file as an
    argument and print its first few lines, or it can work with an input string if no file is provided.
    """

    def __init__(self):
        super().__init__('head', 'display first lines of a file')

    def execute(self, args, input=None):
        """
        Executes the 'head' command with the provided arguments and optional input.

        Args:
            args (dict): A dictionary containing command arguments. Expected keys are 'lines' for the
                         number of lines to display and 'file' for the file path.
            input (str, optional): An optional string input to use when no file is provided.

        Returns:
            str: The first few lines of the file or input string.

        Raises:
            ValueError: If the line count is negative or if no file or input is provided.
            FileNotFoundError: If the provided file path does not exist.
        """
        self._validate_args(args)

        lines = self._get_lines(args, input)
        return '\n'.join(lines[: min(args['lines'].value, len(lines))])

    def _validate_args(self, args):
        """
        Validates the command arguments.

        Args:
            args (dict): The command arguments to validate.

        Raises:
            ValueError: If the line count is negative.
        """
        if args['lines'].value < 0:
            raise ValueError(
                f"head: illegal line count -- {args['lines'].value}"
            )

    def _get_lines(self, args, input):
        """
        Gets the lines from the file or input string.

        Args:
            args (dict): The command arguments.
            input (str): The input string.

        Returns:
            list: A list of lines.

        Raises:
            ValueError: If no file operand is provided and input is None.
            FileNotFoundError: If the file does not exist.
        """
        if args['file'].value is None:
            return self._get_lines_from_input(input)
        else:
            return self._get_lines_from_file(args['file'].value)

    def _get_lines_from_input(self, input):
        """
        Gets lines from the input string.

        Args:
            input (str): The input string.

        Returns:
            list: A list of lines.

        Raises:
            ValueError: If input is None.
        """
        if input is None:
            raise ValueError(
                "head: missing file operand\nTry 'head --help' for more"
                ' information.'
            )
        return input.split('\n')

    def _get_lines_from_file(self, file_path):
        """
        Reads lines from a file.

        Args:
            file_path (str): The path of the file to read.

        Returns:
            list: A list of lines.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(
                f'head: {file_path}: No such file or directory'
            )
        with open(file_path, 'r') as file:
            return file.read().split('\n')
