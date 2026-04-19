import os
import sys

args = sys.argv[1:]

path = "."

for arg in args:
    if not arg.startswith("-"):
        path = arg

files = os.listdir(path)

for f in files:
    print(f)