from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command class is an abstract base class that represents a command that
    can be executed.

    Each command has a name and a description, which are set when the command
    is created.

    The execute method is an abstract method that must be implemented by any
    class that inherits from Command. This method is intended to be called
    with a list of arguments and an optional input argument. The exact
    behavior of the execute method will depend on the specific command.

    The 'pragma: no cover' comment on the execute method is a special
    instruction for coverage.py that tells it not to count this line when
    calculating code coverage, since this is an abstract method that is not
    meant to be directly tested.
    """

    def __init__(self, command_name: str, command_description: str) -> None:
        self.command_name = command_name
        self.command_description = command_description

    # Assumes that the command has been pre-validated by the parser.
    @abstractmethod
    def execute(self, args: dict, input: str =None) -> str:  # pragma: no cover
        raise NotImplementedError

    def help(self) -> None:
        print(f'{self.command_name}: {self.command_description}')
