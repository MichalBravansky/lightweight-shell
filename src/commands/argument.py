class Argument():
    INTEGER = 1
    STRING = 2
    DECIMAL = 3
    FLAG = 4

    def __init__(self, arg_type, arg_name, arg_value=None):
        self.arg_type = arg_type
        self.arg_name = arg_name
        self.arg_value = arg_value
    
    def is_arg_value_valid(self):
        if self.arg_type == Argument.INTEGER:
            return self.arg_value.isdigit()
        elif self.arg_type == Argument.DECIMAL:
            return self.arg_value.replace('.', '', 1).isdigit()
        elif self.arg_type == Argument.FLAG:
            return self.arg_value is None
        else:
            return True



