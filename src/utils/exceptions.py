class UnexpectedArgumentError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(f"Unexpected argument: {arg}")

class MissingValueError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(f"Missing value for argument: {arg}")

class TooManyArgumentsError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(f"Too many arguments: {arg}")