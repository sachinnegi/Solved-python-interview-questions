# METHOD 1    Recursion + Memoization      time -> O(n*space) space -> O(n*space) 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1 != 0:    # not even can't be divided
            return False
        else:
            total = total//2
        memo = [[-1]*(total+1) for i in range(n+1)]
        return self.helper(nums,total, n, memo)
    
    
    def helper(self,nums,total,n,memo):
        if total == 0:    # found answer or can always get a empty subset
            return True
        if n==0 and total!=0:           # total!=0 and  got end of array 
            return False
        
        if memo[n][total] != -1:   # already calculated
            return memo[n][total]
        
        if nums[n-1] > total:    # skip this item
            memo[n][total] = self.helper(nums,total,n-1,memo)
            return memo[n][total] 


        memo[n][total] = self.helper(nums, total-nums[n-1], n-1, memo) or self.helper(nums, total, n-1, memo)
        return memo[n][total]


#METHOD 2   BOTTOM UP     -> space O(n*space)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1 != 0:    # not even can't be divided
            return False
        else:
            total = total//2
        memo = [[False]*(total+1) for i in range(n+1)]
        
        for i in range(0,n+1):
            memo[i][0] = True
        for i in range(1,n+1):
            for j in range(1,total+1):
                
                memo[i][j] = memo[i-1][j]
                if j>=nums[i-1]:
                    memo[i][j] = memo[i-1][j] or memo[i-1][j - nums[i-1]]
        #print(memo)
        return memo[n][total]


#METHOD 3     -> O(space)

''' Thus if you merge array1 and array2 to a single array array, if you update array backwards, all dependencies are not touched!

     (n represents new value, i.e. updated)
 	. . ? . . ? n n n n n n n
                  #  
 However if you update forwards, dp[j - nums[i - 1]] is updated already, you cannot use it:

     (n represents new value, i.e. updated)
 	n n n n n ? . . . . . .  where another ? goes? Oops, it is overriden, we lost it :(
                  #  
'''
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1 != 0:    # not even can't be divided
            return False
        else:
            total = total//2
        memo = [False]*(total+1)
        memo[0] = True
                        
        for i in range(n):
            for j in range(total,0,-1):   # reason for going backword is that for current dp[i][j] we have to depend on previous row hence on going from backward
                                          # the value of current row obtained from previous row is not changed since dp[i] = dp[i-num] || dp[i] and bigger value
                                          # depend upon lower current row which is not yet changed for the current num[i] .But going from 0 to total the value of
                                          # smaller value are already changed for the current row (nums[i]) hence the value dp[i-num] have not have value obatined
                                          # form previous row.
                if j >= nums[i]:
                    memo[j] = memo[j-nums[i]] or memo[j]
        return memo[total]
        
        
    
                    
    
    
    


            
