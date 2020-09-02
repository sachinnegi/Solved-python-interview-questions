'''
Time Comp. -> O(E+V)
Space Comp. -> O(V)
'''



from collections import defaultdict

def topDFS(node,graph,visit,stack):
    visit.add(node)
    for nbr in graph[node]:
        if nbr not in visit:
            topDFS(nbr, graph, visit, stack)
    stack.append(node)

def dfs(node,graph,visit,count):
    count+=1
    visit.add(node)
    for nbr in graph[node]:
        if nbr not in visit:
            count += dfs(nbr, graph, visit, 0)
    return count

def transpose(graph):
    newGraph = defaultdict(list)
    for node in graph:
        for nbr in graph[node]:
            newGraph[nbr].append(node)
    return newGraph



n,m = map(int,input().split())

graph = defaultdict(list)
for i in range(m):
    x,y = map(int,input().split())
    
    graph[x].append(y)

visit = set()
stack = []
for node in range(1,n+1):
    if node not in visit:
        topDFS(node,graph,visit,stack)

newGraph = transpose(graph)
visit.clear()

totalSSC = 0
oddSSC = 0
evenSSC = 0

while stack:
    node = stack.pop()
    if node not in visit:
        totalSSC+=1
        result = dfs(node, newGraph, visit, 0)
        if result%2 != 0:
            oddSSC += result
        else:
            evenSSC += result
print(oddSSC-evenSSC)
print(totalSSC)



