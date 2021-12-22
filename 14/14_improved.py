datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().split("\n\n")

datalines[1] = datalines[1].split("\n")

pairs = {}
start = datalines[0]
for i in range(len(start)-1):
    if start[i:i+2] not in pairs:
        pairs[start[i:i+2]] = 1
    else:
        pairs[start[i:i+2]] += 1

rules = {}
for i in datalines[1]:
    x = i.split(" -> ")
    rules[x[0]] = x[1]

def func(first, start, rules, steps):
    pairs = start.copy()
    for i in range(steps):
        newpairs = {}
        for p in pairs.keys():
            nl = rules[p]
            np1 = p[0] + nl
            np2 = nl + p[1]
            if np1 not in newpairs:
                newpairs[np1] = pairs[p]
            else:
                newpairs[np1] += pairs[p]
            if np2 not in newpairs:
                newpairs[np2] = pairs[p]
            else:
                newpairs[np2] += pairs[p]
        pairs = newpairs.copy()
    # only count last letter of pair
    occurs = {first: 1}
    for p in pairs.keys():
        if p[1] not in occurs:
            occurs[p[1]] = pairs[p]
        else:
            occurs[p[1]] += pairs[p]
   
    c = list(occurs.values())
    return max(c)-min(c)

print(func(start[0], pairs, rules, 10))
print(func(start[0], pairs, rules, 40))
