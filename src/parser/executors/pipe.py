from src.parser.executors.executor import Executor
from src.parser.executors.call import Call


class Pipe(Executor):
    def __init__(self, calls: [Call]) -> None:
        self.calls = calls

    def evaluate(self):
        input = None
        for call in reversed(self.calls):
            input = call.evaluate(input)
        return input
