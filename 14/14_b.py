import os
from utils import read_lines

def tilt(direction, pattern):
    rows = len(pattern)
    cols = len(pattern[0])

    if direction == 'N':
        for y in range(1, rows):
            rocks_x = [x0 for x0 in range(cols) if pattern[y][x0] == 'O']
            for rock_x in rocks_x:
                new_y = y
                for y0 in reversed(range(y)):
                    if pattern[y0][rock_x] == '.':
                        new_y = y0
                    elif pattern[y0][rock_x] == '#':
                        break
                if new_y != y:
                    pattern[new_y][rock_x] = 'O'
                    pattern[y][rock_x] = '.'
    elif direction == 'S':
        for y in reversed(range(rows - 1)):
            rocks_x = [x0 for x0 in range(cols) if pattern[y][x0] == 'O']
            for rock_x in rocks_x:
                new_y = y
                for y0 in range(y, rows):
                    if pattern[y0][rock_x] == '.':
                        new_y = y0
                    elif pattern[y0][rock_x] == '#':
                        break
                if new_y != y:
                    pattern[new_y][rock_x] = 'O'
                    pattern[y][rock_x] = '.'

    elif direction == 'W':
        for x in range(1, cols):
            rocks_y = [y0 for y0 in range(rows) if pattern[y0][x] == 'O']
            for rock_y in rocks_y:
                new_x = x
                for x0 in reversed(range(x)):
                    if pattern[rock_y][x0] == '.':
                        new_x = x0
                    elif pattern[rock_y][x0] == '#':
                        break
                if new_x != x:
                    pattern[rock_y][new_x] = 'O'
                    pattern[rock_y][x] = '.'

    elif direction == 'E':
        for x in reversed(range(cols - 1)):
            rocks_y = [y0 for y0 in range(rows) if pattern[y0][x] == 'O']
            for rock_y in rocks_y:
                new_x = x
                for x0 in range(x, cols):
                    if pattern[rock_y][x0] == '.':
                        new_x = x0
                    elif pattern[rock_y][x0] == '#':
                        break
                if new_x != x:
                    pattern[rock_y][new_x] = 'O'
                    pattern[rock_y][x] = '.'
    return pattern

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))
pattern = [list(line) for line in lines]

CYCLES = 1000000000
history = {}

i = 0
while i < CYCLES:
    for direction in ('N', 'W', 'S', 'E'):
        pattern = tilt(direction, pattern)

    if str(pattern) in history:
        cycle_size = i - history[str(pattern)]
        i += ((CYCLES - i) // cycle_size) * cycle_size

    history[str(pattern)] = i

    i += 1

rows = len(pattern)
cols = len(pattern[0])

s = 0
for y in range(rows):
    for x in range(cols):
        if pattern[y][x] == 'O':
            s += rows - y

print(s)
