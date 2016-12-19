def is_trap(prev_chunk):
    return prev_chunk in ['^^.', '.^^', '..^', '^..']


def next_row(traps):
    prev = '.' + traps + '.'
    next_traps = [is_trap(prev[i:i + 3]) for i in range(len(traps))]
    return ''.join('^' if t else '.' for t in next_traps)


row = '.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....'
safe = row.count('.')
for i in range(40000):
    if i + 1 in (40, 40000):
        print(safe)
    row = next_row(row)
    safe += row.count('.')
