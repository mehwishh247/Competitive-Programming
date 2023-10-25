# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer = []
        
        if not root: return []
        
        queue = deque([root])
        
        while queue:
            
            n = len(queue)
            temp = []
            
            for i in range(n):
                
                node = queue.popleft()
                
                temp.append(node.val)
                
                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right)
            
            answer.append(temp)
            
            
        return answer[::-1]