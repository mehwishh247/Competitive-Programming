# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        self.summ = 0
        
        def dfs(node,ini):

            if not node:return
            
            if not (node.left or node.right):
                if self.summ+node.val == targetSum:
                    return True
                
            
            self.summ+=node.val
            left  = dfs(node.left,False)
            right = dfs(node.right,False)
            self.summ-=node.val
            
            return left or right

        if not root:
            return False
        return dfs(root,True)
        

        