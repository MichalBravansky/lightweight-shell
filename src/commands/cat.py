import argparse
import os
import re
from .command import Command

class CatCommand(Command):
    def __init__(self):
        super().__init__("cat", "concatenate and print files")

    def execute(self, args):
        for filename in args['files'].value:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    if args['number_nonblank'].value:
                        lines = self.number_non_blank_lines(lines)
                    if args['number_output_lines'].value:
                        lines = self.number_all_lines(lines)
                    if args['squeeze_blank'].value:
                        lines = self.squeeze_empty_lines(lines)
                    if args['display_non_printing_chars'].value:
                        lines = self.display_non_printing_chars(lines)
                    if args['display_non_printing_chars_and_dollar'].value:
                        lines = self.display_non_printing_chars_and_dollar(lines)
                    if args['display_non_printing_chars_and_tab'].value:
                        lines = self.display_non_printing_chars_and_tab(lines)
                    print(''.join(lines))
            else:
                print(f"{filename} does not exist")

    def number_non_blank_lines(self, lines):
        return [f"{i+1} {line}" for i, line in enumerate(lines) if line.strip() != '']

    def number_all_lines(self, lines):
        return [f"{i+1} {line}" for i, line in enumerate(lines)]

    def squeeze_empty_lines(self, lines):
        return [line for i, line in enumerate(lines) if i == 0 or lines[i-1].strip() != '' or line.strip() != '']

    def display_non_printing_chars(self, lines):
        return [re.sub(r'[^ -~]', lambda match: '^' + chr(ord(match.group(0)) ^ 0x40), line) for line in lines]

    def display_non_printing_chars_and_dollar(self, lines):
        return [line + '$\n' for line in self.display_non_printing_chars(lines)]

    def display_non_printing_chars_and_tab(self, lines):
        return [line.replace('\t', '^I') for line in self.display_non_printing_chars(lines)]