import re


def isvalid(ip):
    part1 = re.search(r'(\w)(\w)\2\1', ip)
    if part1:
        if len(set(part1.groups())) == 1:
            part1 = None
    part2 = re.search(r'\[\w*(\w)(\w)\2\1\w*\]', ip)
    return 1 if part1 and not part2 else 0

with open('day7.txt') as f:
    data = f.read().splitlines()

print(sum(isvalid(ip) for ip in data))

def isvalid2(ip):
    # print(ip)
    bracketed = ' '.join(re.findall(r'\[(\w+)\]', ip))
    unbracketed = re.sub(r'\[\w+\]', ' ', ip)
    # print(bracketed)
    # print(unbracketed)
    BAB = re.findall(r'(?=(\w)(\w)\1)', bracketed)
    BAB = [x for x in BAB if len(set(x))>1]
    ABA = ['{1}{0}{1}'.format(*x) for x in BAB]
    # print(ABA)
    # print(BAB)
    return any(pattern in unbracketed for pattern in ABA)

# print(isvalid2('aba[bab]xyz'))
# print(isvalid2('xyx[xyx]xyx'))
# print(isvalid2('aaa[kek]eke'))
# print(isvalid2('zazbz[bzb]cdb'))
# print(isvalid2('klioqytpqhkxqiriz[rjgrssxpxozhzbc]fysfmaiblgqhkeue[bycqedeolknahiy]pdusnyfxfcgodvj'))

print(len([ip for ip in data if isvalid2(ip)]))