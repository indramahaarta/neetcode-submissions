# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, n = None, head

        while n:
            nxt = n.next
            n.next = p
            p = n
            n = nxt
        
        return p
            



        