import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

s = 0

for str in lines:
    numbers = []
    for i in range(len(str)):
        c = str[i]
        if '0' < c <= '9':
            numbers.append(int(c))
            continue

        k = 0
        candidates = digit_words
        for search_pos in range(i, len(str)):
            char = str[search_pos]
            if char in [word[k] if k < len(word) else None for word in digit_words]:
                candidates = [word for word in candidates if k < len(word) and word[k] == char]
                if len(candidates) == 1 and k == len(candidates[0]) - 1:
                    numbers.append(digit_words.index(candidates[0])+1)
                    break
            else:
                break
            k += 1
    first = numbers[0]
    last = numbers[-1]
    s += int(f'{first}{last}')

print(s)

