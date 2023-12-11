from .command import Command

class SortCommand(Command):
    """
    Represents the 'sort' command which sorts lines of text.

    This command mimics the behavior of the Unix 'sort' command. It can sort the lines in a file or
    provided input text, in ascending or descending order.
    """

    def __init__(self):
        super().__init__("sort", "sort lines")

    def execute(self, args, input=None):
        """
        Executes the 'sort' command with the provided arguments and optional input.

        Args:
            args (dict): A dictionary containing command arguments. Expected keys are 'reverse' for
                         sorting order and 'file' for the file path.
            input (str, optional): An optional string input to use when no file is provided.

        Returns:
            str: The sorted lines, concatenated into a single string.

        Raises:
            ValueError: If no file or input is provided.
        """
        reverse = args['reverse'].value
        file_path = args['file'].value

        lines = self._read_lines(file_path, input)
        lines.sort(reverse=reverse)

        return "\n".join(lines)

    def _read_lines(self, file_path, input):
        """
        Reads lines from a file or input string.

        Args:
            file_path (str): The file path to read from.
            input (str): The input string.

        Returns:
            list: A list of lines.

        Raises:
            ValueError: If neither a file nor input is provided.
        """
        if file_path:
            with open(file_path, 'r') as f:
                return f.read().splitlines()
        elif input:
            return input.split('\n')
        else:
            raise ValueError("sort: no input provided")
