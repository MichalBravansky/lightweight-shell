from utils.exceptions import (
    UnexpectedArgumentError,
    MissingValueError,
    TooManyArgumentsError,
)


class Argument:
    INTEGER = 1
    STRING = 2
    DECIMAL = 3
    FLAG = 4
    FLAG_WITH_INTEGER = 5
    FLAG_WITH_STRING = 6
    LIST = 7

    def __init__(self, arg_type, arg_name, arg_value=None):
        self.type = arg_type
        self.name = arg_name
        self.value = arg_value

    @staticmethod
    def populate_args(args_info, arg_list):
        i = 0
        positional_count = 0

        seen_positional_args = False
        stop_positional_after_named_args = args_info.get(
            "stop_positional_after_named", True
        )
        while i < len(arg_list):
            arg = arg_list[i]
            if arg.startswith("-"):
                # It's a named argument or flag
                arg_name = arg[1:]
                if arg_name in args_info["named_args"]:
                    if args_info["named_args"][arg_name].type in [
                        Argument.FLAG_WITH_INTEGER,
                        Argument.FLAG_WITH_STRING,
                    ]:
                        # This flag expects a value, consume the next argument
                        i += 1
                        if i < len(arg_list):
                            args_info["named_args"][
                                arg_name
                            ].value = Argument.convert_arg_value(
                                arg_list[i],
                                args_info["named_args"][arg_name].type,
                            )
                        else:
                            raise MissingValueError(arg_name)
                    else:
                        args_info["named_args"][arg_name].value = True
                elif (
                    not seen_positional_args
                    or not stop_positional_after_named_args
                ):
                    # Treat as a positional argument for 'echo' like behavior
                    Argument.handle_positional_arg(
                        args_info, arg, positional_count
                    )
                    positional_count += 1
                else:
                    raise UnexpectedArgumentError(arg_name)
            else:
                seen_positional_args = True
                Argument.handle_positional_arg(
                    args_info, arg, positional_count
                )
                positional_count += 1
            i += 1
        return args_info

    @staticmethod
    def handle_named_arg(args_info, arg_name, arg_list, i):
        arg_obj = args_info["named_args"][arg_name]
        if arg_obj.type == Argument.FLAG:
            arg_obj.value = True  # Set flag to True
            return i  # No value expected for flags, so don't increment i
        elif (i + 1 < len(arg_list)) and (not arg_list[i + 1].startswith("-")):
            arg_value = arg_list[i + 1]
            arg_obj.value = Argument.convert_arg_value(arg_value, arg_obj.type)
            return i + 1  # Increment i to skip the value
        else:
            raise MissingValueError(arg_name)

    @staticmethod
    def handle_positional_arg(args_info, arg, positional_count):
        if positional_count < len(args_info["positional_args"]):
            arg_obj = args_info["positional_args"][positional_count]
            arg_obj.value = Argument.convert_arg_value(arg, arg_obj.type)
        else:
            # Assume last positional argument is an infinite list
            if len(args_info["positional_args"]) == 0:
                raise UnexpectedArgumentError(arg)
            else:
                arg_obj = args_info["positional_args"][-1]
                if arg_obj.type == Argument.LIST:
                    arg_obj.value.append(
                        Argument.convert_arg_value(arg, Argument.STRING)
                    )
                else:
                    raise TooManyArgumentsError(arg)

    @staticmethod
    def convert_arg_value(arg_value, arg_type):
        converters = {
            Argument.INTEGER: int,
            Argument.STRING: str,
            Argument.DECIMAL: float,
            Argument.LIST: lambda x: [x],
            Argument.FLAG_WITH_INTEGER: int,
            Argument.FLAG_WITH_STRING: str,
        }
        return (
            converters[arg_type](arg_value)
            if arg_type in converters
            else arg_value
        )

    @staticmethod
    def set_keys_to_readable(args_info):
        return {
            arg.name: arg
            for arg in args_info["positional_args"]
            + list(args_info["named_args"].values())
        }
