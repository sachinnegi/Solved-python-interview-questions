# time comp -> O(log(min(m,n)) binary_search on min. length array   const. space

class Solution:
    def findMedianSortedArrays(self, A, B ) :
        m = len(A)
        n = len(B)
        if m>n:
            return self.findMedianSortedArrays(B,A)
        mini = 0
        maxi = m
        while mini <= maxi:
            i = (mini+maxi)//2     #  partition of A at i
            j = (m+n+1)//2-i       # half element on the left and half on the right of B at j
            
            Left_A = float('-inf') if i==0 else A[i-1]    # no element on left  partition i=0
            Left_B = float('-inf')  if j==0 else B[j-1]   
            Right_A = float('inf')  if i==m else A[i]      # no element on right partition  i=m
            #print(j)
            Right_B = float('inf')  if j==n else B[j]
            
            if Left_A > Right_B:            # we are ahead of mid 
                maxi = i-1
            elif Left_B > Right_A:          # we are behind mid
                mini = i+1
            else:                           # we are at the middle
                if (m+n) % 2 == 0:
                    return ( max(Left_A,Left_B) + min(Right_A,Right_B)) / 2
                else:
                    return max(Left_A,Left_B)
                
