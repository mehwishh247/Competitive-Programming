# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = head
        leng = 0
        while dummy:
            leng+=1
            dummy = dummy.next
        
        if leng==n:
            return head.next
        
        i=1
        main = head
        while i<leng-n:
            i+=1
            main=main.next
            
        main.next=main.next.next

            
        return head
    
        