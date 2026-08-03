# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def getGoodNode(root: TreeNode, c) -> None:
            nonlocal res
            if not root:
                return
            
            val = max(c, root.val)

            if val <= root.val:
                res += 1
            getGoodNode(root.left, val)
            getGoodNode(root.right, val)
    
        getGoodNode(root, root.val)
        return res

        