from .command import Command
import os
import fnmatch


class FindCommand(Command):
    """
    Represents the 'find' command which walks a file hierarchy.

    This command mimics the behavior of the Unix 'find' command. It searches for files that match a
    given pattern starting from a specified directory.
    """

    def __init__(self):
        super().__init__('find', 'walk a file hierarchy')

    def execute(self, args: dict, input: str = None) -> str:
        """
        Executes the 'find' command with the provided arguments.

        Args:
            args (dict): A dictionary containing command arguments. Expected keys are 'directory' for the
                         starting directory and 'name' for the search pattern.
            input (str, optional): Not used in this command.

        Returns:
            str: The newline-separated list of found files.

        Raises:
            ValueError: If the specified directory is invalid or no search pattern is specified.
        """
        directory = self._get_search_directory(args)
        pattern = self._get_search_pattern(args)

        return '\n'.join(self._find_files(directory, pattern)) + '\n'

    def _get_search_directory(self, args: dict) -> str:
        """
        Retrieves the search directory from the arguments.

        Args:
            args (dict): The command arguments.

        Returns:
            str: The directory to start the search from.

        Raises:
            ValueError: If the specified directory is invalid.
        """
        directory = args['directory'].value or '.'
        if not os.path.isdir(directory):
            raise ValueError(f'find: Invalid directory: {directory}')
        return directory

    def _get_search_pattern(self, args: dict) -> str:
        """
        Retrieves the search pattern from the arguments.

        Args:
            args (dict): The command arguments.

        Returns:
            str: The search pattern.

        Raises:
            ValueError: If no search pattern is specified.
        """
        pattern = args['name'].value
        if pattern is None:
            raise ValueError('find: No search pattern specified')
        return pattern

    def _find_files(self, directory: str, pattern: str) -> [str]:
        """
        Finds files matching the pattern starting from the specified directory.

        Args:
            directory (str): The starting directory.
            pattern (str): The search pattern.

        Returns:
            list: A list of paths to the found files.
        """
        found_files = []
        for root, _, files in os.walk(directory, topdown=True):
            for file in files:
                if fnmatch.fnmatch(file, pattern) or pattern == '*':
                    found_files.append(os.path.join(root, file))
        return found_files
