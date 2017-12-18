from functools import reduce

from aoc2017 import lcm


def calc_sev(layers):
    severity = sum(k * v if k % (2 * (v - 1)) == 0 else 0 for k, v in layers.items())
    return severity


def find_delay(layers):
    cycle_length = reduce(lcm, (2 * (size - 1) for size in layers.values()))
    for delay in range(cycle_length):
        caught = False
        for layer, depth in layers.items():
            cycle = 2 * (depth - 1)
            if (layer + delay) % cycle == 0:
                caught = True
                break
        if not caught:
            return delay


if __name__ == '__main__':
    with open('day13.in') as f:
        layers = dict(map(int, line.split(': ')) for line in f)
    print('Part 1:', calc_sev(layers))
    print('Part 2:', find_delay(layers))
