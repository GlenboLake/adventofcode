import re
from cmath import sqrt
from collections import defaultdict
from functools import reduce
from itertools import combinations
from time import time


def parse_particle(line):
    pos_match = re.search('p=<(-?\d+),(-?\d+),(-?\d+)>', line)
    position = Point3D(int(pos_match.group(1)), int(pos_match.group(2)), int(pos_match.group(3)))
    vel_match = re.search('v=<(-?\d+),(-?\d+),(-?\d+)>', line)
    velocity = Point3D(int(vel_match.group(1)), int(vel_match.group(2)), int(vel_match.group(3)))
    acc_match = re.search('a=<(-?\d+),(-?\d+),(-?\d+)>', line)
    acceleration = Point3D(int(acc_match.group(1)), int(acc_match.group(2)), int(acc_match.group(3)))
    return Particle(position, velocity, acceleration)


class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def manhattan(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __hash__(self):
        return hash(tuple([self.x, self.y, self.z]))

    def __add__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError('Can only add points to other points')

    def __sub__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError('Can only subtract other points from points')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError('Can only multiply point by scalar')

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Point3D(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError('Can only divide point by scalar')

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return Point3D(self.x // other, self.y // other, self.z // other)
        else:
            raise TypeError('Can only divide point by scalar')

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


class Particle(object):
    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def pos_at(self, t):
        return self.pos + self.vel * t + self.acc * t * (t + 1) // 2

    def __str__(self):
        return f'{self.pos}/{self.vel}/{self.acc}'


def part1(particles):
    max_accel = max(abs(p.acc.x) + abs(p.acc.y) + abs(p.acc.z) for p in particles)
    return particles.index(min(particles, key=lambda p: p.pos_at(100 * max_accel).manhattan()))


def will_collide(p1, p2):
    def is_int(c):
        return c.imag == 0 and (isinstance(c.real, int) or c.real.is_integer())

    def solve_quadratic(a, b, c):
        solutions = None
        if a:
            solutions = {(-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)}
        elif b:
            solutions = {-c / b}
        elif c:
            solutions = {c}
        if solutions is not None:
            solutions = set(map(lambda x: int(x.real), filter(is_int, solutions)))
        return solutions

    diff = Particle(p1.pos - p2.pos, p1.vel - p2.vel, p1.acc - p2.acc)
    tuples = [
        (diff.acc.x, diff.vel.x, diff.pos.x),
        (diff.acc.y, diff.vel.y, diff.pos.y),
        (diff.acc.z, diff.vel.z, diff.pos.z),
    ]
    solutions = reduce(lambda a, b: a & b,
                       filter(lambda s: s is not None,
                              [solve_quadratic(a / 2, v + a / 2, p) for a, v, p in tuples]))

    if solutions:
        return min(s for s in solutions if s > 0)
    return None


def pairs_to_sets(data):
    items = {a for a, b in data} | {b for a, b in data}
    sets = []
    seen = set()
    for item in items:
        if item in seen:
            continue
        new_set = set()
        seen.add(item)
        for pair in data:
            if item in pair:
                seen.update(set(pair))
                new_set.update(set(pair))
        sets.append(new_set)
    return sets


def part2(particles):
    collisions = defaultdict(list)
    for a, b in combinations(particles, 2):
        t = will_collide(a, b)
        if t is not None:
            collisions[t].append({a, b})
    collisions = {k: pairs_to_sets(v) for k, v in collisions.items()}
    remaining = set(particles)
    for t, splosions in sorted(collisions.items()):
        for s in splosions:
            if len(remaining & s) > 1:
                remaining -= s
    return len(remaining)


if __name__ == '__main__':
    particles = [parse_particle(line) for line in open('day20.in')]

    start = time()
    print('Part 1:', part1(particles))
    print('Part 2:', part2(particles))
    print(f'Took {time()-start}s')
