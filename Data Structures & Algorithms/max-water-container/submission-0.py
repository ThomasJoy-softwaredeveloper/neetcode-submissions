from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        A, maxA = 0, 0
        while l < r:
            if heights[l] < heights[r]:
                A = heights[l] * (r-l)
                l += 1
            else:
                A = heights[r] * (r - l)
                r -= 1
            maxA = max(A, maxA)
        return maxA