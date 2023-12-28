import os
import re

# path = os.path.join(os.path.dirname(__file__), "example.txt")
path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

seeds = [int(s) for s in lines[0].split(':')[1].split()]
lines = lines[2:]

maps = []
lines = [line for line in lines if len(line) == 0 or line[0].isdigit()]

map_lines = []
for i, line in enumerate(lines):
    if len(line) == 0 or i == len(lines) - 1:
        maps.append(map_lines)
        map_lines = []
    else:
        map_lines.append([int(x) for x in line.split()])

map_names = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location'
]

seed_soil_map = maps[0]

locations = []

for seed in seeds:
    result = seed

    for map_num, map in enumerate(maps):
        print(map_names[map_num])
        for group_num, group in enumerate(map):
            dr_start, sr_start, steps = group
            src_range = range(sr_start, sr_start + steps)
            dest_range = range(dr_start, dr_start + steps)
            if result in src_range:
                index = src_range.index(result)
                result = dest_range[index]
                break
        print()
    locations.append(result)

print(min(locations))


