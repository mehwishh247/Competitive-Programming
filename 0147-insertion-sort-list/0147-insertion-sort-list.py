# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        dummy=head
        while dummy:
            arr.append(dummy.val)
            dummy=dummy.next
        
        arr.sort()
        ans=ListNode(arr[0])
        
        current = ans
        for i in range(1,len(arr)):
            nextNode = ListNode(arr[i])
            current.next=nextNode
            current=nextNode

        return ans

