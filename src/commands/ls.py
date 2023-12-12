from .command import Command
import os


class LsCommand(Command):
    """
    Represents the 'ls' command which lists the contents of a directory.

    This command mimics the behavior of the Unix 'ls' command. It lists
    the files and directories within the specified directory.
    """

    def __init__(self):
        super().__init__('ls', 'list directory contents')

    def execute(self, args, input=None):
        """
        Executes the 'ls' command with the provided arguments.

        Args:
            args (dict): A dictionary containing command arguments. The
                         expected key is 'directory' for the directory whose
                         contents are to be listed.
            input (str, optional): Not used in this command.

        Returns:
            str: A newline-separated list of the contents of the
                 specified directory.

        Raises:
            FileNotFoundError: If the specified directory does not exist.
            NotADirectoryError: If the specified path is not a directory.
        """
        directory = args['directory'].value

        if not directory:
            directory = '.'

        if not os.path.exists(directory):
            raise FileNotFoundError(
                f'ls: {directory}: No such file or directory'
            )

        if not os.path.isdir(directory):
            raise NotADirectoryError(f'ls: {directory}: Not a directory')

        return '\n'.join(os.listdir(directory))
