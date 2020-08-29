'''
Time comp => O(V*E)
Space comp => O(E) + O(V)
'''

def bellman_ford( graph,v,src ):
    distance = [float('inf')]*(v+1)
    distance[src] = 0
    neg_cycle = False
    
    for i in range(v-1):
        for x,y,w in graph:
            if distance[x] != float('inf') and distance[x] + w < distance[y]:
                distance[y] = distance[x]+w
    
    #detecting a negative cycle

    for j in range(v):
        for x,y,w in graph:
            if distance[x] + w < distance[y]:
                neg_cycle = True
                distance[y] = float('-inf')
    return distance, neg_cycle