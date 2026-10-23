class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = [] to store the list of values
        # curr_window = [] list to store the current k values
        # check if the given nums array has k values else return res immediately
        
        if len(nums) <= k:
            res = [max(nums)]
            return res

        res = []
        curr_window = []
        l = 0
        for r in range(len(nums)):
            curr_window.append(nums[r])
            if len(curr_window) == k:
                res.append(max(curr_window))
                curr_window.remove(nums[l])
                l += 1
        return res