from .command import Command


class CutCommand(Command):
    def __init__(self):
        super().__init__(
            "cut", "cut out selected portions of each line of a file"
        )

    def parse_byte_ranges(self, byte_range_str):
        """
        Parses a string representing byte ranges and returns a list of tuples.
        Adjusts for one-based indexing used in command-line tools.
        """
        ranges = []
        for part in byte_range_str.split(","):
            if "-" in part:
                start, end = part.split("-")
                start = (
                    int(start) - 1 if start else 0
                )  # Adjust for one-based indexing
                end = int(end) if end else None
                ranges.append((start, end))
            else:
                byte = int(part) - 1  # Adjust for one-based indexing
                ranges.append((byte, byte + 1))
        return ranges

    def cut_bytes_from_line(self, line, byte_ranges):
        """
        Extracts bytes from a line based on the specified byte ranges.
        """
        result = []
        for i in range(len(line)):
            for start, end in byte_ranges:
                if start is None:
                    start = 0
                if end is None or end > len(line):
                    end = len(line)
                if start <= i < end:
                    result.append(line[i])
                    break  # Exit the inner loop once the byte is included
        return "".join(result)

    def execute(self, args, input=None):
        byte_range_str = args["bytes"].value
        file_name = args["file"].value

        if not file_name and not input:
            raise ValueError(
                "cut: missing file operand\nTry 'cut --help' for more"
                " information."
            )

        try:
            byte_ranges = self.parse_byte_ranges(byte_range_str)
        except ValueError as e:
            return f"Invalid byte range specification: {str(e)}"

        lines = []
        if file_name:
            try:
                with open(file_name, "r") as file:
                    lines = file.read().splitlines()
            except FileNotFoundError:
                return f"File '{file_name}' does not exist."
            except IOError as e:
                return f"Error reading file '{file_name}': {str(e)}"

        result = []
        for line in lines or input.split("\n"):
            result.append(self.cut_bytes_from_line(line, byte_ranges))

        return "\n".join(result) + "\n"
