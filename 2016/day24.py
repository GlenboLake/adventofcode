from itertools import combinations, permutations

import re

sample = '''###########
#0.1.....2#
#.#######.#
#4.......3#
###########'''.splitlines()

with open('day24.txt') as f:
    ducts = f.read().splitlines()


# ducts = sample

def find_nums():
    locs = {}
    for i, line in enumerate(ducts):
        for m in re.findall(r'[^#.]', line):
            locs[m] = (i, line.index(m))
    return locs


def get_dist(a, b):
    xys = [locs[a]]
    visited = {locs[a]}
    dist = 0
    while True:
        dist += 1
        next_xys = []
        for x, y in xys:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = (x + dx, y + dy)
                if (nx, ny) in visited or nx < 0 or nx >= len(ducts) or ny < 0 or ny >= len(ducts[0]):
                    continue
                there = ducts[nx][ny]
                if there == b:
                    # print("It's",dist)
                    return dist
                elif there != '#':
                    visited.add((nx, ny))
                    next_xys.append((nx, ny))
        xys = next_xys


locs = find_nums()
goals = sorted(locs.keys())[1:]
dists = {tuple(sorted([a, b])): get_dist(a, b) for a, b in combinations(locs.keys(), 2)}


def measure(path):
    dist = 0
    # print(path, len(path))
    for i in range(len(path) - 1):
        # print(dists[tuple(sorted([path[i], path[i + 1]]))])
        dist += dists[tuple(sorted([path[i], path[i + 1]]))]
    return dist


paths = [path for path in permutations(locs.keys(), len(locs)) if path[0] == '0']
print('Part 1', min(measure(path) for path in paths))
print('Part 2', min(measure(list(path)+['0']) for path in paths))