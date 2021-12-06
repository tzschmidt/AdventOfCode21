datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in range(len(datalines)):
    x = datalines[i].replace(" -> ",",")
    datalines[i] = list(map(int,x.split(",")))

def count(data):
    c = 0
    for i in data:
        for j in i:
            if j >= 2:
                c += 1
    return c

def func(datalines,size,diag):
    c = [[0 for columns in range(size)] for rows in range(size)]
    if not diag:
        datalines = list(filter(lambda a: not (a[0] != a[2] and a[1] != a[3]), datalines))
    for i in datalines:
        if i[0] < i[2]:
            for x in range(i[0],i[2]+1):
                if i[1] == i[3]:
                    c[i[1]][x] += 1
                elif i[1] < i[3]:
                    c[i[1]+x-i[0]][x] +=1
                else:
                    c[i[1]-x+i[0]][x] +=1
        elif i[0] > i[2]:
            for x in range(i[2],i[0]+1):
                if i[1] == i[3]:
                    c[i[1]][x] += 1
                elif i[1] < i[3]:
                    c[i[3]-x+i[2]][x] +=1
                else:
                    c[i[3]+x-i[2]][x] +=1
        else:
            if i[1] < i[3]:
                for y in range(i[1],i[3]+1):
                    c[y][i[0]] += 1
            elif i[1] > i[3]:
                for y in range(i[3],i[1]+1):
                    c[y][i[0]] += 1
            else:
                c[i[1]][i[0]] += 1
    return count(c)

print(func(datalines,1000,0))
print(func(datalines,1000,1))
