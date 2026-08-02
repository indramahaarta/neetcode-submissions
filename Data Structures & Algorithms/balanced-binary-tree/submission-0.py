# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalance = True

        def findDiff(node) -> int:
            nonlocal isBalance 
            if not node:
                return 0

            heightL = findDiff(node.left)
            heightR = findDiff(node.right)
            if abs(heightL - heightR) > 1:
                isBalance = False

            return max(heightL, heightR) + 1
        
        findDiff(root)
        
        return isBalance





        