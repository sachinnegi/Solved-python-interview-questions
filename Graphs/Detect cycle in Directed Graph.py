def cycle(self,visited,currStack,node,graph):
        visited[node]= True
        currStack[node] = True
        for nbr in graph[node-1]:
            if visited[nbr] == False:
                    if self.cycle(visited,currStack,nbr,graph)==True:
                        return True
                    
            elif currStack[nbr] == True:
                return True
            
                
        currStack[node] = False
        return False
    
    def solve(self, n, graph):
        
        visited = [False]*(n+1)
        currStack = [False]*(n+1)

        for node in range(1,n+1):
            if visited[node]==False:
                if self.cycle(visited,currStack,node,graph):
                    return 1
        return 0
