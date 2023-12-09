from shell_parser.executors.executor import Executor
from shell_parser.executors.call import Call
from itertools import chain


class Sequence(Executor):
    """
    This class represents a sequence of executions in shell command processing,
    allowing for the execution of multiple commands in a specified order.

    It inherits from the Executor class and overrides the evaluate method
    to implement sequential execution of commands.
    """
        
    def __init__(self, left_executor: Executor, right_executor: Executor) -> None:
        """
        Initializes a new instance of the Sequence class.

        Args:
            left_executor (Executor): The first executor in the sequence.
            right_executor (Executor): The second executor in the sequence.
        """
                
        self._left_executor = left_executor
        self._right_executor = right_executor


    def _process_executor(self, executor: Executor, output: [str]) -> [str]:
        """
        Processes an individual executor and appends its output to the existing output list.

        This helper method is used within the evaluate method to process each executor in the sequence.

        Args:
            executor (Executor): The executor to be processed.
            output ([str]): The current list of output lines to which the executor's output will be appended.

        Returns:
            [str]: The updated list of output lines after processing the given executor.
        """
                
        if executor:
            response = executor.evaluate()

            output += chain(response)

        return output

    def evaluate(self):
        """
        Executes the sequence of commands represented by the left and right executors.

        This method processes each executor in the sequence and compiles their outputs in order.

        Returns:
            [str]: The combined output from both executors in the sequence, with empty lines filtered out.
        """
                
        output = []

        output = self._process_executor(self._left_executor, output)
        output = self._process_executor(self._right_executor, output)

        return [line for line in output if line]
