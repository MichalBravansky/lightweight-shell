import unittest
import os
from src.commands.clear import ClearCommand as Clear
from src.commands.argument import Argument

class TestClear(unittest.TestCase):

    def test_clear(self):
        self.assertIsNone(Clear().execute(None))

