import os
from utils import read_lines

def get_horizontal_mirror(pattern):
    rows = len(pattern)
    cols = len(pattern[0])

    for row in range(1, rows):
        pairs = [(row - i, row + i - 1) for i in range(1, rows - row + 1) if row - i >= 0]
        if all(pattern[y0][col] == pattern[y1][col] for y0, y1 in pairs for col in range(cols)):
            return row

def get_vertical_mirror(pattern):
    rows = len(pattern)
    cols = len(pattern[0])

    for col in range(1, cols):
        pairs = [(col - i, col + i - 1) for i in range(1, cols - col + 1) if col - i >= 0]
        if all(pattern[row][x0] == pattern[row][x1] for x0, x1 in pairs for row in range(rows)):
            return col

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))
patterns = []
pattern = []
for i, line in enumerate(lines):
    if line == '' or i == len(lines) - 1:
        if line:
            pattern.append(list(line))
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(list(line))

vert = 0
hor = 0

for pattern in patterns:
    rows = len(pattern)
    cols = len(pattern[0])

    horizontal_mirror = get_horizontal_mirror(pattern)
    vertical_mirror = get_vertical_mirror(pattern)

    if horizontal_mirror:
        hor += horizontal_mirror * 100

    if vertical_mirror:
        vert += vertical_mirror

print(hor + vert)