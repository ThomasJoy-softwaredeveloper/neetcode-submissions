# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = [0]
        def dfs(node, max_value):
            if not node : return 
            if node and node.val >= max_value:
                count[0] += 1

            max_value = max(node.val, max_value)

            dfs(node.left, max_value)
            dfs(node.right, max_value)
        dfs(root, root.val)
        return count[0]