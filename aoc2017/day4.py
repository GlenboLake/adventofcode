input_ = open('day4.in').read().splitlines()


def part_1(lines):
    return sum(map(lambda line: int(len(line.split()) == len(set(line.split()))), lines))


def part_2(lines):
    return sum(map(lambda line: int(len(line.split()) == len({tuple(sorted(word)) for word in line.split()})), lines))

if __name__ == '__main__':
    print('Part 1:', part_1(input_))
    print('Part 2:', part_2(input_))
