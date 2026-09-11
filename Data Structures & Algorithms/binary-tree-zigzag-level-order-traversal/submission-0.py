# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        res = []
        if not root:
            return []
        counter = 0
        while q:
            temp = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                temp.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if counter % 2 == 1:
                temp.reverse()
            counter += 1
            res.append(temp)
        return res
        

        
        
