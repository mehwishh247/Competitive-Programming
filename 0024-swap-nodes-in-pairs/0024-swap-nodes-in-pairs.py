# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = dummy = ListNode(0,head)

        while left.next and left.next.next:
            second = left.next
            third = second.next

            second.next = third.next
            third.next = second

            left.next = third
            left = second

        return dummy.next














        
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = head
#         def solve(prev, node):
#             if not node or not node.next:
#                 return node
            
#             node2 = node.next
#             tail = node2.next
#             node2.next = node
#             node.next = solve(node, tail)
            
#             if prev == head:
#                 return node2
#             else:
#                 prev.next = node2
#                 return node2
            
#         return solve(prev, head)

    
    
    

#         def solve(node):
#             if not node or not node.next:
#                 return node
            
#             node2 = node.next
#             tail = node2.next
#             node2.next = node
#             node.next = solve(tail)
    
#             return node2
        
#         return solve(head)
            
            
            
      
        