class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, n)

            # By maintaining the length of the heap as k we eventually get the kth largest
            if len(heap) > k:
                heapq.heappop(heap)
        
        print(heap)
        return heap[0]