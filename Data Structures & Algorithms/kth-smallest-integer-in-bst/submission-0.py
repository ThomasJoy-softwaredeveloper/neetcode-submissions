# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [0]
        backtrack = [0]
        def dfs(curr, k):
            if curr and curr.left:
                dfs(curr.left, k)
            
            backtrack[0] = backtrack[0] + 1

            if backtrack[0] == k:
                ans[0] = curr.val
                return 
            if curr and curr.right:
                dfs(curr.right, k)

        dfs(root, k)

        return ans[0]