blocked_ranges = []
with open('day20.txt') as f:
    for line in f.read().splitlines():
        start, end = map(int, line.split('-', 1))
        blocked_ranges.append((start, end))
blocked_ranges = sorted(blocked_ranges)


def part1(ranges):
    lowest = 0
    for start, end in ranges:
        if start > lowest:
            return lowest
        else:
            lowest = max(lowest, end + 1)
    return lowest


def part2(ranges):
    count = 0
    low, high = ranges[0]
    for a, b in ranges:
        if a > high + 1:
            # New range; add the last to our total
            count += high - low + 1
            low, high = a, b
        else:
            # Same range; extend it
            high = max(b, high)
    return 4294967296 - count - (high - low + 1)


print(part1(blocked_ranges))
print(part2(blocked_ranges))
