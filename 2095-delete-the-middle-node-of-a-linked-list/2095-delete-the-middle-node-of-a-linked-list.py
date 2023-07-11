# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return None
        
        prev = slow = fast = head
        fg = 0
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            
            if fg>=1:
                prev = prev.next
            fg=2

                
        if prev.next.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        # print(prev)
#         print(slow)
        
#         print(fast)
            
        return head