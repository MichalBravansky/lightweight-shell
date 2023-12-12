import unittest
from src.shell_parser.executors import Call
from utils.unsafe_decorator import UnsafeDecorator


class TestDecorator(unittest.TestCase):
    def test_valid_call(self):
        UnsafeDecorator(Call('echo', ['foo'])).evaluate()

    def test_invalid_call(self):
        UnsafeDecorator(Call('ls', [0.4])).evaluate()
