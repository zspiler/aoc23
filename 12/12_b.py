import os
from utils import read_lines

# PART 2: Recursion + Memoization

def ways(data, gs):
    global memo
    global groups

    if str(data + gs) in memo:
        return memo[str(data + gs)]

    gs = gs.copy()

    if len(data) == 0 and not sum(gs) == 0:
        return 0

    if len(data) == 0 or sum(gs) == 0:
        if data.count('#') > sum(gs):
            return 0
        return 1

    if data[0] == '#':
        if gs[0] == 0:
            return 0
        gs[0] -= 1

        memo[str(data[1:] + gs)] = ways(data[1:], gs)
        return memo[str(data[1:] + gs)]

    elif data[0] == '?':
        memo[str(['#'] + data[1:] + gs)] = ways(['#'] + data[1:], gs)
        memo[str(['.'] + data[1:] + gs)] = ways(['.'] + data[1:], gs)
        return memo[str(['#'] + data[1:] + gs)] + memo[str(['.'] + data[1:] + gs)]

    elif data[0] == '.':
        index_at_original = len(groups) - len(gs)
        if gs[0] != 0 and groups[index_at_original] != gs[0]:
            return 0
        if gs[0] == 0:
            gs = gs[1:]

        memo[str(data[1:] + gs)] = ways(data[1:], gs)
        return memo[str(data[1:] + gs)]

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

memo = {}
N_COPIES = 5
s = 0

for i, line in enumerate(lines):
    memo = {}
    data, groups = line.split()
    data = list(data)
    groups = [int(x) for x in groups.split(',')]

    source_data = data.copy()
    source_groups = groups.copy()
    for i in range(N_COPIES - 1):
        data += ['?']
        data += source_data
        groups += source_groups

    state = data

    s += ways(data, groups)

print(s)