import os

# path = os.path.join(os.path.dirname(__file__), "example.txt")
path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

histories = [[int(a) for a in line.split()] for line in lines]

next_vals = []

for h in histories:
    sequences = [h]
    j = 0
    while not all(a == 0 for a in sequences[-1]):
        row = sequences[j]
        j += 1
        next_row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        sequences.append(next_row)

    sequences[-1].append(0)
    for k in reversed(range(len(sequences) - 1)):
        sequences[k].append(sequences[k][-1] + sequences[k + 1][-1])

    next_vals.append(sequences[0][-1])


print(sum(next_vals))