import unittest
from src.commands.argument import Argument
from utils.exceptions import (
    UnexpectedArgumentError,
    MissingValueError,
    TooManyArgumentsError,
)


class TestArgument(unittest.TestCase):
    def test_integer_argument(self):
        args_info = {
            "positional_args": [Argument(Argument.INTEGER, "number")],
            "named_args": {},
        }
        result = Argument.populate_args(args_info, ["123"])
        self.assertEqual(result["positional_args"][0].value, 123)

    def test_string_argument(self):
        args_info = {
            "positional_args": [Argument(Argument.STRING, "text")],
            "named_args": {},
        }
        result = Argument.populate_args(args_info, ["hello"])
        self.assertEqual(result["positional_args"][0].value, "hello")

    def test_flag_argument(self):
        args_info = {
            "positional_args": [],
            "named_args": {"v": Argument(Argument.FLAG, "verbose")},
        }
        result = Argument.populate_args(args_info, ["-v"])
        self.assertTrue(result["named_args"]["v"].value)

    def test_missing_value_error(self):
        args_info = {
            "positional_args": [],
            "named_args": {
                "n": Argument(Argument.FLAG_WITH_INTEGER, "number")
            },
        }
        with self.assertRaises(MissingValueError):
            Argument.populate_args(args_info, ["-n"])

    def test_unexpected_argument_error(self):
        args_info = {"positional_args": [], "named_args": {}}
        with self.assertRaises(UnexpectedArgumentError):
            Argument.populate_args(args_info, ["unexpected"])

    def test_too_many_arguments_error(self):
        args_info = {
            "positional_args": [Argument(Argument.STRING, "text")],
            "named_args": {},
        }
        with self.assertRaises(TooManyArgumentsError):
            Argument.populate_args(args_info, ["hello", "extra"])

    def test_flag_with_value(self):
        args_info = {
            "positional_args": [],
            "named_args": {
                "limit": Argument(Argument.FLAG_WITH_INTEGER, "limit")
            },
        }
        result = Argument.populate_args(args_info, ["-limit", "10"])
        self.assertEqual(result["named_args"]["limit"].value, 10)

    def test_list_argument(self):
        args_info = {
            "positional_args": [Argument(Argument.LIST, "items")],
            "named_args": {},
        }
        result = Argument.populate_args(args_info, ["item1", "item2", "item3"])
        self.assertEqual(
            result["positional_args"][0].value, ["item1", "item2", "item3"]
        )

    def test_combined_arguments(self):
        args_info = {
            "positional_args": [
                Argument(Argument.STRING, "name"),
                Argument(Argument.INTEGER, "age"),
            ],
            "named_args": {"verbose": Argument(Argument.FLAG, "verbose")},
        }
        result = Argument.populate_args(args_info, ["John", "30", "-verbose"])
        self.assertEqual(result["positional_args"][0].value, "John")
        self.assertEqual(result["positional_args"][1].value, 30)
        self.assertTrue(result["named_args"]["verbose"].value)

    def test_invalid_integer_argument(self):
        args_info = {
            "positional_args": [Argument(Argument.INTEGER, "number")],
            "named_args": {},
        }
        with self.assertRaises(ValueError):
            Argument.populate_args(args_info, ["abc"])

    def test_named_argument_followed_by_positional(self):
        args_info = {
            "positional_args": [Argument(Argument.STRING, "text")],
            "named_args": {"v": Argument(Argument.FLAG, "verbose")},
        }
        result = Argument.populate_args(args_info, ["-v", "message"])
        self.assertTrue(result["named_args"]["v"].value)
        self.assertEqual(result["positional_args"][0].value, "message")

    def test_unexpected_named_argument(self):
        args_info = {
            "positional_args": [],
            "named_args": {"v": Argument(Argument.FLAG, "verbose")},
            "stop_positional_after_named": False,
        }
        with self.assertRaises(UnexpectedArgumentError):
            Argument.populate_args(args_info, ["-unknown"])

    def test_only_positional_arguments(self):
        args_info = {
            "positional_args": [
                Argument(Argument.STRING, "first"),
                Argument(Argument.INTEGER, "second"),
            ],
            "named_args": {},
        }
        result = Argument.populate_args(args_info, ["hello", "123"])
        self.assertEqual(result["positional_args"][0].value, "hello")
        self.assertEqual(result["positional_args"][1].value, 123)

    def test_positional_arguments_after_named(self):
        args_info = {
            "positional_args": [Argument(Argument.STRING, "first")],
            "named_args": {"v": Argument(Argument.FLAG, "verbose")},
        }
        result = Argument.populate_args(args_info, ["-v", "hello"])
        self.assertTrue(result["named_args"]["v"].value)
        self.assertEqual(result["positional_args"][0].value, "hello")

    def test_unexpected_named_argument_after_positional(self):
        args_info = {
            "positional_args": [Argument(Argument.STRING, "first")],
            "named_args": {"v": Argument(Argument.FLAG, "verbose")},
            "stop_positional_after_named": False,
        }
        with self.assertRaises(TooManyArgumentsError):
            Argument.populate_args(args_info, ["hello", "-unknown"])

    def test_positional_arguments_continued_after_named(self):
        args_info = {
            "positional_args": [
                Argument(Argument.STRING, "first"),
                Argument(Argument.INTEGER, "second"),
            ],
            "named_args": {"v": Argument(Argument.FLAG, "verbose")},
            "stop_positional_after_named": False,
        }
        result = Argument.populate_args(args_info, ["hello", "-v", "123"])
        self.assertTrue(result["named_args"]["v"].value)
        self.assertEqual(result["positional_args"][0].value, "hello")
        self.assertEqual(result["positional_args"][1].value, 123)

    def test_convert_arg_value(self):
        self.assertEqual(
            Argument.convert_arg_value("123", Argument.INTEGER), 123
        )
        self.assertEqual(
            Argument.convert_arg_value("hello", Argument.STRING), "hello"
        )
        self.assertEqual(
            Argument.convert_arg_value("hello", Argument.FLAG_WITH_STRING),
            "hello",
        )
        self.assertEqual(
            Argument.convert_arg_value("123", Argument.FLAG_WITH_INTEGER), 123
        )
        self.assertEqual(
            Argument.convert_arg_value("123", Argument.LIST), ["123"]
        )

    def test_unexpected_argument_after_named_and_positional(self):
        args_info = {
            "positional_args": [Argument(Argument.STRING, "text")],
            "named_args": {"v": Argument(Argument.FLAG, "verbose")},
            "stop_positional_after_named": True,
        }
        with self.assertRaises(UnexpectedArgumentError):
            Argument.populate_args(args_info, ["hello", "-v", "-invalid"])
