# Method 1 memoization   space -> O(n*total) time -> O(n*total)   =>in recustion O(2^n) because for each weight either choose or don't choose.
'''The runtime of the dynamic algorithm = (time to solve each subproblem)*(number of unique subproblems)
Typically,
the cost = (outdegree of each vertex)*(number of vertices)'''
class Solution:
    def minimumsubset(self, stones):
        n = len(stones)
        total =sum(stones)
        self.dp =[ [-1]*(total+1) for j in range(n+1)]
        
        def minsum(stones,n,total,calsum):
            if n==0:
                return abs(total-2*calsum)
            if self.dp[n][calsum] != -1:
                return self.dp[n][calsum]
            self.dp[n][calsum] =  min(minsum(stones,n-1,total,calsum), minsum(stones,n-1,total,calsum+stones[n-1]))
            return self.dp[n][calsum]
        
        return minsum(stones,len(stones),sum(stones),0)

# METHOD 2  bottom up    space -> O(total)

class Solution:
    def lastStoneWeightII(self, stones):
        n=len(stones)
        total = sum(stones)
        dp = [False]*(total//2+1)
        dp[0] = True
        for stone in stones:
            for j in range(total//2,0,-1):      # dont wan't to overwrite our value 
                if stone <= j:
                    dp[j] = dp[j] or dp[j-stone]
        for i in range(total//2,-1,-1):      # max value at last of dp which is achievable
            if dp[i] ==True:
                return total - 2*i


        
