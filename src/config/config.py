import json
from utils.exceptions import UnknownCommandError
from commands.argument import Argument

class Config:
    """
    Class representing the configuration settings.
    """

    def __init__(self, config_path: str) -> None:
        """
        Initialize the Config object.

        Args:
            config_path (str): The path to the configuration file.
        """
        self._config = self._load_config(config_path)
    
    def _load_config(self, config_path) -> dict:
        """
        Load the configuration from the specified file.

        Args:
            config_path: The path to the configuration file.

        Returns:
            dict: The loaded configuration.
        """
        with open(config_path, "r") as f:
            config = json.load(f)

        for key in config.keys():

            config[key]["named_args"] = {key: Argument(arg["type"],arg["name"], arg["value"]) for key, arg in config[key]["named_args"].items()}

            config[key]["positional_args"] = [Argument(el["type"], el["name"], el["value"]) for el in config[key]["positional_args"]]

        return config

    def assign_arguments(self, command_name:str, args: list) -> dict:
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
        if command_name not in self._config.keys():
            raise UnknownCommandError(command_name)
        else:
            args_info = dict(self._config[command_name])

            Argument.populate_args(args_info, args)
            args_info = Argument.set_keys_to_readable(args_info)

            return args_info