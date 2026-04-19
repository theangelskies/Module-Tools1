import sys

args = sys.argv[1:]

number = False
files = []

for arg in args:
    if arg == "-n":
        number = True
    else:
        files.append(arg)

line_number = 1

for file in files:
    with open(file, "r") as f:
        for line in f:
            if number:
                print(f"{line_number}\t{line}", end="")
                line_number += 1
            else:
                print(line, end="")