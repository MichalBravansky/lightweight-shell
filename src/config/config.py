import json
from commands.argument import Argument
import copy


class Config:
    """
    Class representing the command configuration options.
    """

    def __init__(self, config_path: str) -> None:
        """
        Initialize the Config object.

        Args:
            config_path (str): The path to the configuration file.
        """
        self._config = self._load_config(config_path)

    def _load_config(self, config_path: str) -> dict:
        """
        Load the configuration from the specified file.

        Args:
            config_path (str): The path to the configuration file.

        Returns:
            dict: The loaded configuration.
        """
        with open(config_path, 'r') as f:
            config = json.load(f)

        for key in config.keys():
            config[key]['named_args'] = {
                key: Argument(
                    getattr(Argument, arg['type']), arg['name'], arg['value']
                )
                for key, arg in config[key]['named_args'].items()
            }

            config[key]['positional_args'] = [
                Argument(
                    getattr(Argument, el['type']), el['name'], el['value']
                )
                for el in config[key]['positional_args']
            ]

        return config

    def is_command(self, command_name: str) -> bool:
        """
        Check if a command exists in the configuration.

        Args:
            command_name (str): The name of the command to check.

        Returns:
            bool: True if the command exists in the configuration,
            False otherwise.
        """
        return command_name in self._config

    def get(self, command_name: str) -> dict:
        """
        Retrieve the configuration for a given command.

        Args:
            command_name (str): The name of the command.

        Returns:
            dict: A deep copy of the configuration for the command.

        """
        if command_name in self._config:
            return copy.deepcopy(self._config[command_name])
