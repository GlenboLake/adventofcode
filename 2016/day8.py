screen = [[0] * 50 for _ in range(6)]


def rect(a, b):
    for r in range(b):
        for c in range(a):
            screen[r][c] = 1


def rotate(how, which, amount):
    if how == 'row':
        screen[which] = screen[which][-amount:] + screen[which][:-amount]
    else:
        prev = [screen[r][which] for r in range(6)]
        for r in range(6):
            screen[r][which] = prev[r - amount]


with open('day8.txt') as f:
    instr = f.read().splitlines()

for line in instr:
    command = line.split()
    if command[0] == 'rect':
        rect(*map(int, command[1].split('x', 1)))
    else:  # command[0] == 'rotate':
        rotate(command[1], int(command[2].split('=')[1]), int(command[4]))

print(sum(sum(line) for line in screen))
trans = str.maketrans('01', ' #')
print('\n'.join([''.join(map(str, line)) for line in screen]).translate(trans))
