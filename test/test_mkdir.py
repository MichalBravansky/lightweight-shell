import unittest
from pathlib import Path
from src.commands.mkdir import MkdirCommand as Mkdir
from src.commands.argument import Argument
import os
import tempfile

class TestMkdir(unittest.TestCase):

    def setUp(self) -> None:
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        os.makedirs(self.temp_path / "subdir")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_mkdir(self):
        command = Mkdir()
        path = os.path.join(self.temp_path, "new_dir")

        args = {
            "create_subdirectories": Argument(Argument.FLAG, "create_subdirectories", False),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        command.execute(args)
        self.assertTrue(os.path.exists(path))

    def test_mkdir_subdirectories(self):
        command = Mkdir()
        path = os.path.join(self.temp_path, "new_dir/path/non_existing_directory")

        args = {
            "create_subdirectories": Argument(Argument.FLAG, "create_subdirectories", True),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        command.execute(args)
        self.assertTrue(os.path.exists(path))

    def test_mkdir_path_already_exists(self):
        command = Mkdir()
        path = os.path.join(self.temp_path, "subdir")

        args = {
            "create_subdirectories": Argument(Argument.FLAG, "create_subdirectories", False),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        with self.assertRaises(FileExistsError):
            command.execute(args)

    def test_mkdir_subdirectories_path_already_exists(self):
        command = Mkdir()
        path = os.path.join(self.temp_path, "subdir")
                             
        args = {
            "create_subdirectories": Argument(Argument.FLAG, "create_subdirectories", True),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        with self.assertRaises(FileExistsError):
            command.execute(args)

    def test_mkdir_no_file(self):
        command = Mkdir()
        path = os.path.join(self.temp_path, "new_dir/path/non_existing_directory")

        args = {
            "create_subdirectories": Argument(Argument.FLAG, "create_subdirectories", False),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        with self.assertRaises(FileNotFoundError):
            command.execute(args)