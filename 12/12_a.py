import os
from utils import read_lines

def is_valid(data, expected_groups):
    groups = []
    grouping = False
    num_in_group = 0
    for i, c in enumerate(data):
        if c == '#':
            if not grouping:
                grouping = True
                num_in_group = 1
            else:
                num_in_group += 1
        else:
            if grouping:
                grouping = False
                groups.append(num_in_group)
                num_in_group = 0
    if num_in_group:
        groups.append(num_in_group)

    return groups == expected_groups

# naive
def get_num_of_arrangements(data, groups):
    q_count = data.count('?')
    combos = 2 ** q_count

    bins = []
    # 1 = #, 0 = .
    for i in range(combos):
        b = bin(i)[2:].zfill(q_count)
        if b.count('1') == sum(groups) - data.count('#'):
            bins.append(b)

    num_of_arrangements = 0
    for b in bins:
        transformed_data = data.copy()
        q_indexes = [i for i, c in enumerate(transformed_data) if c == '?']

        for i, q_index in enumerate(q_indexes):
            transformed_data[q_index] = '#' if b[i] == '1' else '.'

        if is_valid(transformed_data, groups):
            num_of_arrangements += 1
    return num_of_arrangements

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

s = 0
for i, line in enumerate(lines):
    data, groups = line.split()
    data = list(data)
    groups = [int(x) for x in groups.split(',')]
    s += get_num_of_arrangements(data, groups)

print(s)

