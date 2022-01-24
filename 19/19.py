datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().split("\n\n")

for i in range(len(datalines)):
    datalines[i] = datalines[i].splitlines()

data = list(map(lambda a: list(map(lambda b: tuple(map(int, b)), list(map(lambda b: b.split(","), list(filter(lambda b: b[-1:] != "-", a)))))), datalines))

def get_vec(p1, p2):
    return (p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2])

def add_vec(v1, v2):
    return (v2[0]+v1[0], v2[1]+v1[1], v2[2]+v1[2])

def sub_vec(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])

def inv_vec(v):
    return (-v[0], -v[1], -v[2])

def add_rel(r1, r2, p1, p2, sen):
    delta = get_vec(p1, p2)
    newrel = {}
    sen.add(add_vec(p1, inv_vec(p2)))
    for i in r1.items():
        for j in r2.items():
            nvs = set(filter(((0,0,0)).__ne__, set(map(lambda a: add_vec(get_vec(i[0], p1), a), r2[p2]))))
            newrel.update({i[0]: i[1] | nvs})
            nc = sub_vec(j[0], delta)
            if nc not in r1.keys():
                nvs = set(filter(((0,0,0)).__ne__, set(map(lambda a: add_vec(get_vec(j[0], p2), a), r1[p1]))))
                newrel.update({nc: j[1] | nvs})
    return newrel            

def get_rel(scanner):
    rel = {}
    for i in scanner:
        beacon = set()
        for j in scanner:
            if i != j:
                beacon.add(get_vec(i, j))
        rel.update({i: beacon})
    return rel

def tup_rotations(tup):
    t = list(tup)
    l = []
    for _ in range(3):
        l.append((t[0],t[1],t[2]))
        l.append((t[0],-t[1],-t[2]))
        l.append((t[0],t[2],-t[1]))
        l.append((t[0],-t[2],t[1]))
        l.append((-t[0],t[1],-t[2]))
        l.append((-t[0],-t[1],t[2]))
        l.append((-t[0],t[2],t[1]))
        l.append((-t[0],-t[2],-t[1]))
        t = [t[1],t[2],t[0]]
    return l

def rel_rotations(rel):
    rot = [{} for _ in range(24)]
    for i in rel.items():
        key_rot = tup_rotations(i[0])
        val_rot = []
        for j in i[1]:
            val_rot.append(tup_rotations(j))
        for j in range(24):
            rot[j].update({key_rot[j]: set(map(lambda a: a[j], val_rot))}) 
    return rot    

def match(rel1, rel2, sen):
    newrel = rel1.copy()
    for rot in rel_rotations(rel2):
        for i in rel1.items():
            for j in rot.items():
                if len(i[1] & j[1]) >= 11 and (i[1] | j[1]) != i[1]:
                    newrel = add_rel(rel1, rot, i[0], j[0], sen)
                    break
            else:
                continue
            break
        else:
            continue
        break
    return newrel

def manhatten(p, q):
    d = 0
    for p_i, q_i in zip(p, q):
        d += abs(p_i - q_i)
    return d

def func(data):
    prev = {}
    sen = {(0,0,0)}
    rel = get_rel(data[0])
    while prev != rel:
        prev = rel
        for i in data[1:]:
            rel = match(rel, get_rel(i), sen)
    print("part1: " + str(len(rel)))
    print("part2: " + str(max(list(map(lambda x: manhatten(x[0], x[1]), list(filter(lambda x: x[0] != x[1], [[x,y] for x in sen for y in sen])))))))
    return 0

func(data)

