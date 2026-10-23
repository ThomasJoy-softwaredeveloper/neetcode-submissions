# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxm):
            if not node:
                return 
            
            if node.val >= maxm:
                self.count += 1

            maxm = max(node.val, maxm)
            
            dfs(node.left, maxm)
            dfs(node.right, maxm)

        dfs(root, root.val)
        return self.count
        