# space complexity -> O(n),   time comp. -> O(n^2) 

class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0],G[1]=1,1  # either empty tree or single node
        for i in range(2,n+1):
            for j in range(i):
                G[i] += G[j] * G[i-j-1]       # adding combination of total from left subtree and right subtree
        return G[n]
        
