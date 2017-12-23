from collections import defaultdict
from math import sqrt


def part1(prog):
    registers = defaultdict(int)
    i = 0
    muls = 0

    def get(value):
        try:
            return int(value)
        except ValueError:
            return registers[value]

    while True:
        try:
            inst = prog[i]
        except IndexError:
            break
        cmd, *args = inst.split()
        if cmd == 'set':
            registers[args[0]] = get(args[1])
            i += 1
        elif cmd == 'sub':
            registers[args[0]] -= get(args[1])
            i += 1
        elif cmd == 'mul':
            registers[args[0]] *= get(args[1])
            i += 1
            muls += 1
        elif cmd == 'jnz':
            if get(args[0]) != 0:
                i += get(args[1])
            else:
                i += 1
        else:
            raise NotImplementedError(cmd)
    return muls


def part2():
    """Pseudocode for assembly:

    for b = 108100 to 125100 by 17:
        let f=1
        for d = 2 to b, e = 2 to b:
            if d*e == b, let f=0
        if f==0, h+=1

    i.e., for values of b from 108100 to 125100 in increments of 17,
    count the number of composite values
    """
    h = 0
    for b in range(108100, 125101, 17):
        for factor in range(2, int(sqrt(b))):
            if b % factor == 0:
                h += 1
                break
    return h


if __name__ == '__main__':
    with open('day23.in') as f:
        input_ = f.read().splitlines()
    print("Part 1:", part1(input_))
    print("Part 2:", part2())
