'''
Time comp.   -> O(n^3)
Space comp.  -> O(n^2)
'''

def floyd_Warshall(v,graph):
    dist = [[float('inf')]*v for i in range(v)]
    for u,v,w in graph:
        dis[u][v] = dis[v][u] = w
    for i in range(n):
        dis[i][j] = 0

    #take  all vertices to be intermediate vertex
    for k in range(v):
        
        # take all vertices to be source vertex
        for i in range(v):
            
            #take all vertices to be destination vertex
            for j in range(v):
                dis[i][j] = min( dis[i][j], dis[i][k] + [k][j] )

    return dist

    # for identifying if negative cycle is present or not in the graph run the
    # above algo one more time and if dis[i][j] decreases then set dis[i][j] = -inf
    # and cycle is present in it.
