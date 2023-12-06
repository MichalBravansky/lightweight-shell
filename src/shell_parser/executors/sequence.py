from shell_parser.executors.executor import Executor
from shell_parser.executors.call import Call
from itertools import chain


class Sequence(Executor):
    def __init__(self, left_executor: [Executor], right_executor: [Executor]) -> None:
        self._left_executor = left_executor
        self._right_executor = right_executor

    def _process_executor(self, executor: Executor, output: [str]) -> [str]:
        if executor:
            response = executor.evaluate()

            if isinstance(response, list):
                output += chain(response)
            elif response:
                output.append(response)

        return output

    def evaluate(self):
        output = []

        output = self._process_executor(self._left_executor, output)
        output = self._process_executor(self._right_executor, output)

        return "".join(output)
