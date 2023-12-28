import os
from utils import read_lines

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

data = lines[0].split(',')
def hash(s):
    val = 0
    for c in s:
        code = ord(c)
        val += code
        val *= 17
        val %= 256
    return val

boxes = [[] for i in range(256)]

for command in data:
    if '=' in command:
        lens_label, focal_len = command.split('=')
        box_index = hash(lens_label)
        box = boxes[box_index]

        lens_w_same_label = next(((label, foc) for label, foc in box if label == lens_label), None)
        if lens_w_same_label:
            index = box.index(lens_w_same_label)
            box[index] = (lens_label, focal_len)
        else:
            box.append((lens_label, focal_len))
    else:
        lens_label = command.split('-')[0]
        box_index = hash(lens_label)
        box = boxes[box_index]

        lens_w_same_label = next(((label, foc) for label, foc in box if label == lens_label), None)
        if lens_w_same_label:
            boxes[box_index] = [(label, foc) for label, foc in box if label != lens_label]

s = 0
for i, box in enumerate(boxes):
    for lens_label, foc_len in box:
        power = (i + 1) * (box.index((lens_label, foc_len)) + 1) * int(foc_len)
        s += power

print(s)