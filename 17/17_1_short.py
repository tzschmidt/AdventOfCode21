datafile = "data.txt"

with open(datafile) as f:
    dataline = f.read()

data = dataline.split(", ")
data = list(map(lambda a: a.split(".."), data))
target = (int(data[0][0][15:]), int(data[0][1]), int(data[1][0][2:]), int(data[1][1]))

def maxheight(t):
    y = t[2]* -1 - 1
    return int((y + 1) * (y / 2))

print(maxheight(target))


