from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = [] to store the list of values
        # curr_window = [] list to store the current k values
        # check if the given nums array has k values else return res immediately
        
        # if len(nums) <= k:
        #     res = [max(nums)]
        #     return res

        # res = []
        # curr_window = []
        # l = 0
        # for r in range(len(nums)):
        #     curr_window.append(nums[r])
        #     if len(curr_window) == k:
        #         res.append(max(curr_window))
        #         curr_window.remove(nums[l])
        #         l += 1
        # return res


        res = []  # Store the result
        dq = deque()  # Store the indices of useful elements
        l = 0  # Left boundary of the window

        for r in range(len(nums)):  # r is the right boundary of the window
            # Remove indices of elements not within the window
            if dq and dq[0] < l:
                dq.popleft()

            # Remove elements from the back of the deque that are smaller
            # than the current element, as they won't be useful
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            # Add the current element's index to the deque
            dq.append(r)

            # When we have a valid window of size k, record the max
            if r >= k - 1:
                res.append(nums[dq[0]])  # The front of the deque is the max
                l += 1  # Slide the window

        return res
