class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowN=head
        fastN=head
        
        while fastN and fastN.next:
            slowN=slowN.next
            fastN=fastN.next.next
            

        return slowN
        
        
        
#         length=0
#         original=head
#         while head:
#             length+=1
#             head=head.next
        
#         current=ListNode(0)
#         result=current
#         c=0
#         while original:
#             if c>=length//2:
#                 current.next=ListNode(original.val)
#                 current=current.next
#             original=original.next
#             c+=1
#         return result.next
            
        