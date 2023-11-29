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


class CommandFactory:
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
        }

    def execute_command(self, command_name, args: list, input=None):
        command_class = self.classes.get(command_name.lower())
        if command_class is None:
            print(f"Unknown command: {command_name}")
            return
        else:
            command = command_class()
            return command.execute(args, input)