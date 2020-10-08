# Time -> O(nlogn)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [0]*(len(nums))
        size = 0
        
        for ele in nums:
            i = 0; j = size-1
            while i<=j:
                mid = (i+j)//2
                if arr[mid] <ele:
                    i = mid+1
                elif arr[mid]>ele:
                    j = mid-1
                else:
                    i = mid
                    break
            arr[i] = ele
            size = max(i+1, size)
        return size
                    
