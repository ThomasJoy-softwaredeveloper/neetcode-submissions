class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {} # {value: index}
        result = []
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in hashMap:
                result.append(i+1)
                result.append(hashMap[diff])
            hashMap[n] = i+1
        return sorted(result)
            
        