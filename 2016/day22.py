import re
from collections import namedtuple
from itertools import permutations

with open('day22.txt') as f:
    f.readline()
    f.readline()
    nodes = [line.split() for line in f.read().splitlines()]
# X, Y, Size, Used, Avail, Use%
nodes = [re.findall(r'[xy](\d+)', node[0]) + node[1:] for node in nodes]

viable = 0
for a, b in permutations(nodes, 2):
    used = int(a[3][:-1])
    avail = int(b[4][:-1])
    if 0 < used < avail:
        viable += 1
print('Part 1:', viable)

Node = namedtuple('Node', 'x y size used avail')
nodes = [Node(int(node[0]), int(node[1]), int(node[2][:-1]), int(node[3][:-1]), int(node[4][:-1])) for node in nodes]
node_map = {(node.x, node.y): node for node in nodes}


def get_adjacent(node):
    x, y = node
    return [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if (x + dx, y + dy) in node_map]


print([node for node in nodes if node.used == 0])

for y in range(25):
    row = []
    for x in range(37):
        if node_map[(x, y)].size > 200:
            row.append('#')
        elif node_map[(x, y)].used == 0:
            row.append('_')
        else:
            row.append('.')
    print(' '.join(row))
