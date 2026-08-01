# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, i = None, None

        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    head, i = list1, list1
                    list1 = list1.next
                    continue
                
                i.next = list1
                i = list1
                list1 = list1.next
            else:
                if not head:
                    head, i = list2, list2
                    list2 = list2.next
                    continue
                
                i.next = list2
                i = list2
                list2 = list2.next
        
        if list1:
            if not head:
                return list1
            
            i.next = list1
        elif list2:
            if not head:
                return list2
            
            i.next = list2
        
        return head

                
        
        