slots = [5, 13, 17, 3, 19, 7, 11]
positions = [2, 7, 10, 2, 9, 0, 0]

t = 0

solution = [(-i) % s for i, s in enumerate(slots, start=1)]
# print(solution)

p1 = 0
p2 = 0

while not p1 or not p2:
    # print(positions)
    t += 1
    positions = [(p + 1) % s for p, s in zip(positions, slots)]
    if not p1 and positions[:-1] == solution[:-1]:
        p1 = t
    if not p2 and positions == solution:
        p2 = t
print(p1)
print(p2)
