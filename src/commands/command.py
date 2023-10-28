from abc import ABC, abstractmethod
from collections import defaultdict

class Command(ABC):
    def __init__(self, command_name, command_description):
        self.command_name = command_name
        self.command_description = command_description

    # Assumes that the command has been pre-validated by the parser. 
    @abstractmethod
    def execute(self, args):
        process_args()
        folder = None
        flag1 = False
        pass

    def help(self):
        print(f"{self.command_name}: {self.command_description}")
        print("Arguments:")
        for arg in self.command_args:
            print(f"\t{arg}")