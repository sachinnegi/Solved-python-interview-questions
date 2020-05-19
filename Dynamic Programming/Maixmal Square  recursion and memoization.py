'''Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.'''

# recursion + memoization
class Solution:
    def helper(self,i,j,matrix,dp):
        if i>=0 and i<len(matrix) and j>=0 and j<len(matrix[0]):
            if dp[i][j]!=-1:
                return dp[i][j]
            if matrix[i][j]=='1':
                dp[i][j] = 1+min( self.helper(i+1,j,matrix,dp), self.helper(i,j+1,matrix,dp), self.helper(i+1,j+1,matrix,dp) )
                return dp[i][j]
        return 0
            
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        maxi = 0
        dp = [[-1]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    maxi = max(maxi,self.helper(i,j,matrix,dp))
        return maxi**2
