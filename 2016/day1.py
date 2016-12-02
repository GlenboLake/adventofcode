pos = (0, 0)
direction = (0, 1)
visited = {pos}
first_revisit = None


def turn(LR):
    global direction
    if LR == 'L':
        direction = (-direction[1], direction[0])
    elif LR == 'R':
        direction = (direction[1], -direction[0])


with open('day1.txt') as f:
    steps = f.read().split(', ')

for step in steps:
    d, num = step[0], int(step[1:])
    turn(d)
    for _ in range(num):
        pos = (pos[0] + direction[0], pos[1] + direction[1])
        if pos in visited and first_revisit is None:
            first_revisit = pos
        visited.add(pos)

print(first_revisit)
print(pos)

print(abs(pos[0]) + abs(pos[1]))
print(abs(first_revisit[0]) + abs(first_revisit[1]))
