#time complextiy -> O(M^v)      m=colors, v= vertex

def isSafe(graph,vertex,node,color):
    for nbr in graph[node]:
        if color == vertex[nbr]:
            return False
    return True
def solve(graph,vertex,M,V,node):
    if node==V+1:
        return True
    for color in range(1,M+1):
        if isSafe(graph,vertex,node,color):
            vertex[node] = color
            if solve(graph,vertex,M,V,node+1):
                return True
            vertex[node] = -1
        
            

for _ in range(int(input())):
    V=int(input())
    M = int(input())
    E= int(input())
    arr=list(map(int,input().split()))
    graph = [[] for i in range(V+1)]
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])
    #print(graph)
    vertex = [-1]*(V+1)
    if solve(graph,vertex,M,V,1):
        print(1)
    else:
        print(0)
    
