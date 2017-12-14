from timeit import timeit

with open('day11.in') as f:
    path = f.read().split(',')


def measure(steps):
    x = y = 0
    max_d = 0
    for step in steps:
        if step == 'n':
            y += 1
        elif step == 's':
            y -= 1
        else:
            if 'e' in step:
                x += 1
            elif 'w' in step:
                x -= 1
            if 'n' in step:
                y += 0.5
            elif 's' in step:
                y -= 0.5
        h = abs(x)
        max_v = h / 2
        d = h + max(0, abs(y) - max_v)
        max_d = max(d, max_d)
    h = abs(x)
    max_v = h / 2
    return h + max(0, abs(y) - max_v), max_d


assert measure(['ne', 'ne', 'ne'])[0] == 3
assert measure(['ne', 'ne', 'sw', 'sw'])[0] == 0
assert measure(['ne', 'ne', 's', 's'])[0] == 2
assert measure(['se', 'sw', 'se', 'sw', 'sw'])[0] == 3


def distance(x, y, z):
    return sum(map(lambda val: val if val > 0 else 0, [x, y, z]))


def measure_xyz(steps):
    x = y = z = max_d = 0
    for step in steps:
        if step == 'n':
            y += 1
            z -= 1
        elif step == 's':
            y -= 1
            z += 1
        elif step == 'ne':
            x += 1
            z -= 1
        elif step == 'sw':
            x -= 1
            z += 1
        elif step == 'nw':
            x -= 1
            y += 1
        elif step == 'se':
            x += 1
            y -= 1
        max_d = max(max_d, distance(x, y, z))
    return distance(x, y, z), max_d


assert measure_xyz(['ne', 'ne', 'ne'])[0] == 3
assert measure_xyz(['ne', 'ne', 'sw', 'sw'])[0] == 0
assert measure_xyz(['ne', 'ne', 's', 's'])[0] == 2
assert measure_xyz(['se', 'sw', 'se', 'sw', 'sw'])[0] == 3

if __name__ == '__main__':
    print('Part 1: {}\nPart 2: {}'.format(*measure(path)))
    print(timeit('measure(path)', setup='from __main__ import measure, path', number=1000))

    print('Part 1: {}\nPart 2: {}'.format(*measure_xyz(path)))
    print(timeit('measure_xyz(path)', setup='from __main__ import measure_xyz, path', number=1000))
