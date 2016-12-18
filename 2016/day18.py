def is_trap(prev_chunk):
    return prev_chunk in ['^^.', '.^^', '..^', '^..']


def next_row(traps):
    prev = '.' + traps + '.'
    next_traps = [is_trap(prev[i:i + 3]) for i in range(len(traps))]
    return ''.join('^' if t else '.' for t in next_traps)


row = '.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....'
safe = row.count('.')
for _ in range(39):
    row = next_row(row)
    safe += row.count('.')
print(safe)
for _ in range(400000-40):
    row = next_row(row)
    safe += row.count('.')
print(safe)