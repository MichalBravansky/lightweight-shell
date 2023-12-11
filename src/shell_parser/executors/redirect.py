from shell_parser.executors.executor import Executor
from shell_parser.executors.call import Call
import os
from enum import Enum


class RedirectionType(Enum):
    READ = 1
    OVERWRITE = 2
    APPEND = 3


class Redirect(Executor):
    """
    This class represents a redirection in shell command execution,
    handling the redirection of a command's output to a file or using a file's contents as input.

    It inherits from the Executor class and overrides the evaluate method to implement redirection.
    """
        
    def __init__(self, call: Call, redirect_type: RedirectionType, file_name: str) -> None:
        """
        Initializes a new instance of the Redirect class.

        Args:
            call (Call): The call executor representing the command to be executed.
            redirect_type (RedirectionType): The type of redirection (READ, OVERWRITE, or APPEND).
            file_name (str): The name of the file to redirect to/from.

        Raises:
            FileNotFoundError: If the redirect type is READ and the file does not exist.
        """

        super().__init__()

        self.call = call
        self.redirect_type = redirect_type
        self.file_name = file_name

    def evaluate(self, input: str = None) -> [str]:
        """
        Executes the redirection process based on the specified redirection type.

        This method manages the flow of data either to the file (in case of OVERWRITE or APPEND)
        or from the file (in case of READ) and executes the associated command.

        Args:
            input (str, optional): Additional input that functions as standard input for the command.
                                    Defaults to None.

        Returns:
            [str]: The output from the executed command or an empty list if the output is redirected to a file.
        """

        file_contents = None

        if self.redirect_type == RedirectionType.READ:
            if os.path.isfile(self.file_name):
                with open(self.file_name, "r") as file:
                    file_contents = file.read()
            else:
                raise FileNotFoundError(
                    f"No such file or directory: {self.file_name}"
                )

        call_input = input or file_contents or None
        call_output = "".join(self.call.evaluate(call_input))

        if self.redirect_type in (RedirectionType.OVERWRITE, RedirectionType.APPEND):
            
            mode = "w" if self.redirect_type == RedirectionType.OVERWRITE else "a"
            with open(self.file_name, mode) as file:
                file.write(call_output)

            return [""]
        
        elif self.redirect_type == RedirectionType.READ:
            return [call_output]
