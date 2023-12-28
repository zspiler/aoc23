import os
from utils import read_lines

def get_path():
    y = 0
    x = 0
    path = []
    for line in lines:
        _, _, info = line.split(' ')
        distance = int(info[2:7], 16)
        direction = ['R', 'D', 'L', 'U'][int(info[7:8])]

        for i in range(distance):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1

            path.append((y, x))
    return path

def shoelace_area(nodes):
    s = 0
    for node1, node2 in zip(nodes, nodes[1:]):
        y0, x0 = node1
        y1, x1 = node2
        s += x0 * y1 - x1 * y0
    return 0.5 * abs(s)


"""
We need number of boundary points + interior points.

Pick's theorem - area of (simple) polygon with integer vertex coordinates
Shoelace's formula - area of (simple) polygon with any vertex coordinates
"""

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))
path = get_path()
num_boundary = len(path)
area = shoelace_area(path)
num_interior = area - num_boundary/2 + 1 # Pick's
print(num_boundary + num_interior)