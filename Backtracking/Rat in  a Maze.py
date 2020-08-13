# rat in a maze total number of ways to reach right bottom

def isSafe(graph,i,j,m,n):
    if 0<=i<m and 0<=j<n and graph[i][j]==1:
        return True
    return False
    
def dfs(graph,i,j,m,n,arr,st):
    if i==m-1 and j==n-1 and graph[i][j]==1:
        arr.append(st)
        return 
    if isSafe(graph,i,j,m,n):
        graph[i][j]=0 #choose
        
        dfs(graph,i+1,j,m,n,arr,st+'D')
        dfs(graph,i,j-1,m,n,arr,st+'L')
        dfs(graph,i,j+1,m,n,arr,st+'R')
        dfs(graph,i-1,j,m,n,arr,st+'U')
        
        graph[i][j] = 1 # unchoose
        
def findPath(graph, n):
    arr=[]
    st=""
    dfs(graph,0,0,len(graph),len(graph[0]),arr,st)
    if arr:
        return (" ".join(arr))
    return -1
