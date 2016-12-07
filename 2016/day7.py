import re


def is_tls(ip):
    hypernet = ' '.join(re.findall(r'\[\w+\]', ip))
    supernet = re.sub(r'\[\w+\]', ' ', ip)
    # Must be in supernet and not in hypernet
    hresults = [r for r in re.findall(r'(\w)(\w)\2\1', hypernet) if len(set(r)) > 1]
    sresults = [r for r in re.findall(r'(\w)(\w)\2\1', supernet) if len(set(r)) > 1]
    return sresults and not hresults


def is_ssl(ip):
    hypernet = ' '.join(re.findall(r'\[\w+\]', ip))
    unbracketed = re.sub(r'\[\w+\]', ' ', ip)
    BAB = [r for r in re.findall(r'(?=(\w)(\w)\1)', hypernet) if len(set(r)) > 1]
    ABA = ['{1}{0}{1}'.format(*x) for x in BAB]
    return any(pattern in unbracketed for pattern in ABA)


with open('day7.txt') as f:
    data = f.read().splitlines()

print(len([ip for ip in data if is_tls(ip)]))
print(len([ip for ip in data if is_ssl(ip)]))
