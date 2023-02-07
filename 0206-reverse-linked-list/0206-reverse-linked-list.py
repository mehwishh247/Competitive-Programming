# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before=None
        current=head
        
        while current:
# save what commes after
            after = current.next
# change the current pointer to the previeous 
            current.next=before
# update the the before to current to facilitate the next move
            before=current
# jump the pointer to then next(after)
            current=after
            
        return before
        