import os

path = os.path.join(os.path.dirname(__file__), "input.txt")
lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

config = { 'red': 12, 'green': 13, 'blue': 14}
ids = []

for i, line in enumerate(lines):
    groups = [foo.strip() for foo in line.split(':')[1].split(';')]

    reds = 0
    greens = 0
    blues = 0

    ids.append(i + 1)
    for group in groups:
        decoded = [foo.strip() for foo in group.split(',')]
        g = [foo.split(' ') for foo in decoded]

        if any(True for count, color in g if int(count) > config[color]):
            ids.pop()
            break

print(sum(ids))