jump = 367


def part1():
    pos = 0
    items = [0]
    for i in range(1, 2018):
        pos = (pos + jump) % len(items) + 1
        items.insert(pos, i)
    return items[pos + 1]


def part2():
    value = 0
    pos = 0
    for i in range(1, 50000001):
        pos = (pos + jump) % i + 1
        if pos == 1:
            value = i
    return value


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
