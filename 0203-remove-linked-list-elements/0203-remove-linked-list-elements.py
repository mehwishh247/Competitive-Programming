# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = head
        main = copi = ListNode(0)
        
        while dummy:
            
            if dummy.val!=val:
                copi.next = ListNode(dummy.val)
                copi = copi.next
                
            dummy = dummy.next
            
            
        
        return main.next
            
            
            
            
        