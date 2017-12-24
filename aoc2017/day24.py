import time


def solve(blocks):
    new_bridges = [[block] for block in blocks if 0 in block]
    strongest = 0
    longest_strength = 0
    while new_bridges:
        bridges = new_bridges
        new_bridges = []
        for bridge in bridges:
            new_bridges.extend(list(extend(bridge, blocks)))
        if new_bridges:
            longest_strength = max(bridge_strength(bridge) for bridge in new_bridges)
            strongest = max(strongest, longest_strength)
    return strongest, longest_strength


def bridge_strength(bridge):
    return sum(map(sum, bridge))


assert bridge_strength([(0, 1), (1, 10), (10, 9)]) == 31


def extend(bridge, blocks):
    unused = list(filter(lambda b: b not in bridge and b[::-1] not in bridge, blocks))
    for block in unused:
        if bridge[-1][1] == block[0]:
            yield bridge + [block]
        elif bridge[-1][1] == block[1]:
            yield bridge + [block[::-1]]


if __name__ == '__main__':
    start = time.time()
    block_list = []
    with open('day24.in') as f:
        for line in f:
            block_list.append(tuple(map(int, line.split('/'))))
    block_list = [(a, b) if a < b else (b, a) for a, b in block_list]

    print('Part 1: {}\nPart 2: {}'.format(*solve(block_list)))
    print(f'Solved in {time.time() - start}')
