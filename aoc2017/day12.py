def find_group(pipes, seed):
    group = {seed}
    new = {seed}
    while new:
        next_new = set()
        for item in new:
            next_new.update(pipes[item])
        new = next_new - group
        group.update(next_new)
    return group


def count_groups(pipes):
    remaining = set(pipes)
    groups = 0
    while remaining:
        groups += 1
        group = find_group(pipes, remaining.pop())
        remaining -= group
    return groups


if __name__ == '__main__':
    pipes = {}

    with open('day12.in') as f:
        for line in f:
            src, _, dsts = line.split(maxsplit=2)
            pipes[int(src)] = set(map(int, dsts.split(', ')))
    print('Part 1:', len(find_group(pipes, 0)))
    print('Part 2:', count_groups(pipes))
