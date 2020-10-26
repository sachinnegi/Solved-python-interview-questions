# Method 1 -> Two Pointer
'''
Time : O(n)
Space : O(1)
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0:
            return 0
        left, right = height[0], height[len(height)-1]
        l,r = 0, len(height)-1
        total = 0
        while l<=r:
            left = max(left,height[l])
            right = max(right, height[r])
            if height[l]<height[r]:
                total+= max(0, min(left,right) - height[l])
                l+=1
            else:
                total+= max(0, min(left,right) - height[r])
                r-=1
        return total
                

# Method 2 -> Stack based
'''
Space : O(n)
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0:
            return 0
        stack = []
        ans = 0
        for i,h in enumerate(height):
            while stack and h>height[stack[-1]]:
                top = stack.pop()
                if stack:
                    width = i-stack[-1]-1
                    ans+= (min(height[stack[-1]],h) - height[top] )*width
            stack.append(i)
            
        return ans
            
