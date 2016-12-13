commands = open('day12.txt').read().splitlines()


def run_program(init_values):
    def execute_command(command):
        # print(command)
        args = command.split()
        if args[0] == 'cpy':
            try:
                value = int(args[1])
            except ValueError:
                value = registers[args[1]]
            registers[args[2]] = value
        elif args[0] == 'inc':
            registers[args[1]] += 1
        elif args[0] == 'dec':
            registers[args[1]] -= 1
        else:  # jnz
            try:
                value = int(args[1])
            except ValueError:
                value = registers[args[1]]
            if value != 0:
                return current_line + int(args[2])
        return current_line + 1

    current_line = 0
    registers = dict(zip('abcd', init_values))

    while True:
        try:
            current_line = execute_command(commands[current_line])
        except IndexError:
            break
    print(registers['a'])


run_program([0, 0, 0, 0])
run_program([0, 0, 1, 0])
