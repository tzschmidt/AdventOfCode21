datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

for i in range(len(datalines)):
    datalines[i] = list(datalines[i])

def equal(closing, opening):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    if opening == '<' and closing == '>':
        return True
    return False

def func(data):
    illegal = list()
    for i in range(len(data)):
        stack = list()
        for j in range(len(data[i])):
            if data[i][j] in ['(', '[', '{', '<']:
                stack.insert(0, data[i][j])
            elif data[i][j] in [')', ']', '}', '>'] and equal(data[i][j], stack[0]):
                stack.pop(0)
            else:
                illegal.append(data[i][j])
                break
    return sum(list(map(lambda a: 3 if a == ')' else (57 if a == ']' else (1197 if a == '}' else 25137)), illegal)))

print(func(datalines))
