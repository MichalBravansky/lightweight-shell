import os


class AutoCompleter:
    """
    The AutoCompleter class provides autocomplete suggestions based on a given
    input string. It suggests files and directories in the current working
    directory that start with the input string.
    """

    def completer(self, text: str, state: int):
        """
        Return the next autocomplete suggestion that starts with the input
        text.

        Parameters:
        text (str): The input string to match.
        state (int): The index of the suggestion to return.

        Returns:
        str: The next matching suggestion, or None if there are no more
             matches.
        """
        matches = [i for i in os.listdir(os.getcwd()) if i.startswith(text)]

        if state < len(matches):
            return matches[state]

        return None
