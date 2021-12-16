datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in range(len(datalines)):
    datalines[i] = list(map(int, list(datalines[i])))

def blink(data, i, j, blinks):
    if j != 0:
        if data[i][j-1] <= 9:
            data[i][j-1] += 1
            if data[i][j-1] == 10:
                data[i][j-1] += 1
                blinks[0] += 1
                blink(data, i, j-1, blinks)
        if i != 0:
            if data[i-1][j-1] <= 9:
                data[i-1][j-1] += 1
                if data[i-1][j-1] == 10:
                    data[i-1][j-1] += 1
                    blinks[0] += 1
                    blink(data, i-1, j-1, blinks)
        if i != len(data)-1:
            if data[i+1][j-1] <= 9:
                data[i+1][j-1] += 1
                if data[i+1][j-1] == 10:
                    data[i+1][j-1] += 1
                    blinks[0] += 1
                    blink(data, i+1, j-1, blinks)
    if j != len(data[i])-1:
        if data[i][j+1] <= 9:
            data[i][j+1] += 1
            if data[i][j+1] == 10:
                data[i][j+1] += 1
                blinks[0] += 1
                blink(data, i, j+1, blinks)
        if i != 0:
            if data[i-1][j+1] <= 9:
                data[i-1][j+1] += 1
                if data[i-1][j+1] == 10:
                    data[i-1][j+1] += 1
                    blinks[0] += 1
                    blink(data, i-1, j+1, blinks)
        if i != len(data)-1:
            if data[i+1][j+1] <= 9:
                data[i+1][j+1] += 1
                if data[i+1][j+1] == 10:
                    data[i+1][j+1] += 1
                    blinks[0] += 1
                    blink(data, i+1, j+1, blinks)
    if i != 0:
        if data[i-1][j] <= 9:
            data[i-1][j] += 1
            if data[i-1][j] == 10:
                data[i-1][j] += 1
                blinks[0] += 1
                blink(data, i-1, j, blinks)
    if i != len(data)-1:
        if data[i+1][j] <= 9:
            data[i+1][j] += 1
            if data[i+1][j] == 10:
                data[i+1][j] += 1
                blinks[0] += 1
                blink(data, i+1, j, blinks)
    return True
        
def func(data, steps):
    blinks = [0]
    part2 = 0
    if steps == 0:
        part2 = 1
        steps = 1000000000
    for s in range(steps):
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1
                if data[i][j] == 10:
                    data[i][j] += 1
                    blinks[0] += 1
                    blink(data, i, j, blinks)
        data = list(map(lambda b: list(map(lambda a: 0 if a > 9 else a, b)), data))
        if part2:
            if all(all(x == 0 for x in y) for y in data):
                return s+2 
    return blinks[0]

# steps == 0 for part 2
print(func(datalines, 100))
print(func(datalines, 0))
