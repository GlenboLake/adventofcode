ring_max = {i: (2 * i + 1) ** 2 for i in range(300)}

input_ = 277678


def count_spaces(n):
    ring = min(k for k, v in ring_max.items() if v >= n)
    max_value = ring * 2
    min_value = ring
    inc = 1
    value = max_value
    i = ring_max[ring]
    while i != n:
        if value in (min_value, max_value):
            inc *= -1
        value += inc
        i -= 1
    return value


print('part 1:', count_spaces(input_))

dirs = ((0, 1), (-1, 0), (0, -1), (1, 0))

d = 0

squares = {(0, 0): 1}
r, c = 0, 0
for i in range(2, input_):
    r += dirs[d][0]
    c += dirs[d][1]
    value = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            value += squares.get((r + dr, c + dc), 0)
    squares[(r, c)] = value
    if (r + dirs[(d + 1) % 4][0], c + dirs[(d + 1) % 4][1]) not in squares:
        d = (d + 1) % 4
    if value > input_:
        print('Part 2:',value)
        break
print()
