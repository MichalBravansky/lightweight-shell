from shell_parser.executors.executor import Executor
from shell_parser.executors.call import Call


class Pipe(Executor):
    def __init__(self, left_executor: [Executor], right_executor=[Executor]) -> None:
        self._left_executor = left_executor
        self._right_executor = right_executor

    def evaluate(self, input: str = None):
        if self._left_executor:
            input = self._left_executor.evaluate(input)

        if self._right_executor:
            input = self._right_executor.evaluate(input)

        return input
