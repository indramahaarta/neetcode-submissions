# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        while True:
            minimun_node, index = None, -1
            for i, node in enumerate(lists):
                if not node:
                    continue
                
                if not minimun_node or node.val < minimun_node.val:
                    minimun_node = node
                    index = i

            if not minimun_node:
                break
            
            # Update the head of the specific list in the lists array BEFORE modifying the node's next pointer
            lists[index] = minimun_node.next
            
            temp = minimun_node
            tail.next = temp
            tail = temp
            tail.next = None

        
        return head.next
            
            


                

        