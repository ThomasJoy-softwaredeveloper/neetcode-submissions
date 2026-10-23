class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapValues = dict() # (value, index)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapValues:
                return [mapValues[diff], i]
            mapValues[n] = i
        
        return 

        