import json

def count_json(obj, ignore_red=False):
    if isinstance(obj, dict):
        if ignore_red and ("red" in obj or "red" in obj.values()):
            return 0
        else:
            return count_json(list(obj.values()), ignore_red)
    elif isinstance(obj, list):
        sum = 0
        for item in obj:
            sum += count_json(item, ignore_red)
        return sum
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0
    else:
        print("PROBLEM! ", obj)

with open(r'C:\Users\Glen\Downloads\day12.txt') as f:
    input_ = json.loads(f.read())

print(count_json(input_))
print(count_json(input_, True))

obj=[1,{"c":"red","b":2},3]

print(count_json(obj, True))
