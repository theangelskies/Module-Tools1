import os
import sys

def ls(path=".", show_all=False):
    try:
        files = os.listdir(path)

        for f in files:
            if not show_all and f.startswith("."):
                continue
            print(f)

    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")


def main():
    args = sys.argv[1:]

    show_all = False
    path = "."

    for arg in args:
        if arg == "-a":
            show_all = True
        elif not arg.startswith("-"):
            path = arg

    ls(path, show_all)


if __name__ == "__main__":
    main()