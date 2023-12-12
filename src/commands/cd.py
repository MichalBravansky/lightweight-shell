from .command import Command
import os


class CdCommand(Command):
    """
    Represents the 'cd' command which changes the current working directory.

    This command mimics the behavior of the Unix 'cd' command. It changes the current working
    directory of the running Python process. Note that this affects the entire process.
    """

    def __init__(self):
        super().__init__('cd', 'change directory')

    def execute(self, args: dict, input: str = None) -> None:
        """
        Executes the 'cd' command with the provided arguments.

        Args:
            args (dict): A dictionary containing command arguments. Expected key is 'cd_path' for the
                         directory path to change to.
            input (str, optional): Not used in this command.

        Raises:
            NotADirectoryError: If the specified directory does not exist or is not a directory.
        """
        cd_path = args['cd_path'].value
        self._change_directory(cd_path)

    def _change_directory(self, cd_path):
        """
        Changes the current working directory.

        Args:
            cd_path (str): The path of the directory to change to.

        Raises:
            NotADirectoryError: If the specified directory does not exist or is not a directory.
        """
        if os.path.exists(cd_path) and os.path.isdir(cd_path):
            os.chdir(cd_path)
        else:
            raise NotADirectoryError(f'cd: {cd_path}: No such directory')
