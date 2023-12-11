from shell_parser.executors import Executor


class UnsafeDecorator():

    def __init__(self, executor: Executor) -> None:
        
        self._executor = executor

    def evaluate(self, input: str = None) -> [str]:

        try:
            return self._executor.evaluate(input)
        except Exception as e:
            return [f"Error while processing shell: {str(e)}"]
