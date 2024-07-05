import sys
import fileinput


class Cat:
    def __init__(self, files, n, b):
        self.files = files
        self.n = n
        self.b = b

    def cat(self):
        # If the file is a list, then we know it's not standard input
        # and we can loop over the files and print out the contents
        if isinstance(self.files, list):
            for file in self.files:
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        real_pos = 0
                        for pos, line in enumerate(f):
                            if self.b:
                                if (len(line.split(" "))) > 1:
                                    sys.stdout.write(str(real_pos + 1) + "\t" + line)
                                    real_pos += 1
                                else:
                                    sys.stdout.write("\n")
                            if self.n:
                                sys.stdout.write(str(real_pos + 1) + "\t" + line)
                                real_pos += 1
                            if not self.b and not self.n:
                                sys.stdout.write(line)

                except FileNotFoundError as e:
                    print(e)
                except IsADirectoryError as e:
                    print(e)

        # otherwise this is standard input
        if not isinstance(self.files, list):
            pos = 0
            for line in self.files:
                if self.b:
                    if (len(line.split(" "))) > 1:
                        sys.stdout.write(str(pos + 1) + "\t" + line)
                        pos += 1
                    else:
                        sys.stdout.write("\n")
                if self.n:
                    sys.stdout.write(str(pos + 1) + "\t" + line)
                    pos += 1
                if not self.b and not self.n:
                    sys.stdout.write(line)
