ring_max = {i: (2 * i + 1) ** 2 for i in range(300)}


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


def sum_squares(n):
    dirs = ((0, 1), (-1, 0), (0, -1), (1, 0))

    d = 0

    squares = {(0, 0): 1}
    r, c = 0, 0
    for i in range(2, n):
        r += dirs[d][0]
        c += dirs[d][1]
        value = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                value += squares.get((r + dr, c + dc), 0)
        squares[(r, c)] = value
        if (r + dirs[(d + 1) % 4][0], c + dirs[(d + 1) % 4][1]) not in squares:
            d = (d + 1) % 4
        if value > n:
            return value


if __name__ == '__main__':
    input_ = 277678
    print('part 1:', count_spaces(input_))
    print('part 2:', sum_squares(input_))
