from src.commands.echo import EchoCommand
from src.commands.cd import CdCommand
from src.commands.pwd import PwdCommand
from src.commands.cat import CatCommand
from src.commands.ls import LsCommand
from src.commands.head import HeadCommand
from src.commands.tail import TailCommand


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
        }

    def execute_command(self, command_name, args: list, input=None):
        command_class = self.classes.get(command_name.lower())
        if command_class is None:
            print(f"Unknown command: {command_name}")
            return
        else:
            command = command_class()
            return command.execute(args)