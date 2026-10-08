# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        mx = -float('inf')
        def dfs(root):
            nonlocal mx
            if not root:
                return -float('inf')

            left = dfs(root.left)
            right = dfs(root.right)
            mx = max(mx, left + right + root.val, left, right)

            return max(max(left, right) + root.val, root.val)
        
        return max(dfs(root), mx)


        