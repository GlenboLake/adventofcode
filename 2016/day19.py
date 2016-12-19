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
    inc = 1
    prev_max = 1
    for i in range(1, num_elves+2):  # Not sure why I need an extra iteration for the right answer.
        if n >= prev_max:
            inc = 2
        n += inc
        if n >= i:
            prev_max = i - inc
            n = 1
            inc = 1
        # print(i, n)
    return n


print(part1(3012210))
print(part2(3012210))
