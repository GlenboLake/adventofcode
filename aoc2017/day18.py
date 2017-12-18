from collections import defaultdict


def part1(prog):
    registers = defaultdict(int)
    i = 0
    last_played = None

    def get(value):
        try:
            return int(value)
        except ValueError:
            return registers[value]

    while True:
        instruction = prog[i]
        cmd, *args = instruction.split()
        if cmd == 'snd':
            last_played = get(args[0])
            i += 1
        elif cmd == 'set':
            registers[args[0]] = get(args[1])
            i += 1
        elif cmd == 'add':
            registers[args[0]] += get(args[1])
            i += 1
        elif cmd == 'mul':
            registers[args[0]] *= get(args[1])
            i += 1
        elif cmd == 'mod':
            registers[args[0]] %= get(args[1])
            i += 1
        elif cmd == 'rcv':
            if get(args[0]) != 0:
                return last_played
            i += 1
        elif cmd == 'jgz':
            if get(args[0]) > 0:
                i += get(args[1])
            else:
                i += 1
        else:
            raise NotImplementedError


class State(object):
    def __init__(self, num, prog):
        self.id_ = num
        self.i = 0
        self.prog = prog
        self.registers = defaultdict(int)
        self.registers['p'] = num
        self.sends = []
        self.send_count = 0
        self.other = None
        self.terminated = False

    def can_run(self):
        if self.terminated:
            return False
        try:
            rcv = self.prog[self.i].split()[0] == 'rcv'
            if rcv:
                return len(self.other.sends) > 0
        except IndexError:
            return False
        return True

    def do_next(self):
        if not self.can_run():
            return

        def get(value):
            try:
                return int(value)
            except ValueError:
                return self.registers[value]

        if self.terminated:
            return
        try:
            instruction = self.prog[self.i]
        except IndexError:
            self.terminated = True
            return
        cmd, *args = instruction.split()
        if cmd == 'snd':
            self.sends.append(get(args[0]))
            self.send_count += 1
            self.i += 1
        elif cmd == 'set':
            self.registers[args[0]] = get(args[1])
            self.i += 1
        elif cmd == 'add':
            self.registers[args[0]] += get(args[1])
            self.i += 1
        elif cmd == 'mul':
            self.registers[args[0]] *= get(args[1])
            self.i += 1
        elif cmd == 'mod':
            self.registers[args[0]] %= get(args[1])
            self.i += 1
        elif cmd == 'rcv':
            self.registers[args[0]] = self.other.sends.pop(0)
            self.i += 1
        elif cmd == 'jgz':
            if get(args[0]) > 0:
                self.i += get(args[1])
            else:
                self.i += 1
        else:
            raise NotImplementedError


def part2(prog):
    p0 = State(0, prog)
    p1 = State(1, prog)
    p0.other = p1
    p1.other = p0
    while True:
        p0.do_next()
        p1.do_next()
        if not p0.can_run() and not p1.can_run():
            break
    return p1.send_count


if __name__ == '__main__':
    with open('day18.in') as f:
        input_ = f.read().splitlines()

    print('Part 1:', part1(input_))
    print('Part 2:', part2(input_))
