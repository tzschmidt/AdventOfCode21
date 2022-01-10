from copy import deepcopy

datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in range(len(datalines)):
    datalines[i] = eval(datalines[i])

def prep(prel):
    for i in range(len(prel)):
        if type(prel[i]) == int:
            prel[i] = [prel[i]]
        else:
            prep(prel[i])

def reprep(prel):
    for i in range(len(prel)):
        if len(prel[i]) == 1:
            prel[i] = prel[i][0]
        else:
            reprep(prel[i])

def add(pre, new):
    prep(new)
    return [pre, new]

def div(num):
    val1 = num // 2
    if num % 2:
        val2 = val1 + 1
    else:
        val2 = val1
    return [[val1], [val2]]

def check(data, mode):
    prev = [None]
    explode = False
    split = False
    for i in range(len(data)):
        if len(data[i]) == 2:
            for j in range(len(data[i])):
                if len(data[i][j]) == 2:
                    for k in range(len(data[i][j])):
                        if len(data[i][j][k]) == 2:
                            for l in range(len(data[i][j][k])):
                                if len(data[i][j][k][l]) == 2 and not explode and not mode:
                                    # explosion
                                    if type(prev[0]) == int:
                                        prev[0] = prev[0] + data[i][j][k][l][0][0]
                                    val = data[i][j][k][l][1][0]
                                    data[i][j][k][l] = [0]
                                    explode = True
                                elif len(data[i][j][k][l]) == 2:
                                    for m in range(len(data[i][j][k][l])):
                                        if len(data[i][j][k][l][m]) == 2 and not explode and not mode:
                                            if type(prev[0]) == int:
                                                prev[0] = prev[0] + data[i][j][k][l][m][0][0]
                                            val = data[i][j][k][l][m][1][0]
                                            data[i][j][k][l][m] = [0]
                                            explode = True
                                        elif len(data[i][j][k][l][m]) == 2:
                                            print("ERROR")
                                        else:
                                            prev = data[i][j][k][l][m]
                                            if explode and not mode:
                                                prev[0] = prev[0] + val
                                                break
                                            elif prev[0] >= 10 and mode:
                                                res = div(prev[0])
                                                prev[0] = res[0]
                                                prev.append(res[1])
                                                split = True
                                                break
                                    else:
                                        continue
                                    break
                                else:
                                    prev = data[i][j][k][l]
                                    if explode and not mode:
                                        prev[0] = prev[0] + val
                                        break
                                    elif prev[0] >= 10 and mode:
                                        res = div(prev[0])
                                        prev[0] = res[0]
                                        prev.append(res[1])
                                        split = True
                                        break
                            else:
                                continue
                            break
                        else:
                            prev = data[i][j][k]
                            if explode and not mode:
                                prev[0] = prev[0] + val
                                break
                            elif prev[0] >= 10 and mode:
                                res = div(prev[0])
                                prev[0] = res[0]
                                prev.append(res[1])
                                split = True
                                break
                    else:
                        continue
                    break
                else:
                    prev = data[i][j]
                    if explode and not mode:
                        prev[0] = prev[0] + val
                        break
                    elif prev[0] >= 10 and mode:
                        res = div(prev[0])
                        prev[0] = res[0]
                        prev.append(res[1])
                        split = True
                        break
            else:
                continue
            break
        else:
            prev = data[i]
            if explode and not mode:
                prev[0] = prev[0] + val
                break
            elif prev[0] >= 10 and mode:
                res = div(prev[0])
                prev[0] = res[0]
                prev.append(res[1])
                split = True
                break
    return (explode or split, mode)

def mag(l):
    if type(l[0]) == int:
        left = 3 * l[0]
    else:
        left = 3 * mag(l[0])
    if type(l[1]) == int:
        right = 2 * l[1]
    else:
        right = 2 * mag(l[1])
    return left + right

def add_num(data):
    res = data[0]
    unstable = True
    explodable = True
    splitable = True
    prep(res)
    while unstable:
        while explodable:
            explodable = check(res, 0)[0]
        splitable = check(res, 1)[0]
        if splitable:
            explodable = True
        unstable = explodable or splitable
    for i in range(1, len(data)):
        unstable = True
        explodable = True
        splitable = True
        res = add(res, data[i])
        while unstable:
            while explodable:
                explodable = check(res, 0)[0]
            splitable = check(res, 1)[0]
            if splitable:
                explodable = True
            unstable = explodable or splitable
    reprep(res)
    return mag(res)

def part2(data):
    return max(list(map(lambda x: add_num(deepcopy(x)), list(filter(lambda x: x[0] != x[1], [[x,y] for x in data for y in data])))))

print(add_num(deepcopy(datalines)))
print(part2(deepcopy(datalines)))
