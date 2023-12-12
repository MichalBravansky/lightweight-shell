from shell_parser.executors import Executor


class UnsafeDecorator:
    """
    The UnsafeDecorator class is a decorator for the Executor class that 
    catches exceptions raised during command execution and returns 
    an error message.

    This class overrides the evaluate method from the Executor class. 
    When the evaluate method is called, it tries to call the evaluate method of the decorated Executor object. 
    If an exception is raised during the execution of the command, the evaluate method catches the exception and returns an error message.

    The error message includes the type of the exception and its arguments, which provide information about the error.
    """


    def __init__(self, executor: Executor) -> None:
        self._executor = executor

    def evaluate(self, input: str = None) -> [str]:
        try:
            return self._executor.evaluate(input)
        except Exception as e:
            return [f"Error while processing shell: {str(e)}"]
