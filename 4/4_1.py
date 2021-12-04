datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().split('\n\n')

data = [0] * len(datalines)

# format input
for i in range(len(datalines)):
    x = datalines[i].replace(",", " ")
    x = x.replace("\n", " ")
    data[i] = x.split(" ")
    while "" in data[i]:
        data[i].remove("")
    data[i] = list(map(int,data[i]))

# check for hit
def check(block, num, mark):
    for i in range(len(block)):
        if block[i] == num:
            mark[i] = 1
            return True
    return False

# calc result if won
def win(block, mark, num):
    s = 0
    for i in range(len(block)):
        if not mark[i]:
            s += block[i]
    s *= num
    return s

# check for win
def checkwin(block, mark, num):
    # horizontal win
    for i in range(0, len(mark), 5):
        if mark[i] and mark[i+1] and mark[i+2] and mark[i+3] and mark[i+4]:
            return win(block, mark, num)
    # vertical win
    for i in range(0, 5):
        if mark[i] and mark[i+5] and mark[i+10] and mark[i+15] and mark[i+20]:
            return win(block, mark, num)
    return 0        


def bingo(data):
    marker = [[0 for columns in range(25)] for rows in range(len(data)-1)]
    for i in data[0]:
        for j in range(1, len(data)):
            if check(data[j], i, marker[j-1]):
                result = checkwin(data[j], marker[j-1], i)
                if result:
                    return result
    return 0

print(bingo(data))

