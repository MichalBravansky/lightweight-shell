from .command import Command
import os
from pathlib import Path


class MkdirCommand(Command):
    """
    Command class for creating a new directory and subdirectories.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the MkdirCommand class.

        Args:
            None

        Returns:
            None
        """

        super().__init__("mkdir", "creates a new directory and subdirectories")

    def execute(self, args, input=None) -> None:
        """
        Executes the mkdir command to create directories.

        Args:
            args (dict): A dictionary containing the command arguments.
                create_subdirectories (bool): Flag indicating whether to
                                              create subdirectories.
                paths (list): List of paths to create directories.

            input (str, optional): Standard input string. Defaults to None.

        Raises:
            FileExistsError: If the path already exists.
            FileNotFoundError: If the parent directory does not exist and
                               create_subdirectories is False.

        Returns:
            None
        """

        create_subdirectories = args["create_subdirectories"].value
        paths = args["paths"].value

        for path in paths:

            if Path(path).exists():
                raise FileExistsError(f"mkdir: {path}: File exists.")

            if not Path(path).parent.exists():

                if create_subdirectories:
                    os.makedirs(path)
                else:
                    parent = Path(path).parent
                    raise FileNotFoundError(
                        f"mkdir: {parent}: No such parent directory."
                        )

            else:
                os.mkdir(path)
