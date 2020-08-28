def dfs(node,graph,result,visited):
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(nbr,graph,result,visited)
    result.append(node)

def topoSort(n, graph):
    result = []
    visited = set()
    for node in range(n):
        if node not in visited:
            dfs(node,graph,result,visited)
    return result[::-1]