from shell_parser.executors.executor import Executor
from shell_parser.executors.call import Call
from itertools import chain


class Sequence(Executor):
    def __init__(self, left_executor: [Executor], right_executor: [Executor]) -> [str]:
        self._left_executor = left_executor
        self._right_executor = right_executor

    def _process_executor(self, executor: Executor, output: [str]) -> [str]:
        if executor:
            response = executor.evaluate()

            output += chain(response)

        return output

    def evaluate(self):
        output = []

        output = self._process_executor(self._left_executor, output)
        output = self._process_executor(self._right_executor, output)

        return [line for line in output if line]
