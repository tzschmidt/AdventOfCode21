datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in range(len(datalines)):
    datalines[i] = list(map(int, list(datalines[i])))

def func(data):
    risk = 0
    adj = [[None for x in range(len(data[0]))] for x in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i == 0:
                if j == 0:
                    adj[i][j] = [data[i][j+1], data[i+1][j]]
                elif j == len(data[i])-1:
                    adj[i][j] = [data[i][j-1], data[i+1][j]]
                else:
                    adj[i][j] = [data[i][j-1], data[i][j+1], data[i+1][j]]
            elif i == len(data)-1:
                if j == 0:
                    adj[i][j] = [data[i][j+1], data[i-1][j]]
                elif j == len(data[i])-1:
                    adj[i][j] = [data[i][j-1], data[i-1][j]]
                else:
                    adj[i][j] = [data[i][j-1], data[i][j+1], data[i-1][j]]
            else:
                if j == 0:
                    adj[i][j] = [data[i][j+1], data[i+1][j], data[i-1][j]]
                elif j == len(data[i])-1:
                    adj[i][j] = [data[i][j-1], data[i+1][j], data[i-1][j]]
                else:
                    adj[i][j] = [data[i][j+1], data[i][j-1], data[i+1][j], data[i-1][j]]
            if all(data[i][j] < x for x in adj[i][j]):
                risk += data[i][j] + 1
    return risk

print(func(datalines))
