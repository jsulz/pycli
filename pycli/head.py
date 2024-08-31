""" This module contains the an implementation of head
    as a Python class which is responsible for reading the contents
    of a file/files and printing them to standard output. Additional 
    functionality includes the ability to read a certain number of lines
    or bytes from the file.
"""

import sys
from argparse import Namespace, _SubParsersAction


class Head:
    def __init__(self, args: Namespace):
        self.files = args.files
        self.n_lines = args.n
        self.c_bytes = args.c

    @staticmethod
    def register_subcommand(subparser: _SubParsersAction):
        head_parse = subparser.add_parser(name="head")
        head_parse.add_argument("files", type=str, nargs="+")
        head_parse.add_argument("-n", dest="n", type=int)
        head_parse.add_argument("-c", dest="c", type=int)
        head_parse.set_defaults(func=Head)

    # Opens the file and prints out however many lines or bytes have been requested
    def run(self):
        mode = "r"
        if self.c_bytes:
            mode += "b"

        for file in self.files:
            if len(self.files) > 1:
                print(f"\n==> {file} <==")
            try:

                with open(file, mode=mode) as f:
                    if self.c_bytes:
                        sys.stdout.buffer.write(f.read(self.c_bytes) + b"\n")
                        sys.stdout.flush()
                        continue

                    for pos, line in enumerate(f):
                        sys.stdout.write(line)
                        sys.stdout.flush()
                        if pos >= self.n_lines:
                            break

            except FileNotFoundError as e:
                print(e)

            except IsADirectoryError as e:
                print(e)
