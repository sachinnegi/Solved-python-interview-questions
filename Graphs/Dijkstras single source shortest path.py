'''
=> Time Complexity : V * ( log(heapsize) + E*log(heapsize) )
                     V * ( (1+E)*log(heapsize) )  =  V*( E*log(V^2))
                     =  V*E* log(V)      ( where E is max edge from a singele vertex)
                     =  E*log(V)          ( Since total Vertex * max_adjacent edge =  Total edges in the graph)
 
=> Space : O(V)
'''


import heapq

def dijkstras(src,graph):

    heap = heapq.heapify([0,src])
    distance = { vertex: float('inf') for vertex in graph }
    distance[src] = 0

    while heap:
        curr_dis, node = heap.heappop()
        # check if the curr_dis have already been changed by a smaller value from another path
        # while that node was still in the heap
        if curr_dis >= distance[node]:
            continue
        for nbr in graph[node]:
            new_dis = distance[node] + Weight
            if new_dis < distance[nbr]:
                distance[nbr] = new_dis
                heap.heapq.heappush((new_dis,nbr))
                prev[nbr] = node

    return distance, prev
