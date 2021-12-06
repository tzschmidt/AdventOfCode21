datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in datalines:
    data = list(map(int, i.split(",")))

def sim(fish, horizon):
    for i in range(horizon):
        n = fish.count(0)
        fish = list(map(lambda a: 6 if a == 0 else a - 1, fish))
        fish.extend([8] * n)
    return len(fish)

print(sim(data, 80))
