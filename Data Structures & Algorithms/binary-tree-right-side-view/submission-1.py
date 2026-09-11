# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        ret = []
        while q:
            lenQ = len(q)
            level = -101
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    if level == -101:
                        level = node.val
                        ret.append(level)

                    q.append(node.right)
                    q.append(node.left)
        return ret
                    
                