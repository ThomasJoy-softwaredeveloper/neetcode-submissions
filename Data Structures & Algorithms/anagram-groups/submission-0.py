from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_Anagrams = defaultdict(list)
        result = []
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            group_Anagrams[sorted_s].append(s)

        for value in group_Anagrams.values():
            result.append(value)

        return result

        