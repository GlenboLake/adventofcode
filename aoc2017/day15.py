from time import time


def seq(seed, mul, mod=1):
    value = seed
    while True:
        value = (value * mul) % 2147483647
        if value % mod == 0:
            yield value


def part1(a, b):
    matches = 0
    A = seq(a, 16807)
    B = seq(b, 48271)
    for _ in range(int(40e6)):
        a = next(A)
        b = next(B)
        if a & 0xffff == b & 0xffff:
            matches += 1
    return matches


def part2(a, b):
    matches = 0
    A = seq(a, 16807, 4)
    B = seq(b, 48271, 8)
    for _ in range(int(5e6)):
        a = next(A)
        b = next(B)
        if a & 0xffff == b & 0xffff:
            matches += 1
    return matches


if __name__ == '__main__':
    start = time()
    print('new:', part1(289, 629))
    print(time() - start)
    start = time()
    print('new:', part2(289, 629))
    print(time() - start)
