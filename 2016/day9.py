with open('day9.txt') as f:
    text = f.readline().strip()
decompressed = ''

# text = 'X(8x2)(3x3)ABCY'

index = 0
length = 0
while True:
    try:
        next = text[index]
        if next == '(':
            tag_end = text.index(')', index)
            count, times = map(int, text[index + 1:tag_end].split('x'))
            index = tag_end + 1
            for _ in range(times):
                decompressed += text[index: index + count]
                length += count
            index += count
        else:
            decompressed += next
            index += 1
            length += 1
    except IndexError:
        break

print(len(decompressed))
print(length)

decompressed2 = ''


def parse(string):
    index = 0
    length = 0
    while True:
        try:
            next = string[index]
            if next == '(':
                tag_end = string.index(')', index)
                count, times = map(int, string[index + 1:tag_end].split('x'))
                index = tag_end + 1
                length += parse(string[index:index + count]) * times
                index += count
            else:
                length += 1
                index += 1
        except IndexError:
            break
    return length


print(parse('(3x3)XYZ'))
print(parse('X(8x2)(3x3)ABCY'))
print(parse('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
print(parse('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'))
print(parse(text))