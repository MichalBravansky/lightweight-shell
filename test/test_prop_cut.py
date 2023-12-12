import unittest
from hypothesis import given, strategies as st
from src.commands.cut import CutCommand as Cut
from src.commands.argument import Argument


class TestCutProperty(unittest.TestCase):
    @given(
        data=st.text(
            min_size=1,
            max_size=50,
            alphabet=st.characters(blacklist_characters=["\xa0", "\u1234"]),
        ),  # blacklist chars represented in more than 1 byte
        start=st.integers(min_value=1, max_value=100),
        end=st.integers(min_value=1, max_value=100),
    )
    def test_cut_byte_range(self, data, start, end):
        if start > end:
            start, end = end, start
        byte_range = f"{start}-{end}"
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", byte_range)
        input_str = "\n".join(
            [data] * 25
        )  # Repeat the data to form multiple lines

        response = Cut().execute(
            {
                "bytes": byte_arg,
                "file": Argument(Argument.STRING, "file", None),
            },
            input=input_str,
        )

        expected_lines = input_str.split("\n")
        result_lines = response.split("\n")
        for expected_line, result_line in zip(expected_lines, result_lines):
            self.assertTrue(result_line in expected_line)
            self.assertLessEqual(len(result_line), end - start + 1)

    @given(
        # blacklist chars represented in more than 1 byte, \n to avoid singular newline
        data=st.text(
            min_size=1,
            max_size=50,
            alphabet=st.characters(
                blacklist_characters=["\xa0", "\u1234", "\n"]
            ),
        ),
        position=st.integers(min_value=1, max_value=100),
    )
    def test_cut_single_byte(self, data, position):
        if position > len(data):
            return
        byte_range = f"{position}-{position}"
        byte_arg = Argument(Argument.FLAG_WITH_STRING, "bytes", byte_range)
        input_str = "\n".join([data] * 25)

        response = Cut().execute(
            {
                "bytes": byte_arg,
                "file": Argument(Argument.STRING, "file", None),
            },
            input=input_str,
        )

        expected_lines = input_str.split("\n")
        result_lines = response.split("\n")
        for expected_line, result_line in zip(expected_lines, result_lines):
            self.assertTrue(result_line in expected_line)
            self.assertEqual(len(result_line), 1)
