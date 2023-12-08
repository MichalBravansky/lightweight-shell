from shell_parser.executors.executor import Executor
from shell_parser.executors.call import Call
import os
from enum import Enum


class RedirectionType(Enum):
    READ = 1
    OVERWRITE = 2
    APPEND = 3


class Redirect(Executor):
    def __init__(
        self, call: Call, redirect_type: RedirectionType, file_name: str
    ) -> None:
        super().__init__()

        self.call = call
        self.redirect_type = redirect_type
        self.file_contents = None
        self.file_name = file_name

        if redirect_type == RedirectionType.READ:
            if os.path.isfile(file_name):
                self.file_contents = open(file_name, "r").read()
            else:
                raise FileNotFoundError(
                    f"No such file or directory: {file_name}"
                )

    def evaluate(self, input: str = None) -> [str]:
        """
        Executes the command with the provided arguments and optional additional input.

        This method uses the CommandFactory to execute the command and returns the result.

        Args:
            input (str, optional): Additional input that may be required for command execution.
                                    Defaults to None.

        Returns:
            str: The output from the executed command.
        """
        if input:
            call_output = "".join(self.call.evaluate(input))
        elif self.file_contents:
            call_output = "".join(self.call.evaluate(self.file_contents))
        else:
            call_output = "".join(self.call.evaluate())

        if self.redirect_type == RedirectionType.OVERWRITE:
            open(self.file_name, "w").write(call_output)
            return [""]
        elif self.redirect_type == RedirectionType.APPEND:
            open(self.file_name, "a").write(call_output)
            return [""]
        elif self.redirect_type == RedirectionType.READ:
            return [call_output]
