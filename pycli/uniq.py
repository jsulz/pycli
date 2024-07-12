import sys

# @TODO finish step 2


class Uniq:
    def __init__(self, files, c, d, u):
        self.files = files
        self.c = c
        self.u = u
        self.d = d

    def uniq(self):
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

    def print_handler(self, line, count):
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
