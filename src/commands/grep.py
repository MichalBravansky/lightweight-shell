from .command import Command
import os
import re
from commands.argument import Argument


class GrepCommand(Command):
    """
    Represents the 'grep' command which is used for file pattern search.

    This command mimics the behavior of the Unix 'grep' command.
    It searches for a specified pattern (regular expression)
    in a file or a given input string and outputs the matching lines.
    """

    def __init__(self):
        super().__init__('grep', 'file pattern search')

    def process_input(self, pattern: re.Pattern, text_input: str,
                      prefix: str = '') -> [str]:
        """
        Processes the input text to find lines that match the given pattern.

        Args:
            pattern (re.Pattern): The compiled regular expression pattern to
            search for.
            text_input (str): The text to search within.
            prefix (str): Optional prefix to add to each matching line.

        Returns:
            list: A list of matching lines, each optionally prefixed.
        """
        output = []
        for line in text_input.split('\n'):
            if pattern.search(line):
                output.append(prefix + line)
        return output

    def execute(self, args: dict, input: str = None) -> str:
        """
        Executes the 'grep' command with the provided arguments
        and optional input.

        Args:
            args (dict): A dictionary containing command arguments.
                         Expected keys are 'pattern' for the
                         regular expression to match and 'files' for the list
                         of files to search in.
            input (str, optional): An optional string input to use when
            no file is provided.

        Returns:
            str: The concatenated matching lines from all processed inputs.

        Raises:
            ValueError: If no file or input is provided.
            FileNotFoundError: If a provided file path does not exist
            or is not a file.
        """
        pattern = re.compile(args['pattern'].value)
        files = args['files']
        prefix_file_path = len(files.value) > 1

        if not files.value:
            return self._process_input_no_file(pattern, input)

        return self._process_input_files(pattern, files, prefix_file_path)

    def _process_input_no_file(self, pattern: re.Pattern, input: str) -> str:
        """
        Processes input when no file is provided.

        Args:
            pattern (re.Pattern): The compiled regular expression pattern.
            input (str): The input string.

        Returns:
            str: The concatenated matching lines.

        Raises:
            ValueError: If input is None.
        """
        if input is None:
            raise ValueError("grep: missing file operand\nTry 'grep --help'.")
        return '\n'.join(self.process_input(pattern, input))

    def _process_input_files(self, pattern: re.Pattern, files: [Argument],
                             prefix_file_path: bool) -> str:
        """
        Processes input from files.

        Args:
            pattern (re.Pattern): The compiled regular expression pattern.
            files (list(Argument)): The file arguments.
            prefix_file_path (bool): Whether to prefix file paths to output
            lines.

        Returns:
            str: The concatenated matching lines from all files.

        Raises:
            FileNotFoundError: If a file does not exist.
        """
        output = []
        for file_arg in files.value:
            if os.path.exists(file_arg) and os.path.isfile(file_arg):
                with open(file_arg, 'r') as file:
                    file_content = file.read()
                file_name = (file_arg + ':') if prefix_file_path else ''
                output += self.process_input(pattern, file_content, file_name)
            else:
                raise FileNotFoundError(f'grep: {file_arg}: No such file.')
        return '\n'.join(output)
