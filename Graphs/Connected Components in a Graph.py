n,e = map(int,input().split())
graph = [[] for i in range(n)]
for i in range(e):
    u,v = map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)

def dfs(node,graph,component,count,visited):
    component[node] = count
    for nbr in graph[node]:
        if visited[nbr] == False:
            visited[nbr]  = True
            dfs(nbr,graph,component,count,visited)


visited = [False]*n
count = 0
component = [i for i in range(n)]
for node in range(n):
    if visited[node] == False:
        count+=1
        visited[node] = True
        dfs(node,graph,component,count,visited)
print(count)

