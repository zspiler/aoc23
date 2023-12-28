import os

path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

histories = [[int(a) for a in line.split()] for line in lines]

left_most_vals = []

for h in histories:
    sequences = [h]
    j = 0
    while not all(a == 0 for a in sequences[-1]):
        row = sequences[j]
        j += 1
        next_row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        sequences.append(next_row)

    sequences[-1].insert(0, 0)

    for k in reversed(range(len(sequences) - 1)):
        d = sequences[k][0] - sequences[k + 1][0]
        sequences[k].insert(0, d)

    left_most_vals.append(sequences[0][0])

print(sum(left_most_vals))