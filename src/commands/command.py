from abc import ABC, abstractmethod
from collections import defaultdict

class Command(ABC):
    def __init__(self, command_name, command_description):
        self.command_name = command_name
        self.command_description = command_description

    @staticmethod
    def convert_arg_list_to_arg_dict(self, args):
        arg_dict = defaultdict(str)
        for arg in args:
            arg_dict[arg.arg_name] = arg
        return arg_dict

    # Assumes that the command has been pre-validated by the parser. 
    @abstractmethod
    def execute(self, args):
        process_args()
        folder = None
        flag1 = False
        {"folder": }
        pass

    def help(self):
        print(f"{self.command_name}: {self.command_description}")
        print("Arguments:")
        for arg in self.command_args:
            print(f"\t{arg}")