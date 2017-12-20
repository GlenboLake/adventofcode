import re
from textwrap import dedent


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

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError('Can only multiply point by scalar')

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Point3D(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError('Can only multiply point by scalar')

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


class Particle(object):
    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def pos_at(self, t):
        return self.pos + self.vel * t + self.acc * t ** 2 / 2


def part1(particles):
    return particles.index(min(particles, key=lambda p: p.pos_at(1000).manhattan()))


def part2(particles):
    pass


if __name__ == '__main__':
    particles = [parse_particle(line) for line in open('day20.in')]

    print('Part 1:', part1(particles))

    sample = [parse_particle(line) for line in dedent("""\
        p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
        p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
        p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
        p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>""").splitlines()]
    assert part2(sample) == 1

    print('Part 2:', part2(particles))
