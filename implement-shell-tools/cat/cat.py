import sys

def cat(files, number=False, number_nonblank=False):
    line_number = 1

    for file in files:
        try:
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
        except FileNotFoundError:
            print(f"cat: {file}: No such file or directory")


def main():
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

    if number_nonblank:
        number = False

    if not files:
        print("Usage: python3 cat.py [-n|-b] <files>")
        return

    cat(files, number, number_nonblank)


if __name__ == "__main__":
    main()