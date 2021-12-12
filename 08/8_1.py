datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()
    
for i in range(len(datalines)):
    datalines[i] = datalines[i].split(" | ")
    for j in range(len(datalines[i])):
        datalines[i][j] = datalines[i][j].split(" ")

def func(data):
    c = 0
    res = [0] * len(data)
    for i in range(len(data)):
        res[i] = sum(list(map(lambda a: 1 if len(a) in [2, 3, 4, 7]  else 0, data[i][1])))
    return sum(res)

print(func(datalines))
