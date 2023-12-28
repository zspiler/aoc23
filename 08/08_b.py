import os
import math

path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

all_steps = list(lines[0])
lines = lines[2:]

graph = {}
for line in lines:
    x = line.split()
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    graph[node] = (left, right)


current_nodes = [node for node in graph.keys() if node[-1] == 'A']

steps_required = []

for i, node in enumerate(current_nodes):
    curr_node = node
    steps = all_steps.copy()
    j = 0

    while curr_node[-1] != 'Z':
        step = steps.pop(0)
        steps.append(step)

        j += 1

        left, right = graph[curr_node]
        curr_node = left if step == 'L' else right

    steps_required.append(j)

print(math.lcm(*steps_required))

