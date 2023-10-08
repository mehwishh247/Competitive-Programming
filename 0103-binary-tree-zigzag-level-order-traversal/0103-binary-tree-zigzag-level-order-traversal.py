# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:return []
        
        queue = deque()
        queue.append((root,0))
        
        answer = []
        
        while queue:
            
            n = len(queue)
            temp = []
            
            lvl =queue[0][-1]
            
            for i in range(n):
                node,level = queue.popleft()
                temp.append(node.val)
                
                if node.left:queue.append((node.left,level+1))
                if node.right:queue.append((node.right,level+1))
            
            if lvl%2==0:     
                answer.append(temp)
            else:
                answer.append(temp[::-1])

        
        return answer

            