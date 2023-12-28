import os
from copy import deepcopy
from utils import read_lines

def get_horizontal_mirror(pattern, excluding=None):
    rows = len(pattern)
    cols = len(pattern[0])

    for row in range(1, rows):
        pairs = [(row - i, row + i - 1) for i in range(1, rows - row + 1) if row - i >= 0]
        if all(pattern[y0][col] == pattern[y1][col] for y0, y1 in pairs for col in range(cols)) and (not excluding or row != excluding):
            return row

def get_vertical_mirror(pattern, excluding=None):
    rows = len(pattern)
    cols = len(pattern[0])

    for col in range(1, cols):
        pairs = [(col - i, col + i - 1) for i in range(1, cols - col + 1) if col - i >= 0]
        if all(pattern[row][x0] == pattern[row][x1] for x0, x1 in pairs for row in range(rows)) and (not excluding or col != excluding):
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

    found = False

    for row in range(rows):
        if found:
            break
        for col in range(cols):
            pattern_copy = deepcopy(pattern)
            pattern_copy[row][col] = '.' if pattern_copy[row][col] == '#' else '#'

            new_vert = get_vertical_mirror(pattern_copy, vertical_mirror)
            new_horizo = get_horizontal_mirror(pattern_copy, horizontal_mirror)

            if new_vert:
                vertical_mirror = new_vert
                vert += vertical_mirror
                found = True
                break
            if new_horizo:
                horizontal_mirror = new_horizo
                hor += horizontal_mirror * 100
                found = True
                break
print(hor + vert)