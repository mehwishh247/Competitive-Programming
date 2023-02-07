class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        original=head
        while head:
            length+=1
            head=head.next
        half=length//2
        
        current=ListNode(0)
        result=current
        c=0
        while original:
            if c>=half:
                current.next=ListNode(original.val)
                current=current.next
            original=original.next
            c+=1
        return result.next
            
        