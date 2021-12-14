from functools import reduce

datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in range(len(datalines)):
    datalines[i] = list(map(int, list(datalines[i])))

def rekcheck(data, i, j, basinsize, basinstart):
    if j != 0:
        if data[i][j-1] != 9 and data[i][j-1] != data[i][j] and data[i][j-1] >= basinstart:
            basinsize[data[i][j-1]-basinstart] -= 1
            basinsize[data[i][j]-basinstart] += 1
            data[i][j-1] = data[i][j]
            rekcheck(data, i, j-1, basinsize, basinstart)
    if i != 0:
        if data[i-1][j] != 9 and data[i-1][j] != data[i][j] and data[i-1][j] >= basinstart:
            basinsize[data[i-1][j]-basinstart] -= 1
            basinsize[data[i][j]-basinstart] += 1
            data[i-1][j] = data[i][j]
            rekcheck(data, i-1, j, basinsize, basinstart)
    if j != len(data[i])-1:
        if data[i][j+1] != 9 and data[i][j+1] != data[i][j] and data[i][j+1] >= basinstart:
            basinsize[data[i][j+1]-basinstart] -= 1
            basinsize[data[i][j]-basinstart] += 1
            data[i][j+1] = data[i][j]
            rekcheck(data, i, j+1, basinsize, basinstart)
    if i != len(data)-1:
        if data[i+1][j] != 9 and data[i+1][j] != data[i][j] and data[i+1][j] >= basinstart:
            print(data[i+1][j])
            print(basinsize)
            basinsize[data[i+1][j]-basinstart] -= 1
            basinsize[data[i][j]-basinstart] += 1
            data[i+1][j] = data[i][j]
            rekcheck(data, i+1, j, basinsize, basinstart)
    return True
        
def func(data):
    basinstart = 10
    basin = basinstart
    basinsize = list()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i == 0:
                if j == 0:
                    if data[i][j] != 9:
                        data[i][j] = basin 
                        basinsize.append(1)
                        basin += 1
                else:
                    if data[i][j] != 9:
                        if data[i][j-1] != 9:
                            data[i][j] = data[i][j-1]
                            basinsize[data[i][j]-basinstart] += 1
                        else:
                            data[i][j] = basin
                            basinsize.append(1)
                            basin += 1
            elif j == 0:
                if data[i][j] != 9:
                    if data[i-1][j] != 9:
                        data[i][j] = data[i-1][j]
                        basinsize[data[i][j]-basinstart] += 1
                    else:
                        data[i][j] = basin
                        basinsize.append(1)
                        basin += 1
            else:
                if data[i][j] != 9:
                    if data[i-1][j] != 9:
                        data[i][j] = data[i-1][j]
                        basinsize[data[i][j]-basinstart] += 1
                        rekcheck(data, i, j, basinsize, basinstart)
                    elif data[i][j-1] != 9:
                        data[i][j] = data[i][j-1]
                        basinsize[data[i][j]-basinstart] += 1
                    else:
                        data[i][j] = basin
                        basinsize.append(1)
                        basin += 1
    return reduce(lambda x, y: x * y, sorted(list(filter((0).__ne__, basinsize)), reverse=True)[:3])

print(func(datalines))
