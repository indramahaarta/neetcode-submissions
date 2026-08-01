# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l, h = head, head.next if head else None

        while h:
            l = l.next
            h = h.next
            if l == h:
                return True
            
            h = h.next if h else None
            if l == h:
                return True
        
        return False

        
        