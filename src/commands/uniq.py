from .command import Command


class UniqCommand(Command):
    """
    Represents the 'uniq' command which removes duplicate consecutive lines from text.

    This command mimics the behavior of the Unix 'uniq' command. It can process lines from a file or
    from provided input text, and outputs unique lines. It has an option to ignore case while
    comparing lines.
    """

    def __init__(self):
        super().__init__('uniq', 'remove duplicate lines')

    def execute(self, args, input=None):
        """
        Executes the 'uniq' command with the provided arguments and optional input.

        Args:
            args (dict): A dictionary containing command arguments. Expected keys are 'ignore_case' to
                         indicate whether to ignore case in comparisons, and 'file' for the file path.
            input (str, optional): An optional string input to use when no file is provided.

        Returns:
            str: The unique lines, concatenated into a single string.

        Raises:
            ValueError: If no file or input is provided.
        """
        ignore_case = args['ignore_case'].value
        file_path = args['file'].value

        lines = self._read_lines(file_path, input)
        return '\n'.join(self._remove_duplicates(lines, ignore_case))

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
        elif input is not None:
            return input.splitlines()
        else:
            raise ValueError(
                "uniq: missing file operand\nTry 'uniq --help' for more"
                ' information.'
            )

    def _remove_duplicates(self, lines, ignore_case):
        """
        Removes duplicate consecutive lines from the list of lines.

        Args:
            lines (list of str): The lines to process.
            ignore_case (bool): Whether to ignore case in comparisons.

        Returns:
            list: A list of unique lines.
        """
        unique_lines = []
        previous_line = None

        for line in lines:
            comparison_line = line.lower() if ignore_case else line
            if comparison_line != previous_line:
                unique_lines.append(line)
                previous_line = comparison_line

        return unique_lines
