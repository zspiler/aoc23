import os
import networkx as nx
from utils import read_lines

lines = read_lines(os.path.join(os.path.dirname(__file__), 'input.txt'))

edges = set()

for line in lines:
    a, b = line.split(': ')
    key = a
    vals = b.split(' ')
    for v in vals:
        if (key, v) not in edges and (v, key) not in edges:
            edges.add((key, v))

G = nx.Graph(edges)
edges_to_cut = list(nx.minimum_edge_cut(G))
G.remove_edges_from(edges_to_cut)
components = list(nx.connected_components(G))

print(len(components[0])*len(components[1]))