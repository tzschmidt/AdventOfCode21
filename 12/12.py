datafile = "data.txt"

with open(datafile) as f:
    datalines = f.read().splitlines()

nodes = {}
n = 0
adj = []

for i in range(len(datalines)):
    datalines[i] = datalines[i].split("-")
    for j in datalines[i]:
        if j not in nodes: 
            nodes.update({j: n})
            adj.append([])
            n += 1
    if datalines[i][1] not in adj[nodes[datalines[i][0]]]:
        adj[nodes[datalines[i][0]]].append(datalines[i][1])
    if datalines[i][0] not in adj[nodes[datalines[i][1]]]:
        adj[nodes[datalines[i][1]]].append(datalines[i][0])

def dfs(nodes, adj, node, end, visited, stack, paths, extra):
    stack.append(node)
    if node.islower():
        if node in extra and len(extra) > 1:
            extra.pop()
        else:
            visited.append(node)
    if node == end:
        paths.update([tuple(stack[:])])
    else:
        for i in adj[nodes[node]]:
            if i not in visited:
                dfs(nodes, adj, i, end, visited, stack, paths, extra)
    stack.pop()
    if node in visited:
        visited.remove(node)
    elif node in extra and len(extra) == 1:
        extra.append(node)

def func(nodes, adj, start, end, part2):
    visited = []
    stack = []
    paths = set()
    if part2:
        for i in nodes:
            if i.islower() and i != "end" and i != "start" :
                dfs(nodes, adj, start, end, visited, stack, paths, [i, i])
    else:
        dfs(nodes, adj, start, end, visited, stack, paths, [])
    return paths

print(len(func(nodes, adj, "start", "end", 0)))
print(len(func(nodes, adj, "start", "end", 1)))
