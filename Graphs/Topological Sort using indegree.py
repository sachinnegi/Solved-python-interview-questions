def topoSort(n, adj):
    indegree = [0]*(n)
    for nbr in adj.values():
        for node in nbr:
            indegree[node]+=1
    ans = []
    que = []
    for i in range(0,n):
        if indegree[i]==0:
            que.append(i)
    while que:
        val = que.pop(0)
        ans.append(val)
        
        for nbr in adj[val]:
            indegree[nbr]-=1
            if indegree[nbr]==0:
                que.append(nbr)
    #print(ans)
    return ans