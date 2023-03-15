# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = head
        def solve(node):
            if not node or not node.next:
                return node
            
            node2 = node.next
            tail = node2.next
            node2.next = node
            node.next = solve(tail)
            return node2
        
        return solve(head)

            
            
            
      
        