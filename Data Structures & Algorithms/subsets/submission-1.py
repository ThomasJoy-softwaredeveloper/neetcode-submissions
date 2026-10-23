class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        def dfs(i):
            if i >= len(nums):
                res.append(stack[:])
                return
            
            # decision to add the value
            if i < len(nums):
                val = nums[i]
                stack.append(val)
                dfs(i + 1)

            # decision to not add the value
            stack.pop()
            dfs(i + 1)
        dfs(0)
        return res