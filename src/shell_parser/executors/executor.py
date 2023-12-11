from abc import ABC, abstractmethod


class Executor(ABC):
    """
    An abstract base class representing an executor.

    This class serves as a template for concrete executor classes, which are responsible for
    executing specific tasks or commands. It defines the basic structure and ensures that
    all subclasses implement the core functionality defined by the `evaluate` method.
    """

    @abstractmethod
    def evaluate(self, input: str = None) -> [str]: # pragma: no cover
        """
        Abstract method to execute a task or command.

        Args:
            input (str, optional): Additional input that may be required for the execution.
                                   Defaults to None.

        Returns:
            str: The output or result of the execution.
        """
        raise NotImplementedError()
