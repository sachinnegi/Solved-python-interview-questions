def dfs(visited,node,par,graph):
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            if dfs(visited,nbr,node,graph):
                return True
        elif nbr!=par:
            return True
    return False

def isCyclic(g,n):
    visited = set()
    for i in range(n):
        if i not in visited:
            if dfs(visited,i,-1,g):
                return 1
    return 0
