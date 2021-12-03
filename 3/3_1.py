datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

length = len(datalines[0])
countarr = [0] * length
onearr = [1] * length

for i in datalines:
    strlist = list(i)
    intlist = list(map(int,strlist))
    countarr = list(map(lambda a, b : a + b, countarr, intlist)) 

gammalist = list(map(lambda a : 1 if a > len(datalines)/2 else 0, countarr))
gamma = int("".join(str(i) for i in gammalist), 2)
epsilon = gamma ^ int("".join(str(i) for i in onearr), 2)

print(gamma * epsilon)
