class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]  
        # here index is the count and the value is the list of numbers that have that count 

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []

        i = len(freq) - 1

        while i > 0:
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
            i = i - 1