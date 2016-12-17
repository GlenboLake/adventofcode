import hashlib

passcode = 'pvhmgsws'
# passcode = 'ihgpwlah'


def doors(path):
    locks = hashlib.md5((passcode + path).encode()).hexdigest()[:4]
    unlocked = [ch in 'bcdef' for ch in locks]
    return [door for door, unlocked in zip('UDLR', unlocked) if unlocked]


def get_room(path):
    return path.count('D') - path.count('U'), path.count('R') - path.count('L')


def search():
    costs = {'': 0}
    shortest = None
    while True:
        max_cost = max(costs.values())
        paths = [k for k, v in costs.items() if v == max_cost]
        for path in paths:
            if get_room(path) == (3, 3):
                continue
            options = doors(path)
            for opt in options:
                p = path + opt
                x, y = get_room(p)
                if x not in range(4) or y not in range(4):
                    continue
                costs[p] = max_cost + 1
                if x == 3 and y == 3:
                    if shortest is None:
                        shortest = p
        if max_cost == max(costs.values()):
            break
    path_ends = {k: v for k, v in costs.items() if get_room(k) == (3, 3)}
    longest_length = max(path_ends.values())
    return shortest, longest_length


print(search())
