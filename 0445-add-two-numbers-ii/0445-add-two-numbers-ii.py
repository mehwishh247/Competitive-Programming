# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numit(self,root):
        dummy = root
        num = ''
        
        while dummy:
            num+= str(dummy.val)
            dummy = dummy.next
            
        return int(num)
            
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        root = head = ListNode(0)
        
        x = self.numit(l1)
        y = self.numit(l2)
        
        answer = x+y
        
        for num in str(answer):
            head.next = ListNode(num)
            head = head.next
            
        return root.next