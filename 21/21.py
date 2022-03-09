import re

datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().split("\n")
    data = list(map(lambda a: int(re.search(": (\d*)", a).group(1)), datalines))

def next_field(p, v):
    x = (p[0] + sum(v)) % 10
    if x == 0: x = 10
    return x

def updated_next_field(pos, step):
    x = (pos + step) % 10
    if x == 0: x = 10
    return x

def get_val(v):
    v = list(map(lambda a: 100 if a == 0 else a, list(map(lambda a: (a+3) % 100, v))))
    return v

def part1(starts):
    p1 = (starts[0], 0)
    p2 = (starts[1], 0)
    c = 3
    v = [1, 2, 3]
    while True:
        x = next_field(p1,v)
        p1 = (x, p1[1] + x)
        if p1[1] >= 1000: break
        v = get_val(v)
        c += 3
        x = next_field(p2,v)
        p2 = (x, p2[1] + x)
        if p2[1] >= 1000: break
        v = get_val(v)
        c += 3
    return min(p1[1], p2[1])* c

def part2(starts):
    w = [0,0]
    games = {(starts[0], starts[1], 0, 0): 1}
    vdic = {3:1, 4:3 ,5:6 ,6:7 ,7:6 ,8:3 ,9:1}
    while games:
        for p in [0,1]:
            ngames = {}
            for s, v in games.items():
                for i in vdic.keys():
                    nv = v * vdic[i]
                    x = updated_next_field(s[p], i)
                    ns = list(s)
                    ns[p] = x
                    ns[p+2] += x
                    ns = tuple(ns)
                    if ns[p+2] >= 21:
                        w[p] += nv
                    elif ns in ngames:
                        ngames.update({ns: ngames[ns] + nv})
                    else:
                        ngames.update({ns: nv})
            games = ngames.copy()
    if w[0] >= w[1]:
        return w[0]
    return w[1]

print(part1(data))
print(part2(data))

