# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxPath = float('-inf')  # Initialize to negative infinity

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            # Recursively get the maximum path sum from left and right subtrees
            left = max(dfs(node.left), 0)  # Only add positive contributions
            right = max(dfs(node.right), 0)  # Only add positive contributions
            
            # Update the maximum path sum found so far
            self.maxPath = max(self.maxPath, node.val + left + right)
            
            # Return the maximum path sum "starting" from this node
            return node.val + max(left, right)

        dfs(root)
        return self.maxPath