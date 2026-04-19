import sys

files = sys.argv[1:]

total_lines = total_words = total_chars = 0

for file in files:
    with open(file, "r") as f:
        content = f.read()

    lines = content.count("\n")
    words = len(content.split())
    chars = len(content)

    total_lines += lines
    total_words += words
    total_chars += chars

    print(lines, words, chars, file)

if len(files) > 1:
    print(total_lines, total_words, total_chars, "total")