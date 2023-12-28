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

for i, r in enumerate(empty_rows):
    image.insert(r + i, ['.' for x in range(cols)])

for i, c in enumerate(empty_cols):
    for y in range(len(image)):
        image[y].insert(c + i, '.')

rows = len(image)
cols = len(image[0])

i = 1
galaxies = []
names = {}
for y in range(rows):
    for x in range(cols):
        if image[y][x] == '#':
            galaxies.append((y, x))
            image[y][x] = i
            names[(y, x)] = i
            i += 1

s = 0
for source, destination in itertools.combinations(galaxies, 2):
    y0, x0 = source
    y1, x1 = destination
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    shortest_path = dy + dx
    s += shortest_path
print(s)
