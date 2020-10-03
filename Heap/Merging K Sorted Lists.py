# Time Complexity -> K + nlogK      where n is total number of elements in the list and k is total number of lists
# Space Complexity -> k 

import heapq
class Solution:
    def solve(self, lists):
        res = []
        heap = []
        for row,arr in enumerate(lists):
            if arr:
                heapq.heappush(heap,(arr[0], row, 0 ))
        while heap:
            ele, row, col = heapq.heappop(heap)
            res.append(ele)
            if col<len(lists[row])-1:
                heapq.heappush(heap, (lists[row][col+1], row, col+1) )
        return res
        
        
        

