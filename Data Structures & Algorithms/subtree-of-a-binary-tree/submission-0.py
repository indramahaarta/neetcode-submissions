# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        
        isSubTreeLeft = self.isSubtree(root.left, subRoot) if root.left else False
        isSubTreeRight = self.isSubtree(root.right, subRoot) if root.right else False

        return isSubTreeLeft or isSubTreeRight
    
    def isSameTree(self, r: TreeNode, s: TreeNode) -> bool:
        if not r and not s:
            return True
        elif (not r and s) or (r and not s):
            return False
        
        if r.val != s.val:
            return False
        
        return self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right)
        