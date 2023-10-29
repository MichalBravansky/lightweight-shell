class Argument:
    INTEGER = 1
    STRING = 2
    DECIMAL = 3
    FLAG = 4
    LIST = 5

    def __init__(self, arg_type, arg_name, arg_value=None):
        self.type = arg_type
        self.name = arg_name
        self.value = arg_value

    def is_arg_value_valid(self):
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
        i = 0
        while i < len(arg_list):
            arg = arg_list[i]
            if arg.startswith("-"):
                # It's a named argument or flag
                arg_name = arg[1:]
                if arg_name not in args_info["named_args"]:
                    # Treat as a positional argument for 'echo' like behavior
                    Argument.handle_positional_arg(args_info, arg, i)
                else:
                    # It's a valid named argument
                    i = Argument.handle_named_arg(args_info, arg_name, arg_list, i)
            else:
                # It's a positional argument
                Argument.handle_positional_arg(args_info, arg, i)
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
            print(f"Missing value for argument {arg_name}")
            return i  # No value provided, don't increment i

    @staticmethod
    def handle_positional_arg(args_info, arg, i):
        if i < len(args_info["positional_args"]):
            arg_obj = args_info["positional_args"][i]
            arg_obj.value = Argument.convert_arg_value(arg, arg_obj.type)
        else:
            # Assume last positional argument is an infinite list
            if len(args_info["positional_args"]) == 0:
                print(f"Unexpected argument {arg}")
            else:
                arg_obj = args_info["positional_args"][-1]
                if arg_obj.type == Argument.LIST:
                    arg_obj.value.append(
                        Argument.convert_arg_value(arg, Argument.STRING)
                    )
                else:
                    print(f"Unexpected argument {arg}")

    @staticmethod
    def convert_arg_value(arg_value, arg_type):
        converters = {
            Argument.INTEGER: int,
            Argument.STRING: str,
            Argument.DECIMAL: float,
            Argument.LIST: lambda x: [x],
        }
        return converters[arg_type](arg_value) if arg_type in converters else arg_value

    @staticmethod
    def set_keys_to_readable(args_info):
        return {
            arg.name: arg
            for arg in args_info["positional_args"]
            + list(args_info["named_args"].values())
        }
