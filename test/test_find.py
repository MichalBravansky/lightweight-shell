import unittest
import tempfile
import os
from pathlib import Path
from src.commands.find import FindCommand as Find
from src.commands.argument import Argument


class TestFind(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        os.makedirs(self.temp_path / 'subdir')
        with open(self.temp_path / 'file1.txt', 'w') as f:
            f.write('Test file 1')
        with open(self.temp_path / 'file2.txt', 'w') as f:
            f.write('Test file 2')
        with open(self.temp_path / 'subdir' / 'file3.txt', 'w') as f:
            f.write('Test file 3')

    def tearDown(self):
        self.test_dir.cleanup()

    def test_find_valid_directory_and_pattern(self):
        dir_arg = Argument(Argument.STRING, 'directory', str(self.temp_path))
        name_arg = Argument(Argument.FLAG_WITH_STRING, 'name', '*.txt')
        response = Find().execute({'directory': dir_arg, 'name': name_arg})
        expected_files = ['file2.txt', 'file1.txt', 'subdir/file3.txt']
        expected = (
            '\n'.join(str(self.temp_path / f) for f in expected_files) + '\n'
        )
        self.assertCountEqual(response, expected)

    def test_find_invalid_directory(self):
        dir_arg = Argument(Argument.STRING, 'directory', 'invalid')
        name_arg = Argument(Argument.FLAG_WITH_STRING, 'name', '*.txt')
        with self.assertRaises(ValueError):
            Find().execute({'directory': dir_arg, 'name': name_arg})

    def test_find_no_pattern(self):
        dir_arg = Argument(Argument.STRING, 'directory', str(self.temp_path))
        name_arg = Argument(Argument.FLAG_WITH_STRING, 'name', None)
        with self.assertRaises(ValueError):
            Find().execute({'directory': dir_arg, 'name': name_arg})

    def test_find_no_files_found(self):
        dir_arg = Argument(Argument.STRING, 'directory', str(self.temp_path))
        name_arg = Argument(Argument.FLAG_WITH_STRING, 'name', '*.jpg')
        response = Find().execute({'directory': dir_arg, 'name': name_arg})
        expected = '\n'
        self.assertEqual(response, expected)