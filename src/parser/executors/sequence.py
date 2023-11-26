from src.parser.executors.executor import Executor
from src.parser.executors.call import Call


class Sequence(Executor):
    def __init__(self, calls: [Call]) -> None:
        self.calls = calls

    def evaluate(self):
        output = []
        for call in self.calls:
            output.append(call.evaluate())
        return "".join(output)
