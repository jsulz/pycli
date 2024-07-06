""" This module contains an implementation of wc in Python. 
    The class is responsible for reading the contents of a file/files
    and printing out the number of lines, words, characters, and bytes in that file/files.
"""
import os
import sys

# default is always in the order of: lines\tc\tbytes
# @TODO handle standard in

class WC:
    def __init__(self, files, c_bytes, n_lines, n_chars, n_words):
        self.files = files
        self.c_bytes = c_bytes
        self.n_lines = n_lines
        self.n_chars = n_chars
        self.n_words = n_words

    def wc(self):
        total_c, total_l, total_m, total_w = 0, 0, 0, 0
        for file in self.files:
            if self.c_bytes:
                c = self.count_bytes(file)
            if self.n_lines or self.n_chars or self.n_words:
                l, m, w = self.count_more(file)

            self.output(c, l, m, w, file)
            
            total_c += c
            total_l += l
            total_m += m
            total_w += w
        
        if len(self.files) > 1:
            self.output(total_c, total_l, total_m, total_w, "total")

    def output(self, c, l, m, w, file):
        output = (
        f"{str(l) + "\t" if self.n_lines else ""}"
        f"{str(w) + "\t" if self.n_words else ""}"
        f"{str(c) + "\t" if self.c_bytes else ""}"
        f"{str(m) + "\t" if self.n_chars else ""}"
        f"{file}"
        )
        sys.stdout.write(output + "\n")

    def _c_gen(self, reader):
        b = reader(2**16)
        while b:
            yield b
            b = reader(2**16)

    def count_more(self, file):
        sum_lines = 0
        sum_chars = 0
        sum_words = 0
        try:
            with open(file, "rb") as f:
                c_gen = self._c_gen(f.raw.read)
                for buffer in c_gen:
                    sum_lines += buffer.count(b"\n")
                    b_decoded = buffer.decode("utf-8")
                    sum_chars += len(b_decoded)
                    sum_words += len(b_decoded.split())
        except FileNotFoundError as e:
            print(e)
        except IsADirectoryError as e:
            print(e)

        return sum_lines, sum_chars, sum_words

    def count_bytes(self, file):
        try:
            return os.stat(file).st_size
        except FileNotFoundError as e:
            print(e)
        except IsADirectoryError as e:
            print(e)
