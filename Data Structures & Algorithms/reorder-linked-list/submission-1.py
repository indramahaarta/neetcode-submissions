# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        # [1, 2, 3, 4]

        while f:
            f = f.next
            if f:
                f = f.next
            else:
                break
            s = s.next
        
        # print(s.val)
        
        a, b = None, s.next
        while b:
            bnext = b.next
            b.next = a
            a = b
            b = bnext
        s.next = None
        
        h = head
        while h and a:
            # print(h.val, a.val)
            hnext = h.next
            anext = a.next
            h.next = a
            a.next = hnext
            h = hnext
            a = anext
            # print(h, a)

        