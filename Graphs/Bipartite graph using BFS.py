class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0]*(n)
        visited = [False]*(n)
        for i in range(n):
            if visited[i] == False:
                que = deque([i])
                color[i] = 1
                while que:
                    node  = que.popleft()
                    visited[node] = True

                    for nbr in graph[node]:
                        if visited[nbr] == False:
                            que.append(nbr)
                            color[nbr] = 0-color[node]
                        elif color[nbr] == color[node]:
                            print(nbr,node)
                            print(color)
                            return False
        return True
        
