class UnexpectedArgumentError(Exception):
    def __init__(self, command: str, arg: str):
        self.command = command
        self.arg = arg
        super().__init__(f'{command}: Unexpected argument: {arg}')


class MissingValueError(Exception):
    def __init__(self, command: str, arg: str):
        self.command = command
        self.arg = arg
        super().__init__(f'{command}: Missing value for argument: {arg}')


class TooManyArgumentsError(Exception):
    def __init__(self, command: str, arg: str):
        self.command = command
        self.arg = arg
        super().__init__(f'{command}: Too many arguments: {arg}')


class ParsingError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(
            f'Unable to parse the provided shell. Error: {message}'
        )


class UnknownCommandError(Exception):
    def __init__(self, command):
        self.command = command
        super().__init__(f'{command}: command not found')
