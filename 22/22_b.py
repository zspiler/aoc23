import os
from functools import cmp_to_key
from collections import defaultdict
from copy import deepcopy
from utils import read_lines

def compare_by_Z(brick1, brick2):
    brick1_zs = [brick1[0][2], brick1[1][2]]
    brick2_zs = [brick2[0][2], brick2[1][2]]

    if min(brick1_zs) < min(brick2_zs):
        return -1
    return 1

def fall():
    global bricks
    for brick in sorted(bricks, key=cmp_to_key(compare_by_Z), reverse=False):
        (x0, y0, z0), (x1, y1, z1), label = brick
        min_z = z0 if z0 < z1 else z1
        x_range = range(x0, x1 + 1)
        y_range = range(y0, y1 + 1)
        z_range = range(z0, z1 + 1)

        required = [(x, y) for x in x_range for y in y_range]
        all_cubes = [(z, y, x) for x in x_range for y in y_range for z in z_range]

        level_brick_can_drop_to = None
        for z in reversed(range(1, min_z)):
            if all([space[z][y][x] == None for (x, y) in required]):
                level_brick_can_drop_to = z
            else:
                break
        if level_brick_can_drop_to:
            for (z0, y0, x0) in all_cubes:
                min_z = z_range[0]
                diff = min_z - level_brick_can_drop_to
                space[z0][y0][x0] = None
                space[z0 - diff][y0][x0] = label


lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))
bricks = []

max_x = 0
max_y = 0
max_z = 0

brick_id = 0
for line in lines:
    a, b = line.split('~')
    x0, y0, z0 = map(int, a.split(','))
    x1, y1, z1 = map(int, b.split(','))

    bricks.append(([x0, y0, z0], [x1, y1, z1], f'{brick_id}'))
    brick_id += 1

    for x in (x0, x1):
        max_x = max(x, max_x)
    for y in (y0, y1):
        max_y = max(y, max_y)
    for z in (z0, z1):
        max_z = max(z, max_z)

space = [[[None for x in range(max_x+1)] for y in range(max_y+1)] for z in range(max_z+1)]

brick_labels = []

for brick in bricks:
    (x0, y0, z0), (x1, y1, z1), label = brick
    brick_labels.append(label)

    if x0 != x1:
        for x in range(x0, x1 + 1):
            space[z0][y0][x] = label
    elif y0 != y1:
        for y in range(y0, y1 + 1):
            space[z0][y][x0] = label
    elif z0 != z1:
        for z in range(z0, z1 + 1):
            space[z][y0][x0] = label

fall()

positions_by_brick = defaultdict(list)
for z in range(max_z + 1):
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            brick = space[z][y][x]
            if brick != '.' and brick:
                positions_by_brick[brick].append((x, y, z))

supported_bricks = defaultdict(set)
supported_by = defaultdict(set)

for brick, v in positions_by_brick.items():
    for (x, y, z) in v:
        if z < len(space):
            above_brick = space[z + 1][y][x]
            if above_brick and above_brick != brick:
                supported_bricks[brick].add(above_brick)
                supported_by[above_brick].add(brick)

brick_labels = list(positions_by_brick.keys())
can_be_disintegrated = deepcopy(brick_labels)
for brick, supported in supported_bricks.items():
    for br in supported:
        flattened_values = [item for sub_list in [v for x in v for k, v in supported_bricks.items() if k != brick] for item in sub_list]
        if br not in flattened_values:
            can_be_disintegrated.remove(brick)
            break

cannot_be_disintegrated = list(set(brick_labels) - set(can_be_disintegrated))

total = 0
for i, brick in enumerate(cannot_be_disintegrated):
    disintegrated = []
    queue = [brick]
    while queue:
        br = queue.pop()

        if br not in disintegrated:
            sup_by = [x for x in list(supported_by[br]) if x != brick and x not in disintegrated]
            if len(sup_by) == 0:
                disintegrated.append(br)
            for s in supported_bricks[br]:
                queue.append(s)
    disintegrated = [x for x in disintegrated if x != brick]
    total += len(disintegrated)
print(total)
