import re
from collections import namedtuple
from time import time

Particle = namedtuple('Particle', ['pos', 'vel', 'acc'])


def parse_particle(line):
    pos_match = re.search('p=<(-?\d+),(-?\d+),(-?\d+)>', line)
    position = int(pos_match.group(1)), int(pos_match.group(2)), int(pos_match.group(3))
    vel_match = re.search('v=<(-?\d+),(-?\d+),(-?\d+)>', line)
    velocity = int(vel_match.group(1)), int(vel_match.group(2)), int(vel_match.group(3))
    acc_match = re.search('a=<(-?\d+),(-?\d+),(-?\d+)>', line)
    acceleration = int(acc_match.group(1)), int(acc_match.group(2)), int(acc_match.group(3))
    return Particle(position, velocity, acceleration)


def move_particle(particle):
    new_v = tuple(v + a for v, a in zip(particle.vel, particle.acc))
    new_p = tuple(p + v for p, v in zip(particle.pos, new_v))
    return Particle(new_p, new_v, particle.acc)


def manhattan(particle):
    return sum(abs(k) for k in particle.pos)


if __name__ == '__main__':
    particles = [parse_particle(line) for line in open('day20.in')]

    orig = particles.copy()
    start = time()
    for i in range(1000):
        particles = [move_particle(p) for p in particles]
        print(i, particles.index(min(particles, key=manhattan)))
    print(particles.index(min(particles, key=manhattan)))

    particles = orig.copy()
    for _ in range(1000):
        if len(set(p.pos for p in particles)) < len(particles):
            positions = [p.pos for p in particles]
            particles = [part for part, pos in zip(particles, positions) if positions.count(pos) == 1]
            print(len(particles))
        particles = [move_particle(p) for p in particles]
    print(f'Took {time()-start}s')
