import sys


class Head:
    def __init__(self, files, n_lines, c_bytes):
        self.files = files
        self.n_lines = n_lines
        self.c_bytes = c_bytes

    # Opens the file and prints out however many lines or bytes have been requested
    def head(self, type="lines"):
        mode = "r"
        if type == "bytes":
            mode += "b"

        for file in self.files:
            if len(self.files) > 1:
                print(f"\n==> {file} <==")
            try:

                with open(file, mode=mode) as f:
                    if type == "bytes":
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
