import hashlib

door = 'wtnhxymk'

password = ''
index = 0
while len(password) < 8:
    hash = hashlib.md5((door + str(index)).encode())
    if hash.hexdigest().startswith('00000'):
        password += hash.hexdigest()[5]
    index += 1
print(password)

password = ['-'] * 8
index = 0
while '-' in password:
    hash = hashlib.md5((door + str(index)).encode()).hexdigest()
    if hash.startswith('00000'):
        pos = int(hash[5], 16)
        if pos < 8 and password[pos] == '-':
            password[pos] = hash[6]
    index += 1
print(''.join(password))
