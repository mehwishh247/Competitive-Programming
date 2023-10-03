# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        self.answer = 0
        def dfs(node,side):
            
            if not node: return 
            
            if side=="left" and not (node.left or node.right):
                self.answer+=node.val
                return
            
            
            dfs(node.left,"left")
            dfs(node.right,"right")      
            
        dfs(root,"")
        
        return self.answer