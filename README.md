# COMP0010 Shell

Meet COMP0010 Shell, a lightweight shell built in Python offering an interactive [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93print_loop) interface. It uses a straightforward language akin to [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) for command execution. You can call applications and connect their output using pipelines. You can also run multiple commands one after another using ; to sequence commands.

## Features

In addition to the basic required functionality (described in [Applications](#applications)), COMP0010 Shell has been enhanced with the following features:

- **Autocomplete**: The shell provides an autocomplete feature that suggests possible completions for file names / directories when you press tab. This feature is implemented in the [`AutoCompleter`](src/utils/auto_completer.py) class.

- **Command History**: You can navigate through your command history using the up and down arrow keys. This allows you to easily access and repeat previously executed commands without retyping them.

- **Current Working Directory**: COMP0010 Shell will show the current directory you are in at all times without having to run the `pwd` command (although this is still available).

- **Command Help**: The shell supports the `--help` option, which provides help and usage information for a specific command. This feature is useful for understanding the available options and arguments for each command.

- **Helpful Commands**: There are several helpful commands included that are commonly used for file system manipulation and quality of life. These commands include `mkdir` for creating directories, `rm` for removing files and directories, and `clear` for clearing the shell's output.

## Implementation Details

COMP0010 Shell is a Python-based project that provides a simple and interactive command-line interface. The shell is designed to mimic the behavior of a Unix-like shell, with a focus on simplicity and usability.

The project is structured as follows:

- The [`src`](src/) directory contains the main source code of the shell. This includes the implementation of the shell itself, as well as various utility classes and functions.

- The [`commands`](src/commands/) subdirectory contains the implementation of the built-in commands that the shell supports.

- The [`utils`](src/utils/) subdirectory contains utility classes and functions that are used throughout the project, such as the [`AutoCompleter`](src/utils/auto_completer.py),[ArgumentHandler](src/utils/argument_handler.py), and [Exceptions](src/utils/exceptions.py).

- The [`test`](test/) directory contains unit tests as well as prop tests for the various components of the shell.

- The [`system_test`](system_test/) directory contains system tests that test the shell as a whole.

The shell is packaged as a Docker container for easy distribution and execution. The Dockerfile for building the container image is located at the root of the project directory.

The project uses GitHub Actions for continuous integration, which runs the unit tests, property tests, and system tests on every push to the repository.

### Modules used
Some of the notable (built in) Python modules used in COMP0010 Shell include:

- *readline*: Used for handling user input. This provides features like command history and line editing, enhancing the user experience in the interactive shell environment.

- *os and sys*: Used for interacting with the operating system. They provide functions for file and directory manipulation, process management, and reading from and writing to the standard input, output, and error streams.

- *unittest*: Used for running unit tests. It provides a rich set of assertions and a test discovery mechanism that makes it easy to define and run tests.

- *json*: Used for parsing and generating JSON data. It is used for handling configuration files and for communicating with external tools.

*Extra modules in [requirements.txt](requirements.txt)*

## Running COMP0010 Shell in Docker

To run COMP0010 Shell in a Docker container, follow these steps:

1. Build the container image (let's call it `shell`):

    ```
    docker build -t shell .
    ```

2. Run the shell in interactive mode:

    ```
    docker run -it --rm shell /comp0010/sh
    ```

3. Run the shell in non-interactive mode to evaluate a specific command (e.g., `echo foo`):

    ```
    docker run --rm shell /comp0010/sh -c 'echo foo'
    ```

## Running Tests and Analysis

To execute unit tests, code analysis, and test coverage, use the following commands:

1. Run unit tests:

    ```
    docker run -p 80:8000 -ti --rm shell /comp0010/tools/test
    ```

    The results will be available at [http://localhost](http://localhost).

2. Run code analysis:

    ```
    docker run -p 80:8000 -ti --rm shell /comp0010/tools/analysis
    ```

    The results will be available at [http://localhost](http://localhost).

3. Run test coverage:

    ```
    docker run -p 80:8000 -ti --rm shell /comp0010/tools/coverage
    ```

    The results of coverage computation will be available at [http://localhost](http://localhost).

## Running System Tests

To execute system tests, follow these steps:

1. Build a Docker image named `comp0010-system-test`:

    ```
    docker build -t comp0010-system-test .
    ```

2. Execute system tests using the following command (Python 3.7 or higher is required):

    ```
    python system_test/tests.py -v
    ```

    Individual system tests (e.g., `test_cat`) can be executed as:

    ```
    python system_test/tests.py -v TestShell.test_cat
    ```
    
# Language

A shell can be considered as a language for executing commands. COMP0010 Shell is an interactive shell, that is it parses user's command lines and executes the specified commands in a loop, known also as [REPL]((https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)), that

1. prints a prompt message;
2. parses user's command;
3. interprets user's command, runs the specified applications or built-in commands;
4. prints the output;
5. goes to step 1.

In a shell, applications play a role similar to that of functions in programming languages like Java and Python. A command line application in UNIX can be considered as a black-box with two inputs ([command line arguments](https://en.wikipedia.org/wiki/Command-line_interface#Arguments) and [stdin](https://en.wikipedia.org/wiki/Standard_streams#Standard_input_(stdin))) and three outputs ([stdout](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_(stdout)), [stderr](https://en.wikipedia.org/wiki/Standard_streams#Standard_error_(stderr)) and [exit code](https://en.wikipedia.org/wiki/Exit_status)). Command line arguments is a list of strings; stdin, stdout and stderr are sequences of bytes; exit code is a number. In COMP0010 Shell, exceptions are used instead of stderr and exit codes. 

![Applications in UNIX and COMP0010 Shell](apps.svg)

In this document, the syntax of COMP0010 Shell is specified using [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) notation.

## Command Line Parsing

A command may contain several subcommands. When COMP0010 Shell receives a command line, it

1. parses the command line on the command level. It recognizes three kind of commands: call command, sequence command, and pipe command;
2. evaluates the recognized commands in the proper order.

Step 1 uses the following grammar:

    <command> ::= <pipe> | <seq> | <call>
    <pipe> ::= <call> "|" <call> | <pipe> "|" <call>
    <seq>  ::= <command> ";" <command>
    <call> ::= ( <non-keyword> | <quoted> ) *

A non-keyword character is any character except for newlines, single quotes, double quotes, backquotes, semicolons `;` and vertical bars `|`. The non-terminal `<quoted>` is described below.

## Quoting

[Quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html) is used to remove the special meaning of certain characters or words to the shell.

To pass several arguments to an application, we can separate them with spaces:

    echo hello world

In this example, `echo` gets two command line arguments: `hello` and `world`. In order to pass `hello world` as a single argument, we can wrap it by quotes, so that the interpretation of the space character as a separator symbol is disabled:

    echo "hello world"

In this case, `echo` receives `hello world` as a single argument.

COMP0010 Shell supports three kinds of quotes: single quotes ```'```, double quotes ```"``` and backquotes ``` ` ```. The first and the second ones are used to disable interpretation of special characters, the last one is used to make command substitution.

COMP0010 Shell uses the following grammar to parse quoted strings:

    <quoted> ::= <single-quoted> | <double-quoted> | <backquoted>
    <single-quoted> ::= "'" <non-newline and non-single-quote> "'"
    <backquoted> ::= "`" <non-newline and non-backquote> "`"
    <double-quoted> ::= """ ( <backquoted> | <double-quote-content> ) * """

where `<double-quote-content>` can contain any character except for newlines, double quotes and backquotes.

Note that the rule for double quotes is different from single quotes: double quotes do not disable interpretation of backquotes. For example, in the following command:

    echo "this is space: `echo " "`"

the outer `echo` receives one argument rather than two.

Note that compared with e.g. Bash, COMP0010 Shell does not have character escaping.

## Call Command

A call command executes an application with specified inputs. For example,

    grep "Interesting String" < text1.txt > result.txt

finds all lines of the file `text1.txt` that contain the string `Interesting String` as a substring and saves them in the file `result.txt`.

COMP0010 Shell uses the following grammar to parse call commands:

    <call> ::= [ <whitespace> ] [ <redirection> <whitespace> ]* <argument> [ <whitespace> <atom> ]* [ <whitespace> ]
    <atom> ::= <redirection> | <argument>
    <argument> ::= ( <quoted> | <unquoted> )+
    <redirection> ::= "<" [ <whitespace> ] <argument>
                    | ">" [ <whitespace> ] <argument>

In this definition, `<whitespace>` is one or several tabs or spaces; the `<unquoted>` part of an `<argument>` can include any characters except for whitespace characters, quotes, newlines, semicolons `;`, vertical bar `|`, less than `<` and greater than `>`.

A call command is evaluated in the following order:

1. command substitution is performed (see command substitution);
2. the command is split into arguments corresponding to the `<argument>` non-terminal. Note that one backquoted argument can produce several arguments after command substitution. The quotes (`'`, `"` and ``` ` ```) that form the `<quoted>` non-terminals are removed;
3. the filenames are expanded (see globbing);
4. the application name is resolved (the first `<argument>` without a redirection operator is the application to be called);
5.	the specified application is executed.

Before executing an application, COMP0010 Shell interprets the [redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html) commands in the following way:

1. opens the file following the `<` symbol for input redirection; 
2. opens the file following the `>` symbol for output redirection;
3. if several files are specified for input or output redirection (e.g. `> a.txt > b.txt`), throws an exception;
4. if the file specified for input redirection does not exist, throws an exception;
5. if the file specified for output redirection does not exist, creates it.

After that, COMP0010 Shell runs the specified application, supplying given command line arguments and redirection streams.

## Sequence Command

Executes a sequence of commands separated by semicolons. For example, 

    cd articles; cat text1.txt

changes the current directory to `articles`, then displays the content of the file `text1.txt`.

The syntax of this command is the following:

    <seq> ::= <command> ";" <command>

It runs the first command; after the first command terminates, runs the second command. If an exception is thrown during the execution of the first command, the execution if the whole command must be terminated.

## Pipeline Command

The output of each command in a [pipeline](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html) is connected via a pipe to the input of the next command. For example, 

    cat articles/text1.txt | grep "Interesting String"

finds the line of the file `articles/text1.txt` that contain `Interesting String` as a substring. In this command, the output of `cat` is passed as the input to `grep` via a pipe.

Pipiline is expressed using a left-associative operator `|` that binds a set of call commands into a chain:

    <pipe> ::= <call> "|" <call> |
               <pipe> "|" <call>

The operator `|` connects stdout of the left subcommand to stdin of the right subcommand.

## Globbing

Globbing, also known as [filename expansion](https://www.gnu.org/software/bash/manual/html_node/Filename-Expansion.html), allows using patterns to capture one or several filenames. For example,

    cat articles/*

concatenates all files in the directory `articles`.

The symbol `*` (asterisk) in an unquoted part of an argument is interpreted as globbing.

For each argument `ARG` that contains unquoted `*` (asterisk), COMP0010 Shell performs the following:

1. collects all paths to existing files and directories such that these paths can be obtained by replacing all the unquoted asterisk symbols in `ARG` by some (possibly empty) sequences of non-slash characters.
2. if there are no such paths, leaves `ARG` unchanges.
3. if there are such paths, replaces `ARG` with a list of these path separated by spaces.

Globbing is performed after argument splitting, but it produces several command line arguments if several matching paths are found.

## Command Substitution

[Command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html) allows the output of a command to replace the command itself. For example, 

    wc -l `find -name '*.java'`

finds all files whose names end with `.java`, and counts the number of lines in these files.

A part of a call command surrounded by backquotes ``` ` ``` is interpreted as command substitution iff the backquotes are not inside single quotes (see the non-terminal `<backquoted>`).

For each part `SUBCMD` of the call command `CALL` surrounded by backquotes:

1. `SUBCMD` is evaluated as a separate shell command yielding the output `OUT`.
2. `SUBCMD`, together with the backquotes, is substituted in `CALL` with `OUT`. After substitution, the symbols in `OUT` are interpreted the following way:
    - whitespace characters are used for argument splitting. Since our shell does not support multi-line commands, newlines in `OUT` are replaced with spaces;
    - other characters (including quotes) are not interpreted during the next parsing step as special characters.
3. the modified `CALL` is evaluated. Note that there cannot be nested/recursive command substitutions.

Command substitution is performed after command-level parsing but before argument splitting.

# Applications

COMP0010 Shell provides implementations of widely-used UNIX applications: [cd](https://en.wikipedia.org/wiki/Cd_(command)), [pwd](https://en.wikipedia.org/wiki/Pwd), [ls](https://en.wikipedia.org/wiki/Ls), [cat](https://en.wikipedia.org/wiki/Cat_(Unix)), [echo](https://en.wikipedia.org/wiki/Echo_(command)), [head](https://en.wikipedia.org/wiki/Head_(Unix)), [tail](https://en.wikipedia.org/wiki/Tail_(Unix)), [grep](https://en.wikipedia.org/wiki/Grep), [find](https://en.wikipedia.org/wiki/Find_(Unix)), [sort](https://en.wikipedia.org/wiki/Sort_(Unix)), [uniq](https://en.wikipedia.org/wiki/Uniq), [cut](https://en.wikipedia.org/wiki/Cut_(Unix)), and also their unsafe versions. 

Compared to most UNIX shells, COMP0010 Shell has some important differences in handling applications:

- Applications are executed inside the shell process, rather than new separate processes.
- Applications throw exceptions instead of using exit codes and stderr.
- Applications do not read stdin directly from keyboard, but can only receive it from redirections or pipelines. If an application expects data from stdin, but it is not provided, the application should throw an exception.

## pwd

Outputs the current working directory followed by a newline.

    pwd

## cd

Changes the current working directory.

    cd PATH

- `PATH` is a relative path to the target directory.

## ls

Lists the content of a directory. It prints a list of files and directories separated by tabs and followed by a newline. Ignores files and directories whose names start with `.`.

    ls [PATH]

- `PATH` is the directory. If not specified, list the current directory.

## cat

Concatenates the content of given files and prints it to stdout:

    cat [FILE]...

- `FILE`(s) is the name(s) of the file(s) to contatenate. If no files are specified, uses stdin.

## echo

Prints its arguments separated by spaces and followed by a newline to stdout:

    echo [ARG]...

## head

Prints the first N lines of a given file or stdin. If there are less than N lines, prints only the existing lines without raising an exception.

    head [OPTIONS] [FILE]

- `OPTIONS`, e.g. `-n 15` means printing the first 15 lines. If not specified, prints the first 10 lines.
- `FILE` is the name of the file. If not specified, uses stdin.

## tail

Prints the last N lines of a given file or stdin. If there are less than N lines, prints only the existing lines without raising an exception.

    tail [OPTIONS] [FILE]

- `OPTIONS`, e.g. `-n 15` means printing the last 15 lines. If not specified, prints the last 10 lines.
- `FILE` is the name of the file. If not specified, uses stdin.

## grep

Searches for lines containing a match to the specified pattern. The output of the command is the list of lines. Each line is printed followed by a newline.

    grep PATTERN [FILE]...

- `PATTERN` is a regular expression in [PCRE](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) format.
- `FILE`(s) is the name(s) of the file(s). When multiple files are provided, the found lines should be prefixed with the corresponding file paths and colon symbols. If no file is specified, uses stdin.

## cut

Cuts out sections from each line of a given file or stdin and prints the result to stdout.

    cut OPTIONS [FILE]

- `OPTION` specifies the bytes to extract from each line:
    - `-b 1,2,3` extracts 1st, 2nd and 3rd bytes.
    - `-b 1-3,5-7` extracts the bytes from 1st to 3rd and from 5th to 7th.
    - `-b -3,5-` extracts the bytes from the beginning of line to 3rd, and from 5th to the end of line.
- `FILE` is the name of the file. If not specified, uses stdin.

## find

Recursively searches for files with matching names. Outputs the list of relative paths, each followed by a newline.

    find [PATH] -name PATTERN

- `PATTERN` is a file name with some parts replaced with `*` (asterisk).
- `PATH` is the root directory for search. If not specified, uses the current directory.

## uniq

Detects and deletes adjacent duplicate lines from an input file/stdin and prints the result to stdout.

    uniq [OPTIONS] [FILE]

- `OPTIONS`:
    - `-i` ignores case when doing comparison (case insensitive)
- `FILE` is the name of the file. If not specified, uses stdin.

## sort

Sorts the contents of a file/stdin line by line and prints the result to stdout.

    sort [OPTIONS] [FILE]

- `OPTIONS`:
    - `-r` sorts lines in reverse order
- `FILE` is the name of the file. If not specified, uses stdin.

## Unsafe applications

In COMP0010 Shell, each application has an unsafe variant. An unsafe version of an application is an application that has the same semantics as the original application, but instead of raising exceptions, it prints the error message to its stdout. This feature can be used to prevent long sequences from terminating early when some intermediate commands fail. The names of unsafe applications are prefixed with `_`, e.g. `_ls` and `_grep`.
