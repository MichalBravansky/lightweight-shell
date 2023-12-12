import subprocess

def run_mutpy(target, test):
    subprocess.run(["mut.py", "--target", target, "--unit-test", test])

for target, test in [
    ("src/commands/find.py", "test/test_find.py"),
    ("src/commands/grep.py", "test/test_grep.py"),
    ("src/commands/cut.py", "test/test_cut.py"),
    ("src/commands/sort.py", "test/test_sort.py"),
    ("src/commands/head.py", "test/test_head.py"),
]:
    run_mutpy(target, test)