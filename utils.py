def read_lines(path):
    with open(path, "r") as file:
        return file.read().splitlines()