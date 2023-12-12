from shell_parser.executors.executor import Executor


class Pipe(Executor):
    """
    This class represents a pipe mechanism in shell command execution,
    allowing for the output of one command (left_executor) to be passed as input
    to another command (right_executor).

    It inherits from the Executor class and overrides the evaluate method
    to implement the piping functionality.
    """

    def __init__(
        self, left_executor: [Executor], right_executor=[Executor]
    ) -> [str]:
        """
        Initializes a new instance of the Pipe class.

        Args:
            left_executor (Executor): The executor that represents the command on the left side of the pipe.
            right_executor (Executor): The executor that represents the command on the right side of the pipe.
        """

        self._left_executor = left_executor
        self._right_executor = right_executor

    def evaluate(self, input: str = None):
        """
        Executes the piping process between the left and right executors.

        The output of the left executor is used as input for the right executor.
        If either executor is missing, it bypasses that part of the process.

        Args:
            input (str, optional): Initial input that may be required for the first command execution.
                                    Defaults to None.

        Returns:
            [str]: The output from the right executor after processing the piped input.
        """

        if self._left_executor:
            input = ''.join(self._left_executor.evaluate(input))

        if self._right_executor:
            input = ''.join(self._right_executor.evaluate(input))

        return [input]
