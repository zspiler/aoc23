import os
import re
from copy import deepcopy
from utils import read_lines

def get_fitting_range(condition, ranges, inverse=False):
    key = condition[0]
    op = condition[1]
    value = int(condition[2])

    fitting_ranges = deepcopy(ranges)

    start, end = fitting_ranges[key]
    if op == '<':
        if inverse:
            fitting_ranges[key] = [value, end]
        else:
            fitting_ranges[key] = [start, value - 1]
    elif op == '>':
        if inverse:
            fitting_ranges[key] = [start, value]
        else:
            fitting_ranges[key] = [value + 1, end]
    return fitting_ranges

def num_of_combinations(ranges):
    s = 1
    for start, end in ranges.values():
        s *= end + 1 - start
    return s

def explore(workflow_name, ranges):
    global total
    workflow = workflows[workflow_name]
    for i, rule in enumerate(workflow):
        if isinstance(rule, tuple):
            ranges_copy = deepcopy(ranges)
            condition, res = rule

            pos_ranges = get_fitting_range(condition, ranges_copy)
            neg_ranges = get_fitting_range(condition, ranges_copy, True)

            if pos_ranges:
                if res == 'A':
                    if pos_ranges:
                        total += num_of_combinations(pos_ranges)
                elif res != 'R':
                    explore(res, pos_ranges)
            if neg_ranges:
                ranges = neg_ranges
        else:
            res = rule
            if res == 'A':
                total += num_of_combinations(ranges)
            elif res != 'R':
                explore(res, ranges)


lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

workflows = {}

for workflow in lines[:lines.index('')]:
    pattern = r'(\w+)\{([^}]+)\}'
    match = re.match(pattern, workflow)
    workflow_name = match.group(1)
    rules = match.group(2).split(',')

    parsed = []
    for rule in rules[:-1]:
        condition, result = rule.split(':')
        condition = re.split(r'([><])', condition)
        parsed.append((condition, result))

    parsed.append(rules[-1])
    workflows[workflow_name] = parsed

workflow_name = 'in'
workflow = workflows[workflow_name]

ranges = {
    'm': [1, 4000],
    'x': [1, 4000],
    'a': [1, 4000],
    's': [1, 4000],
}

total = 0
explore('in', ranges)
print(total)
