import os
from .command import Command


class CatCommand(Command):
    """
    Represents the 'cat' command which concatenates and prints files.

    This command mimics the Unix 'cat' command. It concatenates the contents of one or more files
    and prints them. If no file is provided, it can return an input string.
    """

    def __init__(self):
        super().__init__("cat", "concatenate and print files")

    def execute(self, args, input=None):
        """
        Executes the 'cat' command with the provided arguments and optional input.

        Args:
            args (dict): A dictionary containing command arguments. Expected key is 'files' for the
                         list of files to concatenate.
            input (str, optional): An optional string input to use when no file is provided.

        Returns:
            str: The concatenated contents of the files or the input string.

        Raises:
            ValueError: If no file or input is provided.
            FileNotFoundError: If any of the provided file paths does not exist.
        """
        if not args["files"].value:
            return self._handle_no_file_provided(input)
        return self._concatenate_files(args["files"].value)

    def _handle_no_file_provided(self, input):
        """
        Handles the case when no file is provided to the command.

        Args:
            input (str): The input string.

        Returns:
            str: The input string.

        Raises:
            ValueError: If input is None.
        """
        if input is None:
            raise ValueError(
                "cat: missing file operand\nTry 'cat --help' for more"
                " information."
            )
        return input

    def _concatenate_files(self, file_names):
        """
        Concatenates the contents of provided files.

        Args:
            file_names (list): List of file paths to concatenate.

        Returns:
            str: The concatenated file contents.

        Raises:
            FileNotFoundError: If any of the files does not exist.
        """
        all_lines = []
        for file_name in file_names:
            if os.path.exists(file_name):
                with open(file_name, "r") as file:
                    lines = file.read().strip().split("\n")
                    all_lines += lines
            else:
                raise FileNotFoundError(
                    f"cat: {file_name}: No such file or directory"
                )
        return "\n".join(all_lines)
