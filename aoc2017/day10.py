from functools import reduce

input_ = '187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216'


def shift(list_, amount):
    return list_[amount:] + list_[:amount]


assert shift([0, 1, 2, 3, 4], 1) == [1, 2, 3, 4, 0]


def cycle(nums, inputs, i=0, skip=0):
    nums = list(nums)
    for num in inputs:
        nums = shift(nums, i)
        nums[:num] = nums[:num][::-1]
        nums = shift(nums, -i)
        i += num + skip
        i %= len(nums)
        skip += 1
    return nums, i, skip


def encode(nums):
    return list(map(ord, nums)) + [17, 31, 73, 47, 23]


def knot_hash(string):
    lengths = encode(string)
    i = skip = 0
    nums = range(256)
    for _ in range(64):
        nums, i, skip = cycle(nums, lengths, i, skip)
    dense = [reduce(lambda a, b: a ^ b, nums[16 * idx:16 * idx + 16]) for idx in range(16)]
    return ''.join(hex(num)[2:].zfill(2) for num in dense)


assert knot_hash('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert knot_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert knot_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert knot_hash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

if __name__ == '__main__':
    p1 = cycle(range(256), map(int, input_.split(',')))[0]
    print('Part 1:', p1[0] * p1[1])
    print('Part 2:', knot_hash(input_))
