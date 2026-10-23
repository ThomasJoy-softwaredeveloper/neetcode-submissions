from typing import List

class Solution:

    def __init__(self):
        self.permutations = []

    def dfs(self, current, remaining):
        if len(remaining) == 0:
            self.permutations.append(current[:])  # Append a copy of current
            return

        for i in range(len(remaining)):
            node = remaining[i]
            temp = current[:]  # Make a copy of current
            temp.append(node)
            self.dfs(temp, remaining[:i] + remaining[i+1:])  # Pass remaining excluding node

    def permute(self, nums: List[int]) -> List[List[int]]:
        current = []
        self.dfs(current, nums)
        return self.permutations
