import sys

args = sys.argv[1:]

number = False
number_nonblank = False
files = []

for arg in args:
    if arg == "-n":
        number = True
    elif arg == "-b":
        number_nonblank = True
    else:
        files.append(arg)

# -b overrides -n
if number_nonblank:
    number = False

line_number = 1

for file in files:
    with open(file, "r") as f:
        for line in f:
            if number_nonblank:
                if line.strip():
                    print(f"{line_number}\t{line}", end="")
                    line_number += 1
                else:
                    print(line, end="")
            elif number:
                print(f"{line_number}\t{line}", end="")
                line_number += 1
            else:
                print(line, end="")