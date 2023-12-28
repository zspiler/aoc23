import os
from copy import deepcopy
import time
from utils import read_lines

def tilt_north():
    global pattern
    pattern_copy = deepcopy(pattern)
    changes = False
    for y in range(1, rows):
        for x in range(cols):
            if pattern[y][x] == 'O':
                if pattern[y-1][x] == '.':
                    pattern_copy[y][x] = '.'
                    pattern_copy[y-1][x] = 'O'
                    changes = True
    pattern = pattern_copy
    return changes

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

pattern = [list(line) for line in lines]

rows = len(pattern)
cols = len(pattern[0])
start = time.time()

while tilt_north():
    pass

s = 0
for y in range(rows):
    for x in range(cols):
        if pattern[y][x] == 'O':
            s += rows - y

print(s)
