# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        mn = min(q.val, p.val)
        mx = max(q.val, p.val)
        if root.val <= mx and root.val >= mn: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        if left: return left

        right = self.lowestCommonAncestor(root.right, p, q)
        if right: return right

        return None