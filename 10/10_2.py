datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in range(len(datalines)):
    datalines[i] = list(datalines[i])

def invert(bracket):
    switch = {
            '(':')',
            '[':']',
            '{':'}',
            '<':'>',
            ')':'(',
            ']':'[',
            '}':'{',
            '>':'<'
            }
    return switch.get(bracket, "error")

def matching(x, y):
    if x == invert(y):
        return True
    return False

def value(bracket):
    switch = {
            ')':1,
            ']':2,
            '}':3,
            '>':4
            }
    return switch.get(bracket, "error")

def func(data):
    scores = list()
    for i in range(len(data)):
        correct = True
        stack = list()
        s = 0
        for j in range(len(data[i])):
            if data[i][j] in ['(', '[', '{', '<']:
                stack.insert(0, data[i][j])
            elif data[i][j] in [')', ']', '}', '>'] and matching(data[i][j], stack[0]):
                stack.pop(0)
            else:
                correct = False
                break
        if correct and len(stack) != 0:
            for j in stack:
                x = invert(j)
                data[i].append(x)
                s = s * 5 + value(x)
            scores.append(s)
    return sorted(scores)[len(scores)//2]

print(func(datalines))
