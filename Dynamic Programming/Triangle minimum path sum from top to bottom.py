#Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# METHOD 1  ->top down approach

def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):               #since length of every row will be different
                if j==0 :                                   #corner elements    
                    triangle[i][j] += triangle[i-1][j]
                elif j==len(triangle[i])-1:                 #corner elements
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min( triangle[i-1][j-1], triangle[i-1][j])   #middle elements
        return min(triangle[-1])



# METHOD 2  -> bottom up approach

def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2,-1,-1):          #start from second last layer
            for j in range(len(triangle[i])):
                triangle[i][j] += min( triangle[i+1][j], triangle[i+1][j+1])    #check min of bottom for (i,j)
        return triangle[0][0]


# METHOD 3 -> O(n) space

def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=triangle[-1]  # since after calculating current layer  it will become useless in upper calculations hence we can use 1D array
        for i in range(len(triangle)-2,-1,-1):          #start from second last layer
            for j in range(len(triangle[i])):
                dp[j] = min( dp[j+1], dp[j]) + triangle[i][j]    #check min of bottom for (i,j)
        return dp[0]


# METHOD 4 -> memoization + recursion

def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def total(arr,dp,i,j):
            if i>=len(arr):
                return 0
            if j>=len(arr[i]):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = arr[i][j]+ min(total(arr,dp,i+1,j), total(arr,dp,i+1,j+1))
            return dp[i][j]
        arr= triangle
        dp = [[-1]*(len(arr[i])) for i in range(len(arr))]
        total(arr,dp,0,0)
        print(dp)
        return dp[0][0]

