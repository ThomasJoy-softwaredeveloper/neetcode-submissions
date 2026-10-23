class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Freq = {}
        res = []
        for n in nums:
            Freq[n] = 1 + Freq.get(n, 0)

        topK = [[] for i in range(len(nums) + 1)]

        for n, c in Freq.items():
            topK[c].append(n)
        
        for i in range(len(topK) - 1, 0, -1):
            for n in topK[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return 
