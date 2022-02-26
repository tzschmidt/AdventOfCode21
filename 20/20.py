from copy import deepcopy

datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().split("\n\n")
    datalines[1] = datalines[1].splitlines()

def format_input(s):
    return list(map(lambda a: a.replace("#", "1").replace(".", "0"), s))

data = [format_input(datalines[0]), list(map(format_input, datalines[1]))]

def prep_matrix(m, n):
    x = 2*n+1
    return list(map(lambda a: ['0']*x + a + ['0']*x, [['0']*len(m[0])]*x + m + [['0']*len(m[0])]*x))

def get_val(m, x, y):
    return int("".join(list(map(lambda a: "".join(a[x-1:x+2]), m[y-1:y+2]))), 2)

def func(data, n):
    algo = data[0]
    matrix = prep_matrix(data[1], n)
    res = deepcopy(matrix)
    for i in range(n):
        default = algo[get_val(matrix, 1, 1)]
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[0])):
                if y == 0 or x == 0 or y == len(matrix)-1 or x == len(matrix[0])-1:
                    v = default
                else:
                    v = algo[get_val(matrix, x, y)]
                res[y][x] = v
        matrix = deepcopy(res)
    return sum(list(map(sum, list(map(lambda a: list(map(int, a)), res)))))

print(func(data,2))
print(func(data,50))
