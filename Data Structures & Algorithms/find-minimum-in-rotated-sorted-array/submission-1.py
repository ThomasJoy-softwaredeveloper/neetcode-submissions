class Solution:
    def findMin(self, nums: List[int]) -> int:
        curr_min = float("inf")
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2 
            curr_min = min(nums[mid], curr_min)
            if nums[r] < curr_min:
                l = mid + 1
            else:
                r = mid - 1 
        return min(curr_min, nums[l])