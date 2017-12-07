hierarchy = {}
weights = {}
not_root = set()

for line in open('day7.in'):
    try:
        parent, weight, _, children = line.split(maxsplit=3)
        children = children.split(', ')
        weights[parent] = int(weight[1:-1])
        hierarchy[parent] = set()
        for c in children:
            hierarchy[parent].add(c.strip())
            not_root.add(c.strip())
    except ValueError:
        node, weight = line.split()
        weights[node] = int(weight[1:-1])
        not_root.add(node)

total_weights = {w: weights[w] for w in weights if w not in hierarchy}

remaining = {w for w in weights if w not in total_weights}

offender, correct_answer = None, 0
while remaining:
    confirmed = set()
    for parent in remaining:
        if not all(child in total_weights for child in hierarchy[parent]):
            continue
        total_weight = sum(total_weights[child] for child in hierarchy[parent]) + weights[parent]
        total_weights[parent] = total_weight
        if len(set(total_weights[child] for child in hierarchy[parent])) > 1:
            branch = {child: total_weights[child] for child in hierarchy[parent]}
            wrong_value = [b for b in branch.values() if list(branch.values()).count(b) == 1].pop()
            right_value = [b for b in branch.values() if list(branch.values()).count(b) >= 1].pop()
            offender = [k for k, v in branch.items() if v == wrong_value].pop()
            correct_answer = weights[offender] + right_value - wrong_value
            confirmed = remaining
            break
        confirmed.add(parent)
    remaining -= confirmed

print('Bottom item is', {node for node in hierarchy if node not in not_root}.pop())
print('{} should be {}'.format(offender, correct_answer))
