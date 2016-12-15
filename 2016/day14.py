import re
import hashlib

salt = 'yjdafjpo'

hashes_p1 = []
hashes_p2 = []
key_indexes_p1 = []
key_indexes_p2 = []

def is_key(index, hash_list):
    h1 = hash_list[index]
    match = re.search(r'(.)\1\1', h1)
    if match:
        ch = h1[match.start()]
    else:
        return False
    if not any(h1[i] == h1[i + 1] == h1[i + 2] for i in range(len(h1) - 2)):
        return False

    return any(ch * 5 in h for h in hash_list[index + 1:index + 1000])


def stretch_hash(s):
    for _ in range(2017):
        s = hashlib.md5(s.encode()).hexdigest()
    return s

index = 0
while len(key_indexes_p1) < 64 or len(key_indexes_p2) < 64:
    if len(key_indexes_p1) < 64:
        while len(hashes_p1) < index + 1000:
            hashes_p1.append(hashlib.md5((salt + str(len(hashes_p1))).encode()).hexdigest())
        if is_key(index, hashes_p1):
            key_indexes_p1.append(index)
    if len(key_indexes_p2) < 64:
        while len(hashes_p2) < index + 1000:
            hashes_p2.append(stretch_hash(salt + str(len(hashes_p2))))
        if is_key(index, hashes_p2):
            key_indexes_p2.append(index)
    index += 1

print(key_indexes_p1[-1])
print(key_indexes_p2[-1])
