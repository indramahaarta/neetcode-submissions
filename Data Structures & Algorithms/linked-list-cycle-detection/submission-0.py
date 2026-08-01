# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0

        while head:
            if head.val > 1000:
                return True
            else:
                head.val = 1001
                head = head.next
        
        return False
        
        