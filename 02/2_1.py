datafile = "data.txt"
horizontal = 0
depth = 0

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in datalines:
    cmd = i[:-2]
    step = int(i[-1:])
    if (cmd == 'forward'):
        horizontal += step
    elif (cmd == 'up'):
        depth -= step
    elif (cmd == 'down'):
        depth += step

print(horizontal * depth)
