import os
import sys

# output is always in the order of: bytes\tlines\tcharacters\twords


class WC:
    def __init__(self, files, c_bytes, n_lines, n_chars, n_words):
        self.files = files
        self.c_bytes = c_bytes
        self.n_lines = n_lines
        self.n_chars = n_chars
        self.n_words = n_words
        self.output = ""

    def wc(self):

        for file in self.files:
            if self.c_bytes:
                try:
                    self.output += str(os.stat(file).st_size)
                except FileNotFoundError as e:
                    print(e)
                except IsADirectoryError as e:
                    print(e)
        sys.stdout.write(self.output + "\n")
