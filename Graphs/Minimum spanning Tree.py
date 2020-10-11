'''
V: nodes in graph
E: number of edges in graph
graph: adjacency matrix, graph[i][j]=weight, if edge exits , else float("inf").
'''

# KRUSKAL'S MST

def find(parent,node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, x, y):
    xroot = find(parent,x)
    yroot = find(parent,y)
    
    if rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    elif rank[yroot] > rank[xroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def spanningTree(V, E, mat):
    result = []
    rank = []
    parent = []
    graph = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]!= float('inf') and i<j:
                graph.append([i,j,mat[i][j]])
    
    graph = sorted(graph, key=lambda x: x[2])
    # print(graph)
    
    for node in range(V):
        parent.append(node)
        rank.append(0)
    e=0     #take care it is starting from 0
    while e < V-1:
        for u,v,w in graph:
            x = find(parent, u)
            y = find(parent, v)
            if x != y :   # no cycle
                result.append([u,v,w])
                e+=1
                union(parent, rank, x, y)
    min_weight = 0
    for u,v,w in result:
        min_weight += w
    return min_weight
        
