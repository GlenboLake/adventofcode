def part1_sim(num_elves):
    elves = [i + 1 for i in range(num_elves)]

    elf = 0
    while len(elves) > 1:
        try:
            elves.pop(elf + 1)
            elf = (elf + 1) % len(elves)
        except IndexError:
            elves.pop(0)
            elf = 0
    return elves[0]


def part1(num_elves):
    n = 1
    for i in range(1, num_elves + 1):
        n += 2
        if n > i:
            n = 1
    return n


def part2_sim(num_elves):
    elves = [i + 1 for i in range(num_elves)]
    elf = 0
    while len(elves) > 1:
        elf_across = (elf + int(len(elves) / 2)) % len(elves)
        elf_number = elves[elf]
        elves.pop(elf_across)
        elf = (elves.index(elf_number) + 1) % len(elves)
    return elves[0]


def part2(num_elves):
    n = 1
    inc = 0
    for i in range(1, num_elves + 1):
        n += inc
        if i == 2 * n:
            inc = 2
        elif i == n:
            inc = 1 - n  # Set inc so that next n is 1
        elif n == 1:
            inc = 1  # Following a reset to 1, set inc to 1
    return n


# for i in range(1, 20):
#     print(i, part1_sim(i))
print(part1(3012210))
# for i in range(1, 20):
#     print(i, part2_sim(i))
print(part2(3012210))
