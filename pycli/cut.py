import sys


class Cut:
    def __init__(self, files, f, d):
        self.files = files
        if len(f) == 1:
            self.f = int(f) - 1
        else:
            if "," in f:
                list_f = f.split(",")
            else:
                list_f = f.split(" ")
            self.f = [int(f) - 1 for f in list_f]
        self.d = d

    def cut(self):
        if isinstance(self.files, list):
            for file in self.files:
                # open the file - bail if it doesn't exist
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        # read each line
                        for line in f:
                            self.split_lines(line)

                except FileNotFoundError as e:
                    print(e)
                except IsADirectoryError as e:
                    print(e)

        else:
            self.handle_stdin()

    def handle_stdin(self):
        for line in self.files:
            self.split_lines(line)

    def split_lines(self, line):
        # Split the line using the delimiter
        split_line = line.rstrip().split(self.d)
        if len(split_line) > 1:
            # Grap the fth element - is zero indexed, but user input
            # is provided as non-zero indexed
            if isinstance(self.f, int):
                sys.stdout.write(split_line[self.f] + "\n")
            if isinstance(self.f, list):
                output = []
                for index in self.f:
                    output.append(split_line[index])
                sys.stdout.write(",".join(output) + "\n")
        else:
            sys.stdout.write(line)

    def to_stdout(self, output):
        for item in output:
            sys.stdout.write(item + "\n")
