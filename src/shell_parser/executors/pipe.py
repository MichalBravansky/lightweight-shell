from shell_parser.executors.executor import Executor
from shell_parser.executors.call import Call


class Pipe(Executor):
    def __init__(self, calls: [Call]) -> None:
        self.calls = calls

    def evaluate(self):
        input = ""
        for call in self.calls:
            input = call.evaluate(input)
        return input
