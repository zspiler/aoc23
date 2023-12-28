import os
import re

path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

s = 0
for line in lines:
    _, winning, mine = re.split(': | \|', line)
    winning = set(int(num) for num in winning.strip().split())
    mine = set(int(num) for num in mine.strip().split())

    matching = winning.intersection(mine)
    if len(matching):
        points = 2 ** (len(matching) - 1)
        s += points

print(s)
