from heapq import *
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap =[]
    
        

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap):
            heappush(self.maxHeap, -num)
            heappush(self.minHeap, -heappop(self.maxHeap))
        else:
            heappush(self.minHeap, num)
            heappush(self.maxHeap, -heappop(self.minHeap))
        

    def findMedian(self) -> float:
     
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2
        else:
            return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()