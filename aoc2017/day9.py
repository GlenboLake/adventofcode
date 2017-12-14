import re

with open('day9.in') as f:
    input_ = f.read().strip()


def score(text):
    total = 0
    depth = 0
    skip = False
    garbage = False
    garbage_count = 0
    for i in range(len(text)):
        if garbage:
            if skip:
                skip = False
            elif text[i] == '>':
                garbage = False
            elif text[i] == '!':
                skip = True
            else:
                garbage_count += 1
        elif text[i] == '<':
            garbage = True
        elif text[i] == '{':
            depth += 1
        elif text[i] == '}':
            total += depth
            depth -= 1
    return total, garbage_count


assert score('{}')[0] == 1
assert score('{{{}}}')[0] == 6
assert score('{{},{}}')[0] == 5
assert score('{{{},{},{{}}}})')[0] == 16
assert score('{<a>,<a>,<a>,<a>}')[0] == 1
assert score('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0] == 9
assert score('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0] == 9
assert score('{{<a!>},{<a!>},{<a!>},{<ab>}} ')[0] == 3

print(score(input_))

assert score('<>')[1] == 0
assert score('<random characters>')[1] == 17
assert score('<<<<>')[1] == 3
assert score('<{!>}>')[1] == 2
assert score('<!!>')[1] == 0
assert score('<!!!>>')[1] == 0
assert score('<{o"i!a,<{i<a>')[1] == 10
