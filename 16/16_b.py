import os
from copy import deepcopy
from utils import read_lines

def get_next_position(pos, dir):
    y, x = pos
    if dir == 'E':
        return (y, x + 1) if x != cols - 1 else None
    if dir == 'W':
        return (y, x - 1) if x != 0 else None
    if dir == 'N':
        return (y - 1, x) if y != 0 else None
    if dir == 'S':
        return (y + 1, x) if y != rows - 1 else None

def run_beam(position, direction):
    global energized_tiles

    mirror_bounces = {
        '\\': { 'E': 'S', 'W': 'N', 'S': 'E', 'N': 'W' },
        '/': { 'E': 'N', 'W': 'S', 'S': 'W', 'N': 'E' }
    }

    while True:
        if str(str(position) + direction) in visited:
            return

        visited.add(str(str(position) + direction))

        y, x = position

        energized_tiles.add((y, x))

        c = grid[y][x]

        if c == '\\' or c == '/':
            direction = mirror_bounces[c][direction]
        elif c == '-' and (direction == 'N' or direction == 'S'):
            beam_queue.append((position, 'W'))
            beam_queue.append((position, 'E'))
            return
        elif c == '|' and (direction == 'W' or direction == 'E'):
            beam_queue.append((position, 'N'))
            beam_queue.append((position, 'S'))
            return

        position = get_next_position(position, direction)
        if not position:
            return


lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))
grid = [list(line) for line in lines]

rows = len(grid)
cols = len(grid[0])

starting_positions = [
    ((0, 0), 'S'),
    ((0, 0), 'E'),

    ((0, cols - 1), 'S'),
    ((0, cols - 1), 'W'),

    ((rows - 1, 0), 'E'),
    ((rows - 1, 0), 'N'),

    ((rows - 1, cols - 1), 'E'),
    ((rows - 1, cols - 1), 'N'),
]

for x in range(cols):
    starting_positions.append(((0, x), 'S'))
    starting_positions.append(((rows - 1, x), 'N'))

for y in range(rows):
    starting_positions.append(((y, 0), 'E'))
    starting_positions.append(((y, cols - 1), 'W'))

max_energized_tiles = 0

for start in starting_positions:
    energized_tiles = set()
    visited = set()

    beam_queue = [start]
    while beam_queue:
        beam = beam_queue.pop()
        pos, dir = beam
        run_beam(pos, dir)

    if len(energized_tiles) > max_energized_tiles:
        max_energized_tiles = len(energized_tiles)

print(max_energized_tiles)