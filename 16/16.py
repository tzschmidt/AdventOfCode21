from functools import reduce

datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in range(len(datalines)):
    datalines[i] = format(int(datalines[i], 16), "0{0}b".format(len(datalines[i])*4))

def func(data, mode, stop, op):
    pnr = 0
    ver = 0
    i = 0
    end = 0
    cut = 0
    numbers = []
    while ((i < stop and not mode) or (pnr < stop and mode)) and len(data) >= 11:
        ver += int(data[i:i+3], 2)
        pid = int(data[i+3:i+6], 2)
        i = 6
        if pid == 4:
            num = ''
            while data[i] != '0':
                num += data[i+1:i+5]
                i += 5
            num += data[i+1:i+5]
            i += 5
            data = data[i:]
            if mode:
                pnr += 1
            else:
                stop -= i
            end += i
            i = 0
            numbers.append(int(num, 2))
        else:
            if not int(data[6:7], 2):
                length = int(data[7:22], 2)
                res = func(data[22:22+length], 0, length, pid)
                ver += res[0]
                numbers.append(res[2])
                cut = 22+length
                end += cut
                data = data[cut:]
                if mode:    
                    pnr += 1
                else:
                    stop -= cut
                i = 0
            else:
                res = func(data[18:], 1, int(data[7:18], 2), pid)
                ver += res[0]
                cut = res[1]+18
                numbers.append(res[2])
                end += cut
                data = data[cut:]
                if mode:
                    pnr += 1
                else:
                    stop -= cut
                i = 0
    if op == 0:
        return (ver, end, sum(numbers))
    elif op == 1:
        return (ver, end, reduce(lambda x, y: x * y, numbers))
    elif op == 2:
        return (ver, end, min(numbers))
    elif op == 3:
        return (ver, end, max(numbers))
    elif op == 4: # should not appear
        return (ver, end, numbers[0])
    elif op == 5:
        return (ver, end, int(numbers[0] > numbers[1]))
    elif op == 6:
        return (ver, end, int(numbers[0] < numbers[1]))
    elif op == 7:
        return (ver, end, int(numbers[0] == numbers[1]))
    return (ver, end, numbers[0])

for i in datalines:
    res = func(i, 0, len(i), 8)
    print(str(res[0]) + ' and ' + str(res[2]))







