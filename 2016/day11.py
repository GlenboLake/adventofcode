import copy
from collections import namedtuple
from itertools import combinations, chain

Pair = namedtuple('Pair', ('chip_floor', 'generator_floor'))
State = namedtuple('State', ('elevator', 'floors'))
AnonymousState = namedtuple('AnonymousState', ('elevator', 'pairs'))


def anonymize_state(state):
    stuff = {item: floor for floor, items in enumerate(state.floors) for item in items}
    elements = set([x[:-1] for x in stuff])
    pairs = tuple(sorted(Pair(stuff[e + 'M'], stuff[e + 'G']) for e in elements))
    return AnonymousState(state.elevator, pairs)


def is_safe(state):
    if state is None:
        return False
    for floor in range(4):
        chips = [x[:-1] for x in state.floors[floor] if x[-1] == 'M']
        generators = [x[:-1] for x in state.floors[floor] if x[-1] == 'G']
        if generators:
            for chip in chips:
                if chip not in generators:
                    return False
    return True


def move(state, payload, direction):
    new_floor = state.elevator + direction
    if new_floor not in range(4):
        return None
    floors = copy.deepcopy(state.floors)
    for item in payload:
        floors[state.elevator].remove(item)
        floors[new_floor].append(item)
    return State(new_floor, floors)


def solve(initial_state):
    target_state = anonymize_state(State(3, [[], [], [], chain(*initial_state.floors)]))
    seen_states = {anonymize_state(initial_state)}
    new_states = [initial_state]

    moves = 0
    while target_state not in seen_states:
        states_to_expand = new_states
        new_states = []
        for state in states_to_expand:
            items_on_floor = state.floors[state.elevator]
            payloads = chain(combinations(items_on_floor, 2), combinations(items_on_floor, 1))
            for p in payloads:
                for direction in 1, -1:
                    new_state = move(state, p, direction)
                    if new_state is None or anonymize_state(new_state) in seen_states:
                        continue
                    if is_safe(new_state):
                        new_states.append(new_state)
                        seen_states.add(anonymize_state(new_state))
        moves += 1
    return moves


part1 = State(0, [['PmM', 'PmG'], ['CoG', 'CmG', 'RuG', 'PuG'], ['CoM', 'CmM', 'RuM', 'PuM'], []])
part2 = State(0, [['EleriumM', 'EleriumG', 'DilithiumM', 'DilithiumG', 'PmM', 'PmG'], ['CoG', 'CmG', 'RuG', 'PuG'],
                  ['CoM', 'CmM', 'RuM', 'PuM'], []])

print(solve(part1))
print(solve(part2))
