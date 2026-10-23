class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # creating a set to make checkings easy
        numSet = set(nums)
        longest = 0

        # we are using a for loop to iterate through the input array
        for n in nums:
            # check if the particular number is the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest