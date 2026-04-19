import sys

def wc(files, count_l, count_w, count_c):
    total_l = total_w = total_c = 0

    for file in files:
        try:
            with open(file, "r") as f:
                content = f.read()

            lines = content.count("\n")
            words = len(content.split())
            chars = len(content)

            total_l += lines
            total_w += words
            total_c += chars

            output = []
            if count_l:
                output.append(str(lines))
            if count_w:
                output.append(str(words))
            if count_c:
                output.append(str(chars))

            print(" ".join(output), file)

        except FileNotFoundError:
            print(f"wc: {file}: No such file")

    if len(files) > 1:
        output = []
        if count_l:
            output.append(str(total_l))
        if count_w:
            output.append(str(total_w))
        if count_c:
            output.append(str(total_c))

        print(" ".join(output), "total")


def main():
    args = sys.argv[1:]

    count_l = count_w = count_c = False
    files = []

    for arg in args:
        if arg == "-l":
            count_l = True
        elif arg == "-w":
            count_w = True
        elif arg == "-c":
            count_c = True
        else:
            files.append(arg)

    if not (count_l or count_w or count_c):
        count_l = count_w = count_c = True

    wc(files, count_l, count_w, count_c)


if __name__ == "__main__":
    main()