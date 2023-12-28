import os
from itertools import combinations
from utils import read_lines

def find_intersection(stone1pos1, stone1pos2, stone2pos1, stone2pos2):
    x1, y1, _ = stone1pos1
    x2, y2, _ = stone1pos2
    x3, y3, _ = stone2pos1
    x4, y4, _ = stone2pos2
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if d == 0:
        return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d
    return [px, py]

def get_position_in_time(position, velocity, time):
    px, py, _ = position
    vx, vy, _ = velocity
    vz, vz, _ = velocity
    x = px + time * vx
    y = py + time * vy
    z = pz + time * vz
    return x, y, z

def is_intersection_invalid(position, velocity, intersection):
    i_x, i_y = intersection
    px, py, _ = position
    vx, vy, _ = velocity
    if vx > 0 and i_x < px or vx < 0 and i_x > px or vy > 0 and i_y < py or vy < 0 and i_y > py:
        return True
    return False

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

stones = []
for line in lines:
    (px, py, pz), (vx, vy, vz) = map(lambda x: list(map(int, x.split(','))), line.replace(' ','').split('@'))
    stones.append(((px, py, pz), (vx, vy, vz)))

limits = (200000000000000, 400000000000000)

count = 0
for stone1, stone2 in list(combinations(stones, 2)):
    stone1_pos, stone1_vel = stone1
    stone2_pos, stone2_vel = stone2

    intersection = find_intersection(
        stone1_pos,
        get_position_in_time(stone1_pos, stone1_vel, 1),
        stone2_pos,
        get_position_in_time(stone2_pos, stone2_vel, 1)
    )

    if intersection:
        is_out_of_bounds = not (limits[0] <= intersection[0] <= limits[1] and limits[0] <= intersection[1] <= limits[1])
        is_invalid = is_intersection_invalid(stone1_pos, stone1_vel, intersection) or is_intersection_invalid(stone2_pos, stone2_vel, intersection)
        if is_out_of_bounds or is_invalid:
            intersection = None
    if intersection:
        count += 1

print(count)
