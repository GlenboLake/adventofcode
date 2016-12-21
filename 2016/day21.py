from itertools import permutations

with open('day21.txt') as f:
    commands = f.read().splitlines()
simple_commands = '''swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d'''.splitlines()

s = list('abcdefgh')


def parse(s):
    s = list(s)
    for c in commands:
        terms = c.split()
        if terms[0] == 'swap':
            a = s.index(terms[2]) if terms[1] == 'letter' else int(terms[2])
            b = s.index(terms[5]) if terms[4] == 'letter' else int(terms[5])
            s[a], s[b] = s[b], s[a]
        elif terms[0] == 'reverse':
            a = int(terms[2])
            b = int(terms[4])
            s[a:b + 1] = s[a:b + 1][::-1]
        elif terms[0] == 'rotate':
            if terms[1] == 'left':
                amount = int(terms[2])
                s = s[amount:] + s[:amount]
            elif terms[1] == 'right':
                amount = int(terms[2])
                s = s[-amount:] + s[:-amount]
            else:
                amount = s.index(terms[6]) + 1
                if amount >= 5: amount += 1
                amount %= len(s)
                s = s[-amount:] + s[:-amount]
        elif terms[0] == 'move':
            ch = s.pop(int(terms[2]))
            s.insert(int(terms[5]), ch)
    return ''.join(s)


def unscramble(password):
    return [''.join(p) for p in permutations(password) if parse(p) == password]


print('Part 1:', parse('abcdefgh'))
result = unscramble('fbgdceah')
print('Part 2:', result[0])