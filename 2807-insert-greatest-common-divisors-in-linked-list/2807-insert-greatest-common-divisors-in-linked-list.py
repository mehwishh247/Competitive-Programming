# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pointer = head
        dumm = kk = ListNode(0)
        
        while pointer and pointer.next:
            a,b = pointer.val ,pointer.next.val
            newNode = ListNode(math.gcd(a,b))
            
            dumm.next = ListNode(pointer.val)
            dumm.next.next = newNode
            dumm = dumm.next.next

    
            pointer = pointer.next
        
        if pointer:
            dumm.next = pointer
            

        return kk.next