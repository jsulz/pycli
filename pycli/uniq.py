import sys


class Uniq:
    def __init__(self, files, c, d, u, of):
        self.files = files
        self.c = c
        self.u = u
        self.d = d
        self.of = of

    def uniq(self):
        if isinstance(self.files, list):
            for file in self.files:
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        prev = None
                        count = 0
                        for line in f:
                            if prev != None and prev != line:
                                self.print_handler(prev, count)
                                count = 1
                            else:
                                count += 1
                            prev = line
                        self.print_handler(prev, count)
                except FileNotFoundError as e:
                    print(e)
                except IsADirectoryError as e:
                    print(e)
        else:
            self.handle_stdin()

    def handle_stdin(self):
        prev = None
        count = 0
        for line in self.files:
            if prev != None and prev != line:
                self.print_handler(prev, count)
                count = 1
            else:
                count += 1
            prev = line
        self.print_handler(prev, count)

    def print_handler(self, line, count):
        if not self.of:
            if self.c:
                if self.d and count > 1:
                    sys.stdout.write("\t" + str(count) + " " + line)
                if self.u and count == 1:
                    sys.stdout.write("\t" + str(count) + " " + line)
                if not self.d and not self.u:
                    sys.stdout.write("\t" + str(count) + " " + line)
            if not self.c:
                if self.d and count > 1:
                    sys.stdout.write(line)
                if self.u and count == 1:
                    sys.stdout.write(line)
                if not self.d and not self.u:
                    sys.stdout.write(line)
        else:
            with open(self.of, "a+", encoding="utf-8") as f:
                if self.d and count > 1:
                    f.write("\t" + str(count) + " " + line)
                if self.u and count == 1:
                    f.write("\t" + str(count) + " " + line)
                if not self.d and not self.u:
                    f.write("\t" + str(count) + " " + line)
            if not self.c:
                if self.d and count > 1:
                    f.write(line)
                if self.u and count == 1:
                    f.write(line)
                if not self.d and not self.u:
                    f.write(line)
