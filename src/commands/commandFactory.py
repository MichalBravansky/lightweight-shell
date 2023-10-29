from src.commands.echo import EchoCommand
from src.commands.cd import CdCommand


class CommandFactory:
    def __init__(self) -> None:
        self.classes = {
            "echo": EchoCommand,
            "cd": CdCommand,
        }

    def execute_command(self, command_name, args: list):
        command_class = self.classes.get(command_name.lower())
        if command_class is None:
            print(f"Unknown command: {command_name}")
        else:
            command = command_class()
            return command.execute(args)
