keypad1 = '''\
123
456
789'''.splitlines()

keypad2 = '''\
  1
 234
56789
 ABC
  D'''.splitlines()


def find_5(text):
    for row, line in enumerate(text):
        try:
            return row, line.index('5')
        except ValueError:
            pass


def move(position, direction):
    if direction == 'U':
        return position[0] - 1, position[1]
    elif direction == 'D':
        return position[0] + 1, position[1]
    elif direction == 'L':
        return position[0], position[1] - 1
    elif direction == 'R':
        return position[0], position[1] + 1


def get_code(keypad, instructions):
    pos = find_5(keypad)
    code = ''
    for line in instructions:
        for ch in line:
            next_pos = move(pos, ch)
            if any(x < 0 for x in next_pos):
                continue
            try:
                if keypad[next_pos[0]][next_pos[1]] != ' ':
                    pos = next_pos
            except IndexError:
                pass
        code += keypad[pos[0]][pos[1]]
    return code

with open('day2.txt') as f:
    instructions = f.read().splitlines()

print(get_code(keypad1, instructions))
print(get_code(keypad2, instructions))
