import os
import itertools

# path = os.path.join(os.path.dirname(__file__), "example.txt")
path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

rows = len(lines)
cols = len(lines[0])

image = [list(line) for line in lines]
empty_rows = [y for y in range(rows) if all(image[y][x0] == '.' for x0 in range(cols))]
empty_cols = [x for x in range(cols) if all(image[y0][x] == '.' for y0 in range(rows))]

rows = len(image)
cols = len(image[0])

galaxies = []
for y in range(rows):
    for x in range(cols):
        if image[y][x] == '#':
            galaxies.append((y, x))

s = 0

for source, destination in itertools.combinations(galaxies, 2):
    y0, x0 = source
    y1, x1 = destination
    dy = abs(y1 - y0)

    for r in empty_rows:
        if min(y0, y1) < r < max(y0, y1):
            dy += 1000000 - 1

    dx = abs(x1 - x0)

    for c in empty_cols:
        if min(x0, x1) < c < max(x0, x1):
            dx += 1000000 - 1

    shortest_path = dy + dx
    s += shortest_path

print(s)