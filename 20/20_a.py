import os
from utils import read_lines

def press_button():
    queue = [(x, 'low', 'broadcaster') for x in destinations['broadcaster']]
    high_count = 0
    low_count = 1 + len(queue)

    while queue:
        module_name, pulse, source = queue.pop(0)
        if module_name not in modules:
            continue

        module_type, module_data = modules[module_name]
        next_modules = destinations[module_name]

        if module_type == '%':
            if pulse == 'high':
                continue
            modules[module_name][1] = (1 if modules[module_name][1] == 0 else 0)
            next_pulse = 'high' if modules[module_name][1] == 1 else 'low'
        else:
            modules[module_name][1][source] = pulse
            next_pulse = 'low' if all([last_pulse == 'high' for last_pulse in modules[module_name][1].values()]) else 'high'

        if next_pulse == 'high':
            high_count += len(next_modules)
        else:
            low_count += len(next_modules)

        for m in next_modules:
            queue.append((m, next_pulse, module_name))

    return high_count, low_count

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

modules = {}
destinations = {}

for i, line in enumerate(lines):
    module, destination = line.split(' -> ')

    if module == 'broadcaster':
        destinations[module] = destination.split(', ')
    else:
        name = module[1:]
        if '%' in module:
            modules[name] = ['%', 0]
        else:
            modules[name] = ['&', {}]
        destinations[name] = destination.split(', ')

for k, v in destinations.items():
    for destination in v:
        if destination in modules and modules[destination][0] == '&':
            modules[destination][1][k] = 'low'

total_high_count = 0
total_low_count = 0
for i in range(1000):
    high_count, low_count = press_button()
    total_high_count += high_count
    total_low_count += low_count

print(total_low_count * total_high_count)