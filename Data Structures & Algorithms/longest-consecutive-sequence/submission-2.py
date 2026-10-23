class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)

        for n in nums:

            if (n - 1) not in numsSet:
                length = 0
                while (n + length) in numsSet:
                    length += 1
                res = max(res, length)
        return res
