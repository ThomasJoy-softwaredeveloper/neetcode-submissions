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
        if not root:
            return 0
        # need two variables to keep track of count and maxm
        # Step 1 : we need to start the dfs by passing the root node and max_value
        # Step 2 : check if the node's value exists 
        # Step 2: (node perspective)
        #   2.1 Check if node exists, if not return 
        #   2.2 If exists -> check if node's value is greater than the max_value if so count increase
        # Step 3: Update the max_value
        # Step 4: recursive call
        # Step 5: return the count
        
        def dfs(node, max_value):
            if not node : return 
            if node and node.val >= max_value:
                self.count += 1

            max_value = max(node.val, max_value)

            dfs(node.left, max_value)
            dfs(node.right, max_value)
        dfs(root, root.val)
        return self.count