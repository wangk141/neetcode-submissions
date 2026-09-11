# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import sys

    sys.setrecursionlimit(1000000000)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def dfs(node):
            nonlocal total
            if not node:
                return
            dfs(node.right)
            tmp = node.val
            node.val += total
            total += tmp
            
            dfs(node.left)
        
        dfs(root)
        return root