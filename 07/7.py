import statistics
import math

datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in datalines:
    data = list(map(int, i.split(",")))

def func(data, part2):
    if part2:
        m1 = statistics.mean(data)
        m2 = int(math.ceil(m1))
        m1 = int(m1)
    else:
        m1 = int(statistics.median(data))
    fuel1 = 0
    fuel2 = 0
    for i in data:
        x1 = abs(i - m1)
        if part2:
            x1 = abs(i - m1)
            x2 = abs(i - m2)
            fuel1 += int((x1 + 1) * (x1 / 2))
            fuel2 += int((x2 + 1) * (x2 / 2))
        else:
            fuel1 += x1
    if fuel1 < fuel2 or not fuel2:
        return fuel1
    else: 
        return fuel2

print(func(data, 0))
print(func(data, 1))
