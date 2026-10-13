# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def dfs(root):
            nonlocal res
            if res:
                res += ","
            if not root:
                res += "n"
                return
            
            res += str(root.val)
            dfs(root.left)
            dfs(root.right)
        # print(res)
        dfs(root)
        # print(res)
        return res
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        if len(arr) == 1:
            return None
        
        i = 0
        def dfs():
            nonlocal i
            if i >= len(arr):
                return None
            if arr[i] == "n":
                i += 1
                return None
            
            node = TreeNode(int(arr[i]))
            i+=1
            node.left = dfs()
            node.right = dfs()

            return node
            
        return dfs()
        

        

