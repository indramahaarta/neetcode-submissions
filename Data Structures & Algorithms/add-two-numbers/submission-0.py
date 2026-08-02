# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        prev_node, res_head = None, None
        while l1 or l2:
            cur_node = ListNode()
            if l1 and l2:
                cur_sum = carry + l1.val + l2.val
                cur_node.val = (cur_sum) % 10
                carry = cur_sum // 10
            elif l1:
                cur_sum = carry + l1.val
                cur_node.val = (cur_sum) % 10
                carry = cur_sum // 10
            else:
                cur_sum = carry + l2.val
                cur_node.val = (cur_sum) % 10
                carry = cur_sum // 10
            
            if not res_head:
                res_head = cur_node
            
            if prev_node:
                prev_node.next = cur_node

            prev_node = cur_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            # print(prev_node.val, carry)
        
        if carry:
            prev_node.next = ListNode(carry)
        
        return res_head
        