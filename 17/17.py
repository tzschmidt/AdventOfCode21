import math

datafile = "data.txt"

with open(datafile) as f:
    dataline = f.read()

data = dataline.split(", ")
data = list(map(lambda a: a.split(".."), data))
target = (int(data[0][0][15:]), int(data[0][1]), int(data[1][0][2:]), int(data[1][1]))

def maxy(y):
    return int((y + 1) * (y / 2))

def besty(t):
    y = t[2]* -1 - 1
    return y

def hit(x, y, t):
    if t[0] <= x <= t[1] and t[2] <= y <= t[3]:
        return True
    return False

def xlowbound(x):
    return int((-1 + math.sqrt(abs(8 * x))) / 2)

def trajec(x, y, dx, dy, t):
    if hit(x, y, t):
        return True
    elif x <= t[1] and y >= t[2]:
        if dx > 0 and x != 0:
            dx -= 1
        return trajec(x+dx, y+dy, dx, dy-1, t)
    return False

def func(t):
    starts = []
    for x in range(xlowbound(t[0]), t[1]+1):
        for y in range(t[2], besty(t)+1):
            if trajec(0, 0, x , y, t):
                starts.append((x, y))
    return len(starts)

print(maxy(besty(target)))
print(func(target))
