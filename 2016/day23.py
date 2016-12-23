# commands = ['cpy 2 a',
#             'tgl a',
#             'tgl a',
#             'tgl a',
#             'cpy 1 a',
#             'dec a',
#             'dec a'
#             ]
commands = open('day23.txt').read().splitlines()


def get(registers, value):
    try:
        return int(value)
    except ValueError:
        return registers[value]


def run_program(instructions, init_values):
    def execute_command(num):
        command = instructions[num]
        # print(num, command)
        op, args = command.split(' ', 1)
        if op == 'cpy':
            value, dst = args.split()
            # Check for loops
            if [i.split(' ', 1)[0] for i in instructions[num + 1:num + 6]] == ['inc', 'dec', 'jnz', 'dec', 'jnz']:
                loop = [i.split() for i in instructions[num + 1:num + 6]]
                inc_var = loop[0][1]
                inner_cond, inner_off = loop[2][1:]
                outer_cond, outer_off = loop[4][1:]
                # Make sure the following sets are len 1
                check_inner_var = {loop[1][1], inner_cond}
                check_outer_var = {loop[3][1], outer_cond}
                if len(check_inner_var) == 1 and len(check_outer_var) == 1 \
                        and int(inner_off) == -2 and int(outer_off) == -5:
                    inner_var = dst
                    outer_var = list(check_outer_var)[0]
                    registers[inc_var] += registers[outer_var] * get(registers, value)
                    registers[inner_var] = registers[outer_var] = 0
                    return num + 6
            registers[dst] = get(registers, value)
        elif op == 'inc':
            registers[args] += 1
        elif op == 'dec':
            registers[args] -= 1
        elif op == 'tgl':
            amount = get(registers, args)
            try:
                toggle = instructions[num + amount].split()
            except IndexError:
                pass
            else:
                if len(toggle) == 2:
                    if toggle[0] == 'inc':
                        toggle[0] = 'dec'
                    else:
                        toggle[0] = 'inc'
                else:
                    if toggle[0] == 'jnz':
                        toggle[0] = 'cpy'
                    else:
                        toggle[0] = 'jnz'
                instructions[num + amount] = ' '.join(toggle)
        else:  # jnz
            check, jump = [get(registers, arg) for arg in args.split()]
            if check:
                return num + jump
        return num + 1

    registers = dict(zip('abcd', init_values))
    current_line = 0

    while 0 <= current_line < len(instructions):
        current_line = execute_command(current_line)
    return registers


part1 = run_program(commands.copy(), [7, 0, 0, 0])
part2 = run_program(commands.copy(), [12, 0, 0, 0])

print('Part 1:', part1['a'])
print('Part 2:', part2['a'])
