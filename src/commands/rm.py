from .command import Command
import os
import shutil


class RmCommand(Command):
    """
    Represents the 'rm' command that removes files or directories.
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the 'rm' command class.
        """

        super().__init__("rm", "removes files or directories")

    def execute(self, args, input=None) -> None:
        """
        Executes the 'rm' command to remove files or directories.

        Args:
            args (dict): A dictionary containing the command arguments.
                'recursive' (bool): Indicates whether to remove files
                                    recursively.
                'paths' (list): A list of paths to be removed.
            input (str, optional): Input string. Not used in this method.

        Raises:
            FileNotFoundError: If the specified path does not exist.
            IsADirectoryError: If the specified path is a directory and
                               'remove_directory' is False.

        Returns:
            None
        """

        recursive_removal = args["recursive"].value
        paths = args["paths"].value

        for path in paths:
            if not os.path.exists(path):
                raise FileNotFoundError(
                    f"rm: {path}: No such file or directory."
                    )

            if os.path.isfile(path):
                os.remove(path)
            elif recursive_removal:
                shutil.rmtree(path)
            else:
                raise IsADirectoryError(
                    f"rm: {path} is a directory. Use -r to remove it."
                    )
