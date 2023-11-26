from src.commands.echo import EchoCommand
from src.commands.cd import CdCommand
from src.commands.pwd import PwdCommand
from src.commands.cat import CatCommand
from src.commands.ls import LsCommand
from src.commands.head import HeadCommand
from src.commands.tail import TailCommand
from src.commands.grep import GrepCommand
from src.commands.find import FindCommand
from src.commands.uniq import UniqCommand
from src.commands.sort import SortCommand


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
            "find": FindCommand
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