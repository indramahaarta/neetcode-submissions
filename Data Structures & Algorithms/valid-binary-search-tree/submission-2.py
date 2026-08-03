# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helperBST(root, l, r):
            if not root:
                return True
            
            if root.val >= r or root.val <= l:
                return False 
            
            return helperBST(root.left, l, root.val) and helperBST(root.right, root.val, r)
        
        return helperBST(root, -float('inf'), float('inf'))
    

        