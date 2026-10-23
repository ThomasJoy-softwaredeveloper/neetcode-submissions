# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        # here we use a list to store the result coz lists are mutable objects
        def dfs(root):
        # we are gonna return the height of the root node at the end
        # we are gonna calculate the height of each particular node
            if not root: return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)

        dfs(root)
        return res[0]