class Solution:
    
    def dfs(self,node,color,graph,c):
        color[node] = c
        for nbr in graph[node]:
            if color[nbr] == 0:
                if self.dfs(nbr,color,graph,-c) == False:
                    return False
            elif color[node] == color[nbr]:
                return False
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0]*(n)
        for i in range(n):
            if color[i] == 0:
                if self.dfs(i,color,graph,1) == False:
                    return False
        return True
