"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for n in node.neighbors:
                if n not in oldToNew:
                    copy.neighbors.append(clone(n))
                else:
                    copy.neighbors.append(oldToNew[n])

            return copy
        
        return clone(node)


        