from commands.echo import EchoCommand
from commands.cd import CdCommand
from commands.pwd import PwdCommand
from commands.cat import CatCommand
from commands.ls import LsCommand
from commands.head import HeadCommand
from commands.tail import TailCommand
from commands.grep import GrepCommand
from commands.find import FindCommand
from commands.uniq import UniqCommand
from commands.sort import SortCommand
from commands.cut import CutCommand
from commands.rm import RmCommand
from commands.clear import ClearCommand
from commands.mkdir import MkdirCommand
from utils.exceptions import UnknownCommandError


class CommandFactory:
    """
    The CommandFactory class is responsible for creating Command objects based on a given command name.

    The create method takes a command name as an argument and returns a new instance of the corresponding Command subclass.
    If the command name is not recognized, the create method raises a ValueError.

    The CommandFactory uses a dictionary to map command names to Command subclasses.
    When the create method is called with a command name,
    the CommandFactory looks up the corresponding Command subclass in the dictionary and instantiates it.
    If the command name is not found in the dictionary, the create method raises a ValueError.
    """

    def __init__(self) -> None:
        self.classes = {
            "echo": EchoCommand,
            "cd": CdCommand,
            "pwd": PwdCommand,
            "cat": CatCommand,
            "ls": LsCommand,
            "head": HeadCommand,
            "tail": TailCommand,
            "grep": GrepCommand,
            "uniq": UniqCommand,
            "sort": SortCommand,
            "find": FindCommand,
            "cut": CutCommand,
            "rm": RmCommand,
            "clear" : ClearCommand,
            "mkdir": MkdirCommand
        }

    def execute_command(self, command_name, args: list, input=None):
        command_class = self.classes.get(command_name.lower())
        if command_class is None:
            raise UnknownCommandError(command_name)
        else:
            command = command_class()
            return command.execute(args, input)
