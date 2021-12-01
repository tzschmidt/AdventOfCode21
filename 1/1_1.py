datafile = "data.txt"
count = 0
prev = float('inf')

with open(datafile) as f:
    datalines = f.readlines()

for i in datalines:
    if (int(i) > prev):
        count+=1
    prev = int(i)

print(count)
