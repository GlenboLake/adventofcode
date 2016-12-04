import re

frm = 'abcdefghijklmnopqrstuvwxyz-'
to_ = 'bcdefghijklmnopqrstuvwxyza '
table = str.maketrans(frm, to_)

def check_room(room):
    match = re.match('([a-z\-]+)-(\d+)\[([a-z]{5})\]', room)
    name, id_, checksum = [match.group(x) for x in (1, 2, 3)]
    name_chars = sorted(set(name) - {'-'})
    expected_checksum = ''.join(sorted(name_chars, key=lambda ch: name.count(ch), reverse=True)[:5])
    return int(id_) if checksum == expected_checksum else 0

with open('day4.txt') as f:
    rooms = f.read().splitlines()

print(sum(map(check_room, rooms)))

def decrypt(room):
    match = re.match('([a-z\-]+)-(\d+)\[([a-z]{5})\]', room)
    name, id_, checksum = [match.group(x) for x in (1, 2, 3)]
    decrypted = name
    for _ in range(int(id_)):
        decrypted = decrypted.translate(table)
    if 'north' in decrypted:
        print(decrypted, id_)

for room in rooms:
    decrypt(room)