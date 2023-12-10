import os

class AutoCompleter:
    
    def completer(self, text: str, state: int):
        matches = [i for i in os.listdir(os.getcwd()) if i.startswith(text)]

        if state < len(matches):
            return matches[state]
        
        return None