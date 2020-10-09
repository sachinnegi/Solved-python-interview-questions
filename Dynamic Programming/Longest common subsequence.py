# Time and Space -> O(n^2)

class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        m,n = len(A), len(B)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j] =0
                elif A[i-1] == B[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1] )
        return dp[m][n]
        
