datafile = "data.txt"
horizontal = 0
depth = 0
aim = 0

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in datalines:
    cmd = i[:-2]
    num = int(i[-1:])
    if (cmd == 'forward'):
        horizontal += num
        depth += num * aim
    elif (cmd == 'up'):
        aim -= num
    elif (cmd == 'down'):
        aim += num

print(horizontal * depth)
