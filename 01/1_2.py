datafile = "data.txt"
count = 0
prev = float('inf')
first = float('inf')
second = float('inf')

with open(datafile) as f:
    datalines = f.readlines()

for i in datalines:
    third = second
    second = first
    first = int(i)
    sum = first + second + third
    if (sum > prev):
        count+=1
    prev = sum

print(count)
