from string import ascii_lowercase


def s(x, dancers):
    return dancers[-x:] + dancers[:-x]


assert s(3, list('abcde')) == list('cdeab')


def x(a, b, dancers):
    dancers[a], dancers[b] = dancers[b], dancers[a]
    return dancers


def p(a, b, dancers):
    ai = dancers.index(a)
    bi = dancers.index(b)
    return x(ai, bi, dancers)


def dance(commands, dancers):
    for c in commands:
        if c[0] == 's':
            dancers = s(int(c[1:]), dancers)
        elif c[0] == 'x':
            a, b = c[1:].split('/')
            dancers = x(int(a), int(b), dancers)
        elif c[0] == 'p':
            a, b = c[1:].split('/')
            dancers = p(a, b, dancers)
    return dancers


def multidance(commands, reps, dancers=list(ascii_lowercase[:16])):
    positions = [dancers.copy()]
    x = None
    for i in range(reps):
        dancers = dance(commands, dancers)
        if dancers in positions:
            x = reps % (i+1)
            break
        positions.append(dancers.copy())
    return ''.join(positions[x])


if __name__ == '__main__':
    dancers = list(ascii_lowercase[:16])
    with open('day16.in') as f:
        commands = f.read().split(',')

    p1 = dance(commands, dancers.copy())
    print('part 1', ''.join(p1))

    p2 = multidance(commands, 1000000000)
    print('part 2', ''.join(p2))
