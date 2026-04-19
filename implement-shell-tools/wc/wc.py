import sys

file = sys.argv[1]

with open(file, "r") as f:
    content = f.read()

lines = content.count("\n")
words = len(content.split())
chars = len(content)

print(lines, words, chars, file)