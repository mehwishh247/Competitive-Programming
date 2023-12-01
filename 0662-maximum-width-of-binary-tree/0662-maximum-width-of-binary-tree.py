# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        queue = deque([(root,0)]) #node and position
        
        
        answer = 0
        
        while queue:
            
            size = len(queue)
            
            most_left,most_right=0,0

            
            for i in range(size):
                
                node,position = queue.popleft()
                
                if i==0:
                    most_left = position
                if i==size-1:
                    most_right = position
                    
                
                if node.left: queue.append((node.left,2*position))
                if node.right: queue.append((node.right,2*position+1))
                    
            answer = max(answer,most_right-most_left+1)
                    
        return answer