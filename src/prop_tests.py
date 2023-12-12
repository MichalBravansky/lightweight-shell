from hypothesis import given, strategies as st
from shell_parser import *  # noqa: F401, F403
from shell import eval
import os
import pytest


@pytest.fixture(autouse=True)
def manage_cwd():
    original_cwd = os.getcwd()
    yield
    os.chdir(original_cwd)


def setup_directories(dir_names):
    for dir_name in dir_names:
        os.makedirs(dir_name, exist_ok=True)


def create_files_with_contents(files_contents):
    for i, content in enumerate(files_contents):
        filename = f"file{i}"
        with open(filename, "w") as file:
            file.write(content)


def create_file_with_lines(filename, lines):
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


@given(st.text())
def test_echo_property(input_str):
    result = eval(f"echo {input_str}")
    assert result.strip() == input_str


@given(st.lists(st.text(), unique=True))
def test_ls_invariance(dir_contents):
    setup_directories(dir_contents)
    first_ls = eval("ls")
    second_ls = eval("ls")
    assert first_ls == second_ls


@given(st.text())
def test_pwd_consistency(unused_input):
    first_pwd = eval("pwd")
    eval(unused_input)  # Execute a random command
    second_pwd = eval("pwd")
    assert first_pwd == second_pwd


@given(st.text(), st.lists(st.text()))
def test_grep_filtering(search_string, lines):
    create_file_with_lines("testfile", lines)
    result = eval(f"grep {search_string} testfile")
    for line in result.split("\n"):
        assert search_string in line


@given(st.text())
def test_cat_nonexistent_file(file_name):
    if not os.path.exists(file_name):
        result = eval(f"cat {file_name}")
        # Check the appropriate failure response of your shell
        assert "No such file or directory" in result


@given(st.text())
def test_cd_change_directory(dir_name):
    setup_directories([dir_name])
    eval(f"cd {dir_name}")
    assert os.getcwd().endswith(dir_name)


@given(st.text(), st.text())
def test_file_creation(file_name, file_content):
    eval(f"echo {file_content} > {file_name}")
    with open(file_name, "r") as file:
        content = file.read()
    assert content.strip() == file_content


@given(st.lists(st.text(), min_size=1))
def test_pipe_operation(lines):
    create_file_with_lines("file.txt", lines)
    result = eval("cat file.txt | sort")
    assert result.strip().split("\n") == sorted(lines)
