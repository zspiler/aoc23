import os
import re

path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

def remove_num_from_coords(y, x):
    global coords
    for x in range(x, width):
        if not coords[y][x] or not type(coords[y][x]) == int:
            return
        coords[y][x] = None

width = len(lines[0])
height = len(lines)

coords = [[None for i in range(width)] for j in range(height)]
for y, line in enumerate(lines):
    for match in re.finditer("\d+", line):
        for x in range(match.span()[0], match.span()[1]):
            coords[y][x] = int(match.group(0))
s = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if not c.isdigit() and c != '.':
            valid_neighbours = [(y1, x1) for y1 in range(y - 1, y + 2) for x1 in range(x - 1, x + 2) if (x1 != x or y1 != y) and 0 <= y < height and 0 <= x < width]

            for (y1, x1) in valid_neighbours:
                if coords[y1][x1]:
                    num = coords[y1][x1]
                    s += num
                    remove_num_from_coords(y1, x1)

print(s)