with open(r'D:\workspace\adventofcode\2017\day13.in') as f:
    layers = dict(map(int, line.split(': ')) for line in f)


def calc_sev(delay):
    severity = sum(k * v if (k + delay) % (2 * (v - 1)) == 0 else 0 for k, v in layers.items())
    if severity == 0 and delay % (2 * (layers[0] - 1)) == 0:
        return -1  # 0 severity, but still caught
    return severity


print('Part 1:', calc_sev(0))
delay = 0
while calc_sev(delay):
    delay += 1
print('Part 2:', delay)