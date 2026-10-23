class MedianFinder:
    def __init__(self):
        # self.small is defined as maxHeap
        # self.large is defined as minHeap
        self.small, self.large = [], []
    def addNum(self, num):
        heapq.heappush(self.small, -1 * num)
        
        # All values that we have in small should be less than what we have in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # check if we have an uneven length
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        print("The length of small : ", len(self.small), "the length of large : ", len(self.large))
        return (-1 * self.small[0] + self.large[0]) / 2
