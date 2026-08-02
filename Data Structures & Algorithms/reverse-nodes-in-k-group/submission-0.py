# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevGroup = dummy

        while True:
            kthNode = self.getKth(prevGroup, k)
            if not kthNode:
                break
            
            prev, cur = kthNode.next, prevGroup.next
            i = 0

            """
            dummy --> 1 --> 2 --> 3 --> 4 --> 5, k = 2

            # iterration 1
            prevGroup = dummy
            kthNode = 2
            prev = 3
            cur = 1
            --------
            prev = 2
            cur = 3
            dummy --> 2 --> 1 --> 3
            """
            while i < k:
                curNext = cur.next
                cur.next = prev
                prev = cur
                cur = curNext

                i += 1

            prevGroupNext = prevGroup.next
            prevGroup.next = prev 
            prevGroup = prevGroupNext
        
        return dummy.next


    
    def getKth(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1
        
        return node



        