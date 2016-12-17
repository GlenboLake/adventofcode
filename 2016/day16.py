initial = '11101000110010100'

trans = str.maketrans('01', '10')


def step(data):
    return data + '0' + data[::-1].translate(trans)


def fill_data(initial_state, length):
    data = initial_state
    while len(data) < length:
        data = step(data)
        print(len(data))
    return data[:length]


def chunks(l, n=2):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def checksum(data):
    res = ''
    for chunk in chunks(data):
        if len(set(chunk)) == 1:
            res += '1'
        else:
            res += '0'
    if len(res) % 2 == 0:
        return checksum(res)
    else:
        return res


print(checksum(fill_data(initial, 272)))
print(checksum(fill_data(initial, 35651584)))
