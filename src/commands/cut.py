from .command import Command


class CutCommand(Command):
    """
    Represents the 'cut' command which cuts out selected portions of each line of a file.

    This command mimics the behavior of the Unix 'cut' command. It is used to extract specified byte
    or character ranges from each line of a file or a given input string.
    """

    def __init__(self):
        super().__init__(
            "cut", "cut out selected portions of each line of a file"
        )

    def parse_byte_ranges(self, byte_range_str):
        """
        Parses a string representing byte ranges and returns a list of tuples.

        The function adjusts for one-based indexing used in command-line tools.

        Args:
            byte_range_str (str): String representing byte ranges, e.g., "1-3,5".

        Returns:
            list: A list of tuples representing the byte ranges.

        Raises:
            ValueError: If there's an error in parsing the byte range string.
        """
        ranges = []
        for part in byte_range_str.split(","):
            if "-" in part:
                start, end = part.split("-")
                start = int(start) - 1 if start else 0
                end = int(end) if end else None
                ranges.append((start, end))
            else:
                byte = int(part) - 1
                ranges.append((byte, byte + 1))
        return ranges

    def cut_bytes_from_line(self, line, byte_ranges):
        """
        Extracts bytes from a line based on the specified byte ranges.

        Args:
            line (str): The line from which to cut bytes.
            byte_ranges (list of tuples): Byte ranges to cut from the line.

        Returns:
            str: The extracted bytes as a single string.
        """
        result = []
        for i in range(len(line)):
            for start, end in byte_ranges:
                end = end if end and end <= len(line) else len(line)
                if start <= i < end:
                    result.append(line[i])
                    break
        return "".join(result)

    def execute(self, args, input=None):
        """
        Executes the 'cut' command with the provided arguments and optional input.

        Args:
            args (dict): A dictionary containing command arguments. Expected keys are 'bytes' for the
                         byte ranges to cut and 'file' for the file path.
            input (str, optional): An optional string input to use when no file is provided.

        Returns:
            str: The lines with the specified byte ranges cut out.

        Raises:
            ValueError: If no file or input is provided, or if byte ranges are invalid.
            FileNotFoundError: If the provided file path does not exist.
            IOError: If there's an error reading the file.
        """
        byte_range_str = args["bytes"].value
        file_name = args["file"].value

        if not file_name and not input:
            raise ValueError(
                "cut: missing file operand\nTry 'cut --help' for more"
                " information."
            )

        byte_ranges = self._parse_and_validate_byte_ranges(byte_range_str)

        lines = self._read_lines_from_file_or_input(file_name, input)
        return self._cut_bytes_from_lines(lines, byte_ranges)

    def _parse_and_validate_byte_ranges(self, byte_range_str):
        """
        Parses and validates the byte range string.

        Args:
            byte_range_str (str): String representing byte ranges.

        Returns:
            list: A list of tuples representing the byte ranges.

        Raises:
            ValueError: If the byte range string is invalid.
        """
        try:
            return self.parse_byte_ranges(byte_range_str)
        except ValueError as e:
            raise ValueError(f"Invalid byte range specification: {str(e)}")

    def _read_lines_from_file_or_input(self, file_name, input):
        """
        Reads lines from a file or input string.

        Args:
            file_name (str): The file name to read from.
            input (str): The input string.

        Returns:
            list: A list of lines.

        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If there's an error reading the file.
        """
        if file_name:
            try:
                with open(file_name, "r") as file:
                    return file.read().splitlines()
            except FileNotFoundError:
                raise FileNotFoundError(f"File '{file_name}' does not exist.")
            except IOError as e:
                raise IOError(f"Error reading file '{file_name}': {str(e)}")
        return input.split("\n")

    def _cut_bytes_from_lines(self, lines, byte_ranges):
        """
        Cuts bytes from each line based on the byte ranges.

        Args:
            lines (list of str): The lines to cut bytes from.
            byte_ranges (list of tuples): Byte ranges to cut from each line.

        Returns:
            str: Concatenated string of all lines with bytes cut out.
        """
        result = [
            self.cut_bytes_from_line(line, byte_ranges) for line in lines
        ]
        return "\n".join(result)
