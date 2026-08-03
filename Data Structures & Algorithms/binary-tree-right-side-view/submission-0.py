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
        
        queue = deque([root])
        res = []
        while queue:
            l = len(queue)
            havePop = False
            for i in range(l):
                cur = queue.popleft()
                if not havePop:
                    res.append(cur.val)
                    havePop = True
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        return res
        
        
        