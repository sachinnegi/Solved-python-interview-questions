# DFS Approach   # k*2^n
class Solution:
    def dfs(self,arr,idx,n,temp,target,ans):
        if target==0:
            ans.append(temp)
            return 
        for i in range(idx,n):
            if arr[i]>target:
                break
            self.dfs(arr,i,n,temp+[arr[i]],target-arr[i],ans)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        n  = len(candidates)
        self.dfs(candidates,0,n,[],target,ans)
        return ans


# my approach

class Solution:
    def helper(self,arr,target,i,n,cache,temp,ans):
        if target==0:
            ans.append(temp.split())
            return 
        if i==n or target<0:
            return
        self.helper(arr,target-arr[i],i,n,cache,temp+" "+str(arr[i]),ans)
        self.helper(arr,target,i+1,n,cache,temp,ans)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        self.helper(candidates,target,0,len(candidates),{},"",ans)
        return ans
