# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_help = ListNode()
        head_help.next = head
        l = 0
        ptr = head_help
        while ptr:
            l += 1
            ptr = ptr.next
        
        """
        [1, 2, 3, 4]
        l = 4
        n = 2
        [1, 2, 4] --> index = 1

        [1, 2, 3]
        l = 3
        n = 2
        [1, 3] --> index = 0

        eq: l - n - 1
        """

        c = 0
        ptr = head_help
        while ptr:
            if l - n - 1 == c:
                removed = ptr.next
                ptr.next = removed.next
                remove = None
            
            ptr = ptr.next
            c += 1
        
        return head_help.next
        