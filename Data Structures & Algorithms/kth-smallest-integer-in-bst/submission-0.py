# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        ptr = 0
        def bst(root, k) -> None:
            nonlocal ptr, ans

            if ans:
                return 

            if not root:
                return
            
            bst(root.left, k)
            ptr += 1
            # print(root.val, ptr, k)

            if ptr == k:
                ans = root

            bst(root.right, k)
        
        bst(root, k)

        return ans.val
        