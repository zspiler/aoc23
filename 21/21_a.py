import os
from copy import deepcopy
from math import inf
from utils import read_lines

def get_neighbors(y, x):
    return [(y0, x0) for (y0, x0) in [(y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)] if 0 <= y0 < rows and 0 <= x0 < cols and grid[y0][x0] != '#']

def bfs(node, max_depth=inf):
    queue.append(node)

    depth_queue = [0]
    while queue:
        node = queue.pop(0)
        depth = depth_queue.pop(0)

        if node in visited:
            continue

        visited[node] = depth

        if depth == max_depth:
            continue

        neighbors = get_neighbors(*node)

        for neighbour in neighbors:
            queue.append(neighbour)
            depth_queue.append(depth + 1)

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))
grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0])

start = None
for y in range(rows):
    for x in range(cols):
        if grid[y][x] == 'S':
            start = (y, x)
            break

queue = []
visited = {}

bfs(start, 64)

s = 0
path = deepcopy(grid)
for (y, x), level in visited.items():
    if level % 2 == 0:
        path[y][x] = 'o'
        s += 1

print(s)