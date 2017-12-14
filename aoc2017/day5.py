def navigate(jumps, limit=None):
    jumps = list(jumps)
    i = 0
    count = 0
    while i in range(len(jumps)):
        jump = jumps[i]
        if limit and jump >= limit:
            jumps[i] -= 1
        else:
            jumps[i] += 1
        i += jump
        count += 1
    return count


assert navigate([0, 3, 0, 1, -3]) == 5
assert navigate([0, 3, 0, 1, -3], 3) == 10

nums = list(map(int, open('day5.txt').read().splitlines()))
print('Part 1:', navigate(nums))
print('Part 2:', navigate(nums, 3))
