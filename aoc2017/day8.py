from collections import defaultdict


def parse(lines):
    registers = defaultdict(int)
    max_ever = 0
    for line in lines:
        reg, op, diff, _, a, comp, b = line.split()
        condition = "registers['{}'] {} {}".format(a, comp, b)
        if eval(condition):
            if op == 'inc':
                registers[reg] += int(diff)
            else:
                registers[reg] -= int(diff)
        max_ever = max(max_ever, max(registers.values()))
    return registers, max_ever


if __name__ == '__main__':
    with open('day8.in') as f:
        registers, record = parse(f.readlines())
    print('Part 1:', max(registers.values()))
    print('Part 2:', record)
