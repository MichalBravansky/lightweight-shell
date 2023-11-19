from src.parser.executors.executor import Executor, Call

class Pipe(Executor):
    def __init__(self, calls: [Call]) -> None:
        self.calls = calls

    def execute(self):
        input = None
        for call in reversed(self.calls):
            input = call.evaluate(input)
        return input
        
        