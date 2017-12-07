input_ = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]


def realloc(init):
    current = init.copy()
    count = len(init)
    states = [init]
    while True:
        new_state = current.copy()
        i = current.index(max(current))
        value = current[i]
        new_state[i] = 0
        for j in range(value):
            new_state[(i + j + 1) % count] += 1
        if new_state in states:
            break
        states.append(new_state)
        current = new_state
    return len(states), len(states) - states.index(new_state)


assert realloc([0, 2, 7, 0]) == (5, 4)
print('Part 1: {}\nPart 2: {}'.format(*realloc(input_)))
