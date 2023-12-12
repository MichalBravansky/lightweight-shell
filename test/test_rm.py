import unittest
from pathlib import Path
from src.commands.rm import RmCommand as Rm
from src.commands.argument import Argument
import os
import tempfile

class TestRm(unittest.TestCase):

    def setUp(self) -> None:
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)

        with open(self.temp_path / "file.txt", "w") as f:
            f.write("Test file 1")

        os.makedirs(self.temp_path / "subdir")

        with open(self.temp_path / "subdir/file.txt", "w") as f:
            f.write("Test file 2")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_rm_single_file(self):
        command = Rm()
        path = self.temp_path / "file.txt"

        args = {
            "recursive": Argument(Argument.FLAG, "recursive", False),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        command.execute(args)
        self.assertFalse(os.path.exists(path))

    def test_rm_resursive(self):
        command = Rm()
        path = self.temp_path / "subdir"

        args = {
            "recursive": Argument(Argument.FLAG, "recursive", True),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        command.execute(args)
        self.assertFalse(os.path.exists(path))
    
    def test_rm_multiple_files(self):
        command = Rm()
        path1 = self.temp_path / "file.txt"
        path2 = self.temp_path / "subdir/file.txt"

        args = {
            "recursive": Argument(Argument.FLAG, "recursive", False),
            "paths": Argument(Argument.LIST, "paths", [path1, path2])
        }

        command.execute(args)
        self.assertFalse(os.path.exists(path1))
        self.assertFalse(os.path.exists(path2))
    
    def test_rm_multiple_files_recursive(self):
        command = Rm()
        path1 = self.temp_path / "file.txt"
        path2 = self.temp_path / "subdir/file.txt"

        args = {
            "recursive": Argument(Argument.FLAG, "recursive", True),
            "paths": Argument(Argument.LIST, "paths", [path1, path2])
        }

        command.execute(args)
        self.assertFalse(os.path.exists(path1))
        self.assertFalse(os.path.exists(path2))
    
    def test_rm_no_file(self):
        command = Rm()
        path = self.temp_path / "non_existing_file.txt"

        args = {
            "recursive": Argument(Argument.FLAG, "recursive", False),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        with self.assertRaises(FileNotFoundError):
            command.execute(args)
    
    def test_rm_resursive_no_path(self):
        command = Rm()
        path = self.temp_path / "non_existing_directory"

        args = {
            "recursive": Argument(Argument.FLAG, "recursive", True),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        with self.assertRaises(FileNotFoundError):
            command.execute(args)

    def test_rm_directory_removal(self):
        command = Rm()
        path = self.temp_path / "subdir"

        args = {
            "recursive": Argument(Argument.FLAG, "recursive", False),
            "paths": Argument(Argument.LIST, "paths", [path])
        }

        with self.assertRaises(IsADirectoryError):
            command.execute(args)