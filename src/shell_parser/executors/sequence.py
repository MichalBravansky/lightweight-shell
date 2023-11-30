from shell_parser.executors.executor import Executor
from shell_parser.executors.call import Call


class Sequence(Executor):
    def __init__(self, calls: [Call]) -> None:
        self.calls = calls

    def evaluate(self):
        output = []
        for call in self.calls:
            evaluate_result = call.evaluate()
            if evaluate_result is not None:
                output.append(evaluate_result)
        return "".join(output)
