from itertools import permutations

if __name__ == '__main__':
    sheet = open('day2.in').read().splitlines()
    sheet = [list(map(int, row.split())) for row in sheet]

    print('Part 1:', sum(max(row) - min(row) for row in sheet))
    print('Part 2:', sum(a // b for r in sheet for a, b in permutations(r, 2) if a % b == 0))
