datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

count = 0

def oxy(data):
    for i in range(len(data[0])):
        count = 0
        for j in data:
            count += int(j[i])
        data = list(filter(lambda a: int(a[i]) == 1 if count >= len(data)/2 else int(a[i]) == 0, data))
        if (len(data) == 1):
            break
    return int("".join(str(i) for i in data), 2)

def co2(data):
    for i in range(len(data[0])):
        count = 0
        for j in data:
            count += int(j[i])
        data = list(filter(lambda a: int(a[i]) == 1 if count < len(data)/2 else int(a[i]) == 0, data))
        if (len(data) == 1):
            break
    return int("".join(str(i) for i in data), 2)

print(oxy(datalines) * co2(datalines))




