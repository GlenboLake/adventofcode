from statistics import mode

with open('day6.txt') as f:
    message = f.read().splitlines()

code = ''
for i in range(len(message[0])):
    opts = [line[i] for line in message]
    code += mode(opts)
print(code)

code = ''
for i in range(len(message[0])):
    opts = [line[i] for line in message]
    freqs = {ch: opts.count(ch) for ch in opts}
    minval = min(freqs.values())
    code += [ch for ch, v in freqs.items() if v == minval][0]
print(code)
