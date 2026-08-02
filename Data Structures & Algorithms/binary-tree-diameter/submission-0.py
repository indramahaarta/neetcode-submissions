# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        curMax = 0
        def helper(node):
            nonlocal curMax
            if not node:
                return 0

            leftHeight = helper(node.left)
            rightHeight = helper(node.right)
            curMax = max(curMax, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1
        
        helper(root)
        return curMax

        
        