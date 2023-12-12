import unittest
import tempfile
from pathlib import Path
from src.commands.uniq import UniqCommand as Uniq
from src.commands.argument import Argument


class TestUniq(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        with open(self.temp_path / 'test_file.txt', 'w') as f:
            f.write('apple\nOrange\norange\nbanana\nbanana\nApple\nbanana')

    def tearDown(self):
        self.test_dir.cleanup()

    def test_uniq_ignore_case(self):
        args = {
            'ignore_case': Argument(Argument.FLAG, 'ignore_case', True),
            'file': Argument(
                Argument.STRING, 'file', str(self.temp_path / 'test_file.txt')
            ),
        }
        expected = 'apple\nOrange\nbanana\nApple\nbanana'
        response = Uniq().execute(args)
        self.assertEqual(response, expected)

    def test_uniq_without_ignore_case(self):
        args = {
            'ignore_case': Argument(Argument.FLAG, 'ignore_case', False),
            'file': Argument(
                Argument.STRING, 'file', str(self.temp_path / 'test_file.txt')
            ),
        }
        expected = 'apple\nOrange\norange\nbanana\nApple\nbanana'
        response = Uniq().execute(args)
        self.assertEqual(response, expected)

    def test_uniq_no_file(self):
        args = {
            'ignore_case': Argument(Argument.FLAG, 'ignore_case', False),
            'file': Argument(Argument.STRING, 'file', None),
        }
        input_text = 'apple\nOrange\norange\nbanana\nApple\nbanana'
        expected = 'apple\nOrange\norange\nbanana\nApple\nbanana'
        response = Uniq().execute(args, input_text)
        self.assertEqual(response, expected)

    def test_uniq_no_file_no_input(self):
        args = {
            'ignore_case': Argument(Argument.FLAG, 'ignore_case', False),
            'file': Argument(Argument.STRING, 'file', None),
        }
        with self.assertRaises(ValueError):
            Uniq().execute(args)
