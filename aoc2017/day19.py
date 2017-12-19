def follow(path):
    step_count = 0
    r, c = 0, {col for row, col in path if row == 0}.pop()
    dr, dc = 1, 0
    passed = ''
    while True:
        step_count += 1
        r += dr
        c += dc
        if (r, c) not in path:
            break
        if path[(r, c)] not in '|-+':
            passed += path[(r, c)]
        elif path[(r, c)] == '+':
            if (r + dc, c + dr) in path:
                dr, dc = dc, dr
            elif (r - dc, c - dr) in path:
                dr, dc = -dc, -dr
            else:
                break
    return passed, step_count


if __name__ == '__main__':
    data = {}
    with open('day19.in') as f:
        for row, line in enumerate(f):
            for col, char in enumerate(line):
                if char != ' ' and char != '\n':
                    data[(row, col)] = char
    print('Part 1: {}\nPart 2: {}'.format(*follow(data)))
