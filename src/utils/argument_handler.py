from config import config
from utils.exceptions import UnknownCommandError
from commands.argument import Argument


class ArgumentHandler:
    """
    The ArgumentHandler class is responsible for assigning arguments to a
    specific command.

    The assign_arguments class method takes a command name and a list of
    arguments as input. It returns a dictionary where the keys are the
    argument names and the values are the argument values.

    The ArgumentHandler uses the Argument class to represent individual
    arguments. Each Argument object has a name and a value, which are set
    when the Argument object is created.

    If the command name is not recognized, the assign_arguments method raises
    an UnknownCommandError.
    """

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
            UnknownCommandError: If the command is not found in the
            configuration.
        """
        if not config.is_command(command_name):
            raise UnknownCommandError(command_name)
        else:
            args_info = dict(config.get(command_name))

            Argument.populate_args(command_name, args_info, args)
            args_info = Argument.set_keys_to_readable(args_info)

            return args_info
