from collections import defaultdict

registers = defaultdict(int)
max_ever = 0
with open('day8.in') as f:
    for line in f:
        reg, op, diff, _, a, comp, b = line.split()
        condition = "registers['{}'] {} {}".format(a, comp, b)
        if eval(condition):
            if op == 'inc':
                registers[reg] += int(diff)
            else:
                registers[reg] -= int(diff)
        max_ever = max(max_ever, max(registers.values()))

print('Part 1:', max(registers.values()))
print('Part 2:', max_ever)
