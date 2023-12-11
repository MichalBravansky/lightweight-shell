import unittest
import tempfile
import os
from pathlib import Path
from src.shell_parser.executors import Call, Redirect, RedirectionType, Pipe, Sequence

from src.utils.unsafe_decorator import UnsafeDecorator


class TestExecutors(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        with open(self.temp_path / "file1.txt", "w") as f:
            f.write("Hello World\nTest Line 1\nAnother Test Line")
        with open(self.temp_path / "file2.txt", "w") as f:
            f.write("Test Line 2\nSample Text\nMore Test Lines")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_call_arguments(self):
        call = Call("echo", ["foo", "bar"])
        self.assertListEqual(call.evaluate(), ["foo bar"])
    
    def test_call_no_arguments(self):
        call = Call("echo", [])
        self.assertListEqual(call.evaluate(), [])
    
    def test_redirection_read(self):
        call = Call("cat", [])
        redirection = Redirect(call, RedirectionType.READ, self.temp_path / "file1.txt")
        self.assertListEqual(redirection.evaluate(), ["Hello World\nTest Line 1\nAnother Test Line"])
    
    def test_redirection_append(self):
        call = Call("cat", [])
        redirection = Redirect(call, RedirectionType.APPEND, self.temp_path / "file1.txt")
        redirection.evaluate("Test Line 4")
        with open(self.temp_path / "file1.txt", "r") as f:
            self.assertEqual(f.read(), "Hello World\nTest Line 1\nAnother Test LineTest Line 4")
    
    def test_redirection_overwrite(self):
        call = Call("cat", [])
        redirection = Redirect(call, RedirectionType.OVERWRITE, self.temp_path / "file1.txt")
        redirection.evaluate("Test Line 4")
        with open(self.temp_path / "file1.txt", "r") as f:
            self.assertEqual(f.read(), "Test Line 4")
    
    def test_redirection_read_nonexistent(self):
        call = Call("cat", [])
        redirection = Redirect(call, RedirectionType.READ, self.temp_path / "file3.txt")
        self.assertRaises(FileNotFoundError, redirection.evaluate)

    def test_pipe_single(self):
        call1 = Call("cat", [os.path.join(self.temp_path, "file1.txt")])
        call2 = Call("grep", [])
        pipe = Pipe(call1, call2)
        self.assertListEqual(pipe.evaluate(), ["Hello World\nTest Line 1\nAnother Test Line"])

    def test_pipe_multiple(self):
        call1 = Call("cat", [os.path.join(self.temp_path, "file1.txt")])
        call2 = Call("grep", ["Test"])
        call3 = Call("cat", [])

        pipe = Pipe(call1, Pipe(call2, call3))
        self.assertListEqual(pipe.evaluate(), ["Test Line 1\nAnother Test Line"])

    def test_pipe_multiple_redirection(self):
        call1 = Call("cat", [os.path.join(self.temp_path, "file1.txt")])
        call2 = Call("grep", ["Test"])
        call3 = Call("cat", [])

        pipe = Pipe(call1, Pipe(call2, Redirect(call3, RedirectionType.APPEND, self.temp_path / "file3.txt")))
        pipe.evaluate()
        with open(self.temp_path / "file3.txt", "r") as f:
            self.assertEqual(f.read(), "Test Line 1\nAnother Test Line")
    
    def test_sequence_single(self):
        call1 = Call("echo", ["foo"])
        call2 = Call("echo", ["bar"])
        sequence = Sequence(call1, call2)
        self.assertListEqual(sequence.evaluate(), ["foo", "bar"])
    
    def test_sequence_multiple(self):
        call1 = Call("echo", ["foo"])
        call2 = Call("echo", ["bar"])
        call3 = Call("echo", ["baz"])
        sequence = Sequence(call1, Sequence(call2, call3))
        self.assertListEqual(sequence.evaluate(), ["foo", "bar", "baz"])
    
    def test_sequence_redirection(self):
        call1 = Call("echo", ["foo"])
        call2 = Call("echo", ["bar"])
        sequence = Sequence(call1, Redirect(call2, RedirectionType.OVERWRITE, self.temp_path / "file3.txt"))
        sequence.evaluate()
        with open(self.temp_path / "file3.txt", "r") as f:
            self.assertEqual(f.read(), "bar")

    def test_unsafe_call_no_arguments(self):
        call = UnsafeDecorator(Call("echo", []))
        self.assertListEqual(call.evaluate(), [])
    
    def test_unsafe_call_arguments(self):
        call = UnsafeDecorator(Call("echo", ["foo", "bar"]))
        self.assertListEqual(call.evaluate(), ["foo bar"])
    
    def test_unsafe_call_argument_exception(self):
        try:
            call = UnsafeDecorator(Call("ls", [6]))
        except:
            self.fail("Exception raised when using UnsafeDectorator")

    def test_none_sequence(self):
        call1 = None
        call2 = None
        sequence = Sequence(call1, call2)
        self.assertListEqual(sequence.evaluate(), [])

    def test_none_pipe(self):
        call1 = None
        call2 = None
        pipe = Pipe(call1, call2)
        self.assertListEqual(pipe.evaluate(), [None])