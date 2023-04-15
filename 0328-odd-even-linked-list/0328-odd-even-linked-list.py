# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        slow,fast=head,head.next
        evenhead = head.next
        
        while fast and fast.next:
            slow.next = slow.next.next
            slow = slow.next  
            fast.next = fast.next.next
            fast = fast.next
        
        slow.next=evenhead
        return head