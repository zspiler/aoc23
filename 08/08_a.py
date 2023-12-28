import os

# path = os.path.join(os.path.dirname(__file__), "example.txt")
path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

steps = list(lines[0])
lines = lines[2:]

graph = {}
for line in lines:
    x = line.split()
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    graph[node] = (left, right)

curr_node = 'AAA'

i = 0
while curr_node != 'ZZZ':
    step = steps.pop(0)
    steps.append(step)

    left, right = graph[curr_node]
    curr_node = left if step == 'L' else right

    i += 1

print(i)