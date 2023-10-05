# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        
        answer = []
        
        while queue:
            
            n = len(queue)
            temp_ans = float('-inf')
            
            for i in range(n):

                node = queue.popleft()
                temp_ans = max(temp_ans,node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
            answer.append(temp_ans)
                
        return answer
        