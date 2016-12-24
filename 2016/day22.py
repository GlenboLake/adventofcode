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

empty = [(node.x,node.y) for node in nodes if node.used == 0]
avg_size = sum(node.size for node in nodes) / len(nodes)
walls = [xy for xy, node in node_map.items() if node.size > 2 * avg_size]


def shortest_path(start, end, xrange, yrange, walls):
    visited = {start}
    dist = 0
    new_points = [start]
    while end not in visited:
        iter_over = new_points.copy()
        new_points = []
        for x, y in iter_over:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                pt = (x + dx, y + dy)
                if pt[0] not in xrange or pt[1] not in yrange or pt in walls:
                    continue
                if pt not in visited:
                    new_points.append(pt)
                    visited.add(pt)
        dist += 1
    return dist


def print_map(node_map):
    ymax = max(node_map.keys(), key=lambda pt: pt[1])[1] + 1
    xmax = max(node_map.keys(), key=lambda pt: pt[0])[0] + 1
    for y in range(ymax):
        row = []
        for x in range(xmax):
            if node_map[(x, y)].size > 200:
                row.append('#')
            elif node_map[(x, y)].used == 0:
                row.append('_')
            else:
                row.append('.')
        print(' '.join(row))


# print_map(node_map)
xs = {node.x for node in nodes}
ys = {node.y for node in nodes}
prep = shortest_path(empty[0], (max(xs)-1, 0), xs, ys, walls)
print('Part 2:',prep+1+(max(xs)-1)*5)
