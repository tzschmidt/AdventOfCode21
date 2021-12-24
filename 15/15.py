from copy import deepcopy

datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in range(len(datalines)):
    datalines[i] = [int(j) for j in datalines[i]]

def increase_risk(data):
    return list(map(lambda a: list(map(lambda b: b + 1 if b < 9 else 1, a)), data))

def expand(data, xtimes, ytimes):
    
    new = deepcopy(data)
    newdata = data
    for i in range(1,xtimes):
        newdata = increase_risk(newdata)
        new = list(map(lambda a, b: a + b, new, newdata))
    newdata = new
    for i in range(1,ytimes):
        newdata = increase_risk(newdata)
        new.extend(newdata)
    return new

# not needed, see below
def calc_h(data):
    h = deepcopy(data)
    for i in range(len(h)):
        for j in range(len(h[i])):
            #h[i][j] = len(h) - 1 - i + len(h[i]) - 1 - j
            h[i][j] = 0
    return h

def get_neighbours(node, xmax, ymax):
    return list(filter(lambda a: 0 <= a[0] <= xmax and 0 <= a[1] <= ymax, [(node[0]+1, node[1]), (node[0]-1, node[1]), (node[0], node[1]+1), (node[0], node[1]-1)]))

def backtrack(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

def a_star(start, goal, d, h):
    openSet = set([start])
    cameFrom = {}
    gscore = {}
    gscore[start] = 0
    fscore = {}
    fscore[start] = 0

    while openSet:
        current = min(openSet, key=fscore.__getitem__)
        if current == goal:
            return backtrack(cameFrom, current)
        
        openSet.remove(current)
        for neighbour in get_neighbours(current, len(d[0])-1, len(d)-1):
            if neighbour not in gscore:
                gscore[neighbour] = float('inf')
            tentative_gscore = gscore[current] + d[neighbour[1]][neighbour[0]]
            if tentative_gscore < gscore[neighbour]:
                cameFrom[neighbour] = current
                gscore[neighbour] = tentative_gscore
                fscore[neighbour] = tentative_gscore + h[neighbour[1]][neighbour[0]]
                if neighbour not in openSet:
                    openSet.add(neighbour)
                    if neighbour not in fscore:
                        fscore[neighbour] = float('inf')
    return False

def func(data, part2):
    if part2:
        data = expand(data, 5, 5)
    path = a_star((0, 0), (len(data[0])-1, len(data)-1), data, calc_h(data))
    return sum(list(map(lambda a: data[a[1]][a[0]], path))) - data[0][0]

print(func(datalines, 0))
# part2 could probably be optimized by removing heuristic h and fscore completely
print(func(datalines, 1))
