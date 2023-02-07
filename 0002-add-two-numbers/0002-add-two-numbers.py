class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summ=ListNode(0)
        total=summ
        carry=0
        while l1 or l2:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
#             artimetcis
            tot=val1+val2+carry
            carry=tot//10
            summ.next=ListNode(tot%10)
#             shift pointers
            summ=summ.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if carry:
            summ.next=ListNode(carry)
        return total.next
            
        