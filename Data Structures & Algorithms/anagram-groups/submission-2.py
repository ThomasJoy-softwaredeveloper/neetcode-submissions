class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = {}

        for s in strs:
            ns = tuple(sorted(s))
            if ns in Map:
                Map[ns].append(s)
            else:
                Map[ns] = [s]
        return Map.values()