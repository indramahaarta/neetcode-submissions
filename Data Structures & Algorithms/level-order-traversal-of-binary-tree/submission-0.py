# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res = []
        queue = deque([root])
        while queue:
            temp = []
            next_queue = deque([])
            ctr = 0
            for q in queue:
                ctr += 1
                temp.append(q.val)

                if q.left:
                    next_queue.append(q.left)
                
                if q.right:
                    next_queue.append(q.right)
            
            res.append(temp)
            queue = next_queue
        
        return res
        
        