# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def rec(node, deep):
            nonlocal mx
            if not node:
                mx = max(mx, deep)
                return
            
            rec(node.left, deep + 1)
            rec(node.right, deep + 1)
        
        rec(root, 0)
        return mx
        