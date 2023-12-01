# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
    
            oddP = 1 -> 3 -> 5
                             i
            evenP = 2 -> 4
                         j
                         
            evenHead = head.next //2 -> 4
            
            oddP.next = evenHead
            head
    
        '''
        
        if not head: return 
            
        odd_pointer,even_pointer = head,head.next
        evenHead = head.next
        
        while even_pointer and even_pointer.next:
            
            odd_pointer.next = odd_pointer.next.next
            even_pointer.next = even_pointer.next.next
            
            odd_pointer = odd_pointer.next
            even_pointer = even_pointer.next
        
        
        odd_pointer.next = evenHead
        
        return head
            
        