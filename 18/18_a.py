import os
from utils import read_lines

def flood_fill(node):
    queue = [node]
    while queue:
        node = queue.pop()
        y, x = node
        grid[y][x] = '#'
        neighbours = [(y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1)]
        for n_y, n_x in neighbours:
            if grid[n_y][n_x] != '#':
                queue.append((n_y, n_x))

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

y = 0
x = 0
path = []
for line in lines:
    direction, steps, _ = line.split(' ')
    for i in range(int(steps)):
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y -= 1
        elif direction == 'D':
            y += 1

        path.append((y, x))

# adjust
min_y = min(y for y, _ in path)
min_x = min(x for _, x in path)
path = [(y - min_y, x - min_x) for y, x in path]

max_y = max(y for y, _ in path)
max_x = max(x for _, x in path)

cols = max_x + 1
rows = max_y + 1
grid = [['.' for x in range(cols)] for y in range(rows)]

for y, x in path:
    grid[y][x] = '#'

flood_fill((1, 60))

s = sum(grid[y].count('#') for y in range(rows))
print(s)