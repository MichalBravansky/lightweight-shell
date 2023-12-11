from utils.exceptions import (
    UnexpectedArgumentError,
    MissingValueError,
    TooManyArgumentsError,
)

class Argument:
    """
    Represents a command line argument with a type, name, and optional value.
    
    Attributes:
        type (int): Type of the argument (e.g., INTEGER, STRING).
        name (str): Name of the argument.
        value (any, optional): Value of the argument, defaults to None.
    """

    # Argument types
    INTEGER = 1
    STRING = 2
    DECIMAL = 3
    FLAG = 4
    FLAG_WITH_INTEGER = 5
    FLAG_WITH_STRING = 6
    LIST = 7

    def __init__(self, arg_type, arg_name, arg_value=None):
        """
        Initializes an Argument instance.

        Args:
            arg_type (int): The type of the argument.
            arg_name (str): The name of the argument.
            arg_value (any, optional): The initial value of the argument. Defaults to None.
        """
        self.type = arg_type
        self.name = arg_name
        self.value = arg_value

    def is_arg_value_valid(self):
        """
        Checks if the argument's value is valid based on its type.

        Returns:
            bool: True if the value is valid, False otherwise.
        """
        if self.type == Argument.INTEGER:
            return self.value.isdigit()
        elif self.type == Argument.DECIMAL:
            return self.value.replace(".", "", 1).isdigit()
        elif self.type == Argument.FLAG:
            return self.value is None
        else:
            return True

    @staticmethod
    def populate_args(args_info, arg_list):
        """
        Populates arguments based on the provided list of command line arguments.

        Args:
            args_info (dict): Information about expected arguments.
            arg_list (list[str]): List of command line arguments.

        Returns:
            dict: Updated args_info with populated arguments.

        Raises:
            MissingValueError: If a required value is missing.
            UnexpectedArgumentError: If an unexpected argument is encountered.
        """
        i = 0
        positional_count = 0
        seen_positional_args = False
        stop_positional_after_named_args = args_info.get("stop_positional_after_named", True)

        while i < len(arg_list):
            arg = arg_list[i]
            if arg.startswith("-"):
                arg_name = arg[1:]
                if arg_name in args_info["named_args"]:
                    i = Argument.handle_named_arg(args_info, arg_name, arg_list, i)
                elif not seen_positional_args or not stop_positional_after_named_args:
                    Argument.handle_positional_arg(args_info, arg, positional_count)
                    positional_count += 1
                else:
                    raise UnexpectedArgumentError(arg_name)
            else:
                seen_positional_args = True
                Argument.handle_positional_arg(args_info, arg, positional_count)
                positional_count += 1
            i += 1

        return args_info



    @staticmethod
    def handle_named_arg(args_info, arg_name, arg_list, i):
        """
        Handles a named argument and updates its value in args_info.

        Args:
            args_info (dict): Information about expected arguments.
            arg_name (str): The name of the argument to handle.
            arg_list (list[str]): List of command line arguments.
            i (int): Current index in arg_list.

        Returns:
            int: Updated index after processing the named argument.

        Raises:
            MissingValueError: If a required value is missing for the named argument.
        """
        arg_obj = args_info["named_args"][arg_name]
        if arg_obj.type in [Argument.FLAG, Argument.FLAG_WITH_INTEGER, Argument.FLAG_WITH_STRING]:
            arg_obj.value = True
            if arg_obj.type != Argument.FLAG:
                if i + 1 < len(arg_list):
                    arg_obj.value = Argument.convert_arg_value(arg_list[i + 1], arg_obj.type)
                    i += 1
                else:
                    raise MissingValueError(arg_name)
        return i


    @staticmethod
    def handle_positional_arg(args_info, arg, positional_count):
        """
        Handles a positional argument and updates its value in args_info.

        Args:
            args_info (dict): Information about expected arguments.
            arg (str): The current argument to handle.
            positional_count (int): Count of positional arguments processed so far.

        Raises:
            UnexpectedArgumentError: If an unexpected positional argument is encountered.
            TooManyArgumentsError: If too many arguments are provided.
        """
        if positional_count < len(args_info["positional_args"]):
            arg_obj = args_info["positional_args"][positional_count]
            arg_obj.value = Argument.convert_arg_value(arg, arg_obj.type)
        else:
            if len(args_info["positional_args"]) == 0:
                raise UnexpectedArgumentError(arg)
            else:
                arg_obj = args_info["positional_args"][-1]
                if arg_obj.type == Argument.LIST:
                    arg_obj.value.append(Argument.convert_arg_value(arg, Argument.STRING))
                else:
                    raise TooManyArgumentsError(arg)

    @staticmethod
    def convert_arg_value(arg_value, arg_type):
        """
        Converts the argument value to its appropriate type.

        Args:
            arg_value (str): The argument value as a string.
            arg_type (int): The type of the argument.

        Returns:
            any: The converted argument value.
        """
        converters = {
            Argument.INTEGER: int,
            Argument.STRING: str,
            Argument.DECIMAL: float,
            Argument.LIST: lambda x: [x],
            Argument.FLAG_WITH_INTEGER: int,
            Argument.FLAG_WITH_STRING: str,
        }
        return converters.get(arg_type, lambda x: x)(arg_value)

    @staticmethod
    def set_keys_to_readable(args_info):
        """
        Converts argument objects in args_info to a dictionary with readable keys.

        Args:
            args_info (dict): Information about expected arguments.

        Returns:
            dict: Dictionary with arguments as keys and their details as values.
        """
        return {
            arg.name: arg
            for arg in args_info["positional_args"]
            + list(args_info["named_args"].values())
        }
