from functools import reduce

datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().split("\n\n")

for i in range(len(datalines)):
    datalines[i] = datalines[i].split("\n")
    for j in range(len(datalines[i])):
        if i == 1:
            x = datalines[i][j].split("=")
            datalines[i][j] = [x[0][-1:], int(x[1])]
        else:
            datalines[i][j] = list(map(int, datalines[i][j].split(",")))

def xfold(paper, x):
    for i in range(len(paper)):
        paper[i] = list(map(lambda a, b: a + b, paper[i][:x], paper[i][:x:-1]))
    return paper

def yfold(paper, y):
    for i in range(y):
        paper[i] = list(map(lambda a, b: a + b, paper[i], paper[len(paper)-1+-i]))
    return paper[:y]

def func(data, cmds, part1):
    xdim = 0
    ydim = 0
    for i in cmds:
        if i[0] == 'x' and not xdim:
            xdim = i[1] * 2 + 1
        if i[0] == 'y' and not ydim:
            ydim = i[1] * 2 + 1
    paper = [[0 for columns in range(xdim)] for rows in range(ydim)]

    for i in data:
        paper[i[1]][i[0]] = 1

    for i in cmds:
        if i[0] == 'x':
            paper = xfold(paper, i[1])
        if i[0] == 'y':
            paper = yfold(paper, i[1])
        if part1:
            break
    if part1: 
        return sum(list(map(lambda a: len(a), list(map(lambda b: list(filter((0).__ne__, b)), paper)))))
    else:
        return reduce(lambda x, y: x + y + "\n", list(map(lambda a: reduce(lambda x, y: x + y, list(map(lambda b: "." if b == 0 else "#", a)), ""), paper)), "")

print(func(datalines[0], datalines[1], 1))
print(func(datalines[0], datalines[1], 0))
