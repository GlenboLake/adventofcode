def valid_triangle(sides):
    sides = sorted(map(int, sides))
    return sides[-1] < sum(sides[:2])


with open('day3.txt') as f:
    lines = f.read().splitlines()
triangles = [line.split() for line in lines]

print(len([t for t in triangles if valid_triangle(t)]))


def chunks(l, n=3):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


triangles = chunks([t[0] for t in triangles] + [t[1] for t in triangles] + [t[2] for t in triangles])

print(len([t for t in triangles if valid_triangle(t)]))
