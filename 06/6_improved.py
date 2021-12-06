datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in datalines:
    data = list(map(int, i.split(",")))

def sim(data, horizon):
    fish = [0] * 9
    for i in data:
        fish[i] += 1
    for i in range(horizon):
        n = fish.pop(0)
        fish[6] += n
        fish.append(n)
    return sum(fish)

print(sim(data, 80))
print(sim(data, 256))
