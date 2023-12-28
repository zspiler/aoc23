import os

path = os.path.join(os.path.dirname(__file__), "input.txt")
lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

config = { 'red': 12, 'green': 13, 'blue': 14}
ids = []

s = 0
for i, line in enumerate(lines):
    groups = [x.strip() for x in line.split(':')[1].split(';')]

    max_per_color = { 'red': 0, 'green': 0, 'blue': 0 }

    for group in groups:
        decoded = [x.strip() for x in group.split(',')]
        g = [x.split(' ') for x in decoded]
        for count, color in g:
            count = int(count)
            if count > max_per_color[color]:
                max_per_color[color] = count

    power = max_per_color['red'] * max_per_color['green'] * max_per_color['blue']
    s += power

print(s)