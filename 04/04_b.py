import os
import re

path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

matches_by_line = {}

for line_num, line in enumerate(lines):
    _, winning, mine = re.split(': | \|', line)
    winning = set(int(num) for num in winning.strip().split())
    mine = set(int(num) for num in mine.strip().split())
    matches_by_line[line_num] = len(winning.intersection(mine))

s = 0
i = 0

copies = [j for j, _ in enumerate(lines)]

while len(copies):
    s += 1
    matches = matches_by_line[i]
    for x in range(i + 1, min(len(lines), i + 1 + matches)):
        copies.append(x)
    i = copies.pop()

print(s)