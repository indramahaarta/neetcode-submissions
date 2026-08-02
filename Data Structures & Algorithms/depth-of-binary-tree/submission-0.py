# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = [root]
        res = 0
        while l:
            local_l = []
            while l:
                val = l.pop()
                if val.right:
                    local_l.append(val.right)
                if val.left:
                    local_l.append(val.left)
                
            l = local_l
            res += 1
        
        return res
            

        