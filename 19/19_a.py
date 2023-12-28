import os
import re
from utils import read_lines

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

ratings = lines[lines.index('') + 1:]
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

ratings = [
    {k: int(v) for prop in rating[1:-1].split(',') for k, v in (item.split('=') for item in prop.split(','))}
    for rating in ratings
]

accepted = []
for rating in ratings:
    workflow_name = 'in'
    while workflow_name:
        workflow = workflows[workflow_name]

        res = None
        for i, rule in enumerate(workflow):
            if i == len(workflow) - 1:
                res = rule
            else:
                (op1, op, op2), result = rule
                if op == '<' and rating[op1] < int(op2) or op == '>' and rating[op1] > int(op2):
                    res = result
            if res == 'R':
                workflow_name = None
                break
            elif res == 'A':
                accepted.append(rating)
                workflow_name = None
                break
            elif res:
                workflow_name = res
                break

s = sum([sum(rating.values()) for rating in accepted])

print(s)