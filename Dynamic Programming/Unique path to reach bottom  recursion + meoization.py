#find total number of unique path to reach from top(0,0) of the matrix to the bottom right(m,n)

# METHOD 1 -> recursion + memoization    time and space -> O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  
        cache = [ [-1]*(n+1) for i in range(m+1)]
        def reach(m,n,cache):
            if m==1 and n==1:
                return 1
            if m<=0 or n<=0:
                return 0
            if cache[m][n]!=-1:
                return cache[m][n]
            cache[m][n] = reach(m-1,n,cache) + reach(m,n-1,cache)
            return cache[m][n]
        return reach(m,n,cache)


# METHOD 2 -> top down approach

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  
        cache = [ [0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                    cache[i][j]= 0
                if i==1 or j==1:
                    cache[i][j]=1
                else:
                    cache[i][j] =  cache[i-1][j]+cache[i][j-1]
        
        return cache[m][n]

#METHOD 3 -> space O(2n)   since it depends only on the current row and previous row 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  
        prev = [1]*(n+1)
        curr = [1]*(n+1)
        for i in range(2,m+1):
            for j in range(2,n+1):
                curr[j] = prev[j] + curr[j-1]
            
            prev,curr = curr,prev
        
        return prev[n]

#METHOD 4 -> space O(n) 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  
        curr = [1]*(n+1)
        for i in range(2,m+1):
            for j in range(2,n+1):
                curr[j] = curr[j] + curr[j-1]
        
        return prev[n]


