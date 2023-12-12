from config import config
from utils.exceptions import UnknownCommandError
from commands.argument import Argument


class ArgumentHandler:
    @classmethod
    def assign_arguments(cls, command_name: str, args: list) -> dict:
        """
        Assign the arguments to the specified command.

        Args:
            command_name (str): The name of the command.
            args (list): The list of arguments.

        Returns:
            dict: The assigned arguments.

        Raises:
            UnknownCommandError: If the command is not found in the configuration.
        """
        if not config.is_command(command_name):
            raise UnknownCommandError(command_name)
        else:
            args_info = dict(config.get(command_name))

            Argument.populate_args(args_info, args)
            args_info = Argument.set_keys_to_readable(args_info)

            return args_info
