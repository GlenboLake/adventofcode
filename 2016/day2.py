moves = {
    'U': {
        1: None,
        2: None,
        3: None,
        4: 1,
        5: 2,
        6: 3,
        7: 4,
        8: 5,
        9: 6
    },
    'D': {
        1: 4,
        2: 5,
        3: 6,
        4: 7,
        5: 8,
        6: 9,
        7: None,
        8: None, 9: None
    },
    'L': {
        1: None, 2: 1, 3: 2,
        4: None, 5: 4, 6: 5,
        7: None, 8: 7, 9: 8
    },
    'R': {
        1: 2, 2: 3, 3: None,
        4: 5, 5: 6, 6: None,
        7: 8, 8: 9, 9: None
    }
}

moves2 = {
    'U': {'3': '1', '6': '2', '7': '3', '8': '4', 'A': '6', 'B': '7', 'C': '8', 'D': 'B'},
    'D': {'1': '3', '2': '6', '3': '7', '4': '8', '6': 'A', '7': 'B', '8': 'C', 'B': 'D'},
    'L': {'3': '2', '4': '3', '6': '5', '7': '6', '8': '7', '9': '8', 'B': 'A', 'C': 'B'},
    'R': {'2': '3', '3': '4', '5': '6', '6': '7', '7': '8', '8': '9', 'A': 'B', 'B': 'C'}
}

pos = 5

# instructions = '''ULL
# RRDDD
# LURDL
# UUUUD'''.splitlines()
with open('day2.txt') as f:
    instructions = f.read().splitlines()

code = []
for line in instructions:
    for direction in line:
        next_pos = moves[direction][pos]
        if next_pos is not None:
            pos = next_pos
    code.append(pos)
print(''.join(map(str, code)))

pos = '5'
code = []
for line in instructions:
    for direction in line:
        next_pos = moves2[direction].get(pos)
        if next_pos is not None:
            pos = next_pos
    code.append(pos)
print(''.join(map(str, code)))
