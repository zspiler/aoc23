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

print(sum(hash(str) for str in data))