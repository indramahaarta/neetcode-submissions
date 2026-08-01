# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
        2 --> 4 --> [6] --> 8 --> None
        2 --> 8 --> 4 --> 6 --> None

        2 --> 4 --> [6] --> 8 --> 10 --> None
        2 --> 10 --> 4 --> 8 --> 6 --> None

        node --> None is len(tree) // 2 + 1
        """

        t = head
        i = 0
        # Getting the length of list
        while t:
            t = t.next
            i += 1
        
        # print(i)

        # Getting the second node
        second_node, p = None, 0
        t = head
        prev = None
        while t:
            tnext = t.next
            # if p + 1 == i//2:
            #     t.next = None
            prev = t
            t = tnext
            p += 1
            if p == (i+1)//2:
                second_node = t
                # print("second_node ", second_node.val)
                break
        # print("prev.val", prev.val)
        prev.next = None

        # print(second_node.val)
        
        # Reverse second node
        a, b = None, second_node
        while b:
            bnext = b.next
            b.next = a
            a = b
            b = bnext
        
        # print(a.val, a.next.val)
        # h = head
        # while h:
        #     print(h.val)
        #     h = h.next
        
        # print("---------")
        
        # while a:
        #     print(a.val)
        #     a = a.next
        
        # print("---------")
        
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

        