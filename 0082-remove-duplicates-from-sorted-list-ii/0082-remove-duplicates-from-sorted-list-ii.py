class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_vals = set()
        self.main = defaultdict(int)
        dummy = head
        while dummy:
            self.main[dummy.val]+=1
            dummy=dummy.next
        
        
        return self.remove_duplicates(head)
    
    def remove_duplicates(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node:
            return None
        if self.main[node.val]==1:
            node.next = self.remove_duplicates(node.next)
        else:
            return self.remove_duplicates(node.next)

        return node
