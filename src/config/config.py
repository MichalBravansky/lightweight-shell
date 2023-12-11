import json
from commands.argument import Argument
import copy

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
    
    def is_command(self, command_name: str):
        return command_name in self._config.keys()
    
    def get(self, command_name: str):
        if command_name in self._config:
            return copy.deepcopy(self._config[command_name])
        return None