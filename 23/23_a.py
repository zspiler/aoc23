import os
import sys
from collections import defaultdict
from utils import read_lines

def neighbour_is_valid(neighbour, node):
    y, x = node
    if grid[y][x] == '<':
        return neighbour == (y, x - 1)
    elif grid[y][x] == '>':
        return neighbour == (y, x + 1)
    elif grid[y][x] == 'v':
        return neighbour == (y + 1, x)
    return True
def get_neighbors(node):
    y, x = node
    return [(y0, x0) for (y0, x0) in [(y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)] if
                     0 <= y0 < rows and 0 <= x0 < cols and grid[y0][x0] != '#' and neighbour_is_valid((y0, x0), node)]

def dfs(node, path):
    global max_path_len
    y, x = node

    max_path_len_per_node[node] = max(max_path_len_per_node[node], len(path))
    if len(path) < max_path_len_per_node[node]:
        return

    if node == goal:
        max_path_len = max(max_path_len, len(path))
        return

    neighbors = [n for n in get_neighbors((y, x))]

    for neighbour in neighbors:
        # NOTE: we need to check current path, not global 'visited'
        if neighbour not in path:
            dfs(neighbour, path + [node])

sys.setrecursionlimit(10000)

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

rows = len(lines)
cols = len(lines[0])

grid = [[c for c in list(line)] for line in lines]
start = (0, 1)
goal = (rows - 1, cols - 2)

max_path_len_per_node = defaultdict(int)
max_path_len = 0
dfs(start, [])

print(max_path_len)