datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()
    
for i in range(len(datalines)):
    datalines[i] = datalines[i].split(" | ")
    for j in range(len(datalines[i])):
        datalines[i][j] = list(map(set,(datalines[i][j].split(" "))))

def func(data):
    result = [None] * len(data)
    for i in range(len(data)):
        result[i] = [None] * len(data[i][1]) 
        num = [set()] * 10
        for j in range(len(data[i][0])):
            x = len(data[i][0][j])
            element = data[i][0][j]
            if x == 2:
                num[1] = element
                #data[i][0].remove(element)
                data[i][0][j] = 0
            elif x == 3:
                num[7] = element
                data[i][0][j] = 0
            elif x == 4:
                num[4] = element
                data[i][0][j] = 0
            elif x == 7:
                num[8] = element
                data[i][0][j] = 0
        data[i][0] = list(filter((0).__ne__, data[i][0]))
        while len(data[i][0]) != 0: 
            for j in range(len(data[i][0])):
                element = data[i][0][j]
                if num[4] < (element):
                    num[9] = element
                    data[i][0][j] = 0
                elif (num[8] - (num[4] - num[1])) < element:
                    num[0] = element
                    data[i][0][j] = 0
                elif (num[8] - num[1]) < element:
                    num[6] = element
                    data[i][0][j] = 0
                elif ((num[4] - num[0]) | num[1]) < element and num[9] and num[0]:
                    num[3] = element
                    data[i][0][j] = 0
                elif (num[4] & num[6]) < element and num[6] and num[9]:
                    num[5] = element
                    data[i][0][j] = 0
                elif (num[8] - num[4]) < element and num[6] and num[0]:
                    num[2] = element
                    data[i][0][j] = 0
            data[i][0] = list(filter((0).__ne__, data[i][0]))
        for j in range(len(data[i][1])):
            for k in range(len(num)):
                if data[i][1][j] == num[k]:
                    result[i][j] = k
        result[i] = int("".join(str(l) for l in result[i])) 
    return sum(result)
                    
print(func(datalines))
