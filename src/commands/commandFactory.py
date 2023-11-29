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
        unsafe_mode = False
        if command_name.startswith("_"):
            print(command_name)
            command_name = command_name[1:]
            unsafe_mode = True
        command_class = self.classes.get(command_name.lower())
        if command_class is None:
            print(f"Unknown command: {command_name}")
            return
        else:
            command = command_class()
            if unsafe_mode:
                try:
                    return command.execute(args, input)
                except Exception as e:
                    return str(e)
            else:
                return command.execute(args, input)
