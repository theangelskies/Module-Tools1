import os
import sys

args = sys.argv[1:]

show_all = False
path = "."

for arg in args:
    if arg == "-a":
        show_all = True
    elif not arg.startswith("-"):
        path = arg

files = os.listdir(path)

for f in files:
    if not show_all and f.startswith("."):
        continue
    print(f)