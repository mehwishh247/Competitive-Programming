# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        visited=set()
        dummy = head
        
        while dummy:
            if dummy in visited:
                return dummy
            visited.add(dummy)
            dummy=dummy.next

        return None
                
 