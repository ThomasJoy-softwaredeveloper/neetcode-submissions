class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        def dfs(curr, remaining):
            if len(remaining) == 0:
                res.append(curr[:])
                return
            
            for i in range(len(remaining)):
                node = remaining[i]
                temp = curr + [node]
                dfs(temp, remaining[:i] + remaining[i+1:])

        dfs(stack, nums)
        res.sort()
        return res           