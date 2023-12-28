import os

# path = os.path.join(os.path.dirname(__file__), "example.txt")
path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]


def is_pipe(symbol):
    return symbol not in ('.', 'S')

def get_starting_neighbor_pipes(y, x):
    global graph
    all_neighbour_pipes = [(y1, x1) for (y1, x1) in [(y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1)] if
                           0 <= y1 < rows and 0 <= x1 < cols and graph[y1][x1] != '.']
    neighbour_pipes = []

    for (pipe_y, pipe_x) in all_neighbour_pipes:
        pipe = graph[pipe_y][pipe_x]

        if pipe_y == y - 1 and pipe_x == x and pipe in ('|', '7', 'F'):  # up
            neighbour_pipes.append((pipe_y, pipe_x))

        if pipe_y == y + 1 and pipe_x == x and pipe in ('|', 'J', 'L'):  # down
            neighbour_pipes.append((pipe_y, pipe_x))

        if pipe_y == y and pipe_x == x + 1 and pipe in ('-', 'J', '7'):  # right
            neighbour_pipes.append((pipe_y, pipe_x))

        if pipe_y == y and pipe_x == x - 1 and pipe in ('-', 'F', 'L'):  # left
            neighbour_pipes.append((pipe_y, pipe_x))
    return neighbour_pipes


def get_next_pipe(y, x):
    global graph
    global visited

    pipe = graph[y][x]

    directions = ['N', 'E', 'S', 'W']
    pipe_connections = {
        '|': ['N', 'S'],
        '-': ['E', 'W'],
        'L': ['N', 'E'],
        'J': ['N', 'W'],
        '7': ['S', 'W'],
        'F': ['S', 'E'],
    }

    neighbors = []
    connections = pipe_connections[pipe]
    for connection in connections:
        y0, x0 = y, x
        if connection == 'N' and y > 0:
            y0 = y - 1
        elif connection == 'S' and y < rows:
            y0 = y + 1
        elif connection == 'E' and x < cols:
            x0 = x + 1
        elif connection == 'W' and x > 0:
            x0 = x - 1
        neighbor = graph[y0][x0]
        if is_pipe(neighbor) and directions[(directions.index(connection) + 2) % len(directions)] in pipe_connections[neighbor]:
            neighbors.append((y0, x0))

    if len(neighbors) == 1:
        return neighbors[0]

    if all(neighbor in visited for neighbor in neighbors):
        return None

    return neighbors[0] if neighbors[1] in visited else neighbors[1]

graph = [list(line) for line in lines]
rows = len(graph)
cols = len(graph[0])

starting_point = None
for y in range(rows):
    if 'S' in graph[y]:
        starting_point = (y, graph[y].index('S'))
        break

node = get_starting_neighbor_pipes(*starting_point)[0]
visited = set()

while node != starting_point:
    visited.add(node)
    y, x = node

    node = get_next_pipe(y, x)

    if not node:
        break


print((len(visited) + 1) // 2)