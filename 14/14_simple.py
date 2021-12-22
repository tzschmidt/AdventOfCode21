datafile = "test.txt"

with open(datafile) as f:
    datalines = f.read().split("\n\n")

datalines[1] = datalines[1].split("\n")

rules = {}
ref = {}
c = 0
for i in datalines[1]:
    if i[-1:] not in ref:
        ref.update({i[-1:]: str(c)})
        c += 1

for i in datalines[1]:
    x = i.split(" -> ")
    rules[x[0]] = x[0][0] + ref[x[1]] + x[0][1]


def func(start, rules, ref, steps):
    data = start
    for i in range(steps):
        # workaround for BBB not leading to B1B1B but only B1BB
        for j in range(2):
            for key, value in rules.items():
                data = data.replace(key, value)
        for key, value in ref.items():
            data = data.replace(value, key)
    occurs = list(map(lambda a: data.count(a), list(ref.keys())))
    print(occurs)
    return max(occurs)-min(occurs)

print(func(datalines[0], rules, ref, 10))
