import sys

args = sys.argv[1:]

count_lines = False
count_words = False
count_chars = False

files = []

for arg in args:
    if arg == "-l":
        count_lines = True
    elif arg == "-w":
        count_words = True
    elif arg == "-c":
        count_chars = True
    else:
        files.append(arg)

if not (count_lines or count_words or count_chars):
    count_lines = count_words = count_chars = True

total_l = total_w = total_c = 0

for file in files:
    with open(file, "r") as f:
        content = f.read()

    lines = content.count("\n")
    words = len(content.split())
    chars = len(content)

    total_l += lines
    total_w += words
    total_c += chars

    output = []
    if count_lines:
        output.append(str(lines))
    if count_words:
        output.append(str(words))
    if count_chars:
        output.append(str(chars))

    print(" ".join(output), file)

if len(files) > 1:
    output = []
    if count_lines:
        output.append(str(total_l))
    if count_words:
        output.append(str(total_w))
    if count_chars:
        output.append(str(total_c))

    print(" ".join(output), "total")