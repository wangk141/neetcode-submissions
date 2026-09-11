# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            counter = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            counter += dfs(node.left, maxVal)
            counter += dfs(node.right, maxVal)
            return counter
        return dfs(root, root.val)