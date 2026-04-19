import sys

files = sys.argv[1:]

for file in files:
    with open(file, "r") as f:
        for line in f:
            print(line, end="")