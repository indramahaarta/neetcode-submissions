"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = defaultdict(Node)
        tail = head
        while tail:
            mp[tail] = Node(tail.val)
            tail = tail.next
        
        tail = head
        while tail:
            copy = mp[tail]
            if tail.next:
                copy.next = mp[tail.next]
            if tail.random:
                copy.random = mp[tail.random]

            tail = tail.next

        return mp[head] if head else None