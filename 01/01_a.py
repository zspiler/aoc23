import os

path = os.path.join(os.path.dirname(__file__), "input.txt")
lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

s = 0
for line in lines:
    first, last = None, None
    for c in line:
        if '0' < c <= '9':
            if not first:
                first = c
            last = c
    s += int(f'{first}{last}')
print(s)