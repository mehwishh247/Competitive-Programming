# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.MAXX =float("-inf") 
        def solv(node):
            if not node: return 0
            
            left = solv(node.left)+node.val
            right = solv(node.right)+node.val
            
            self.MAXX = max(left,right,node.val,left+right-node.val,self.MAXX) 
            return max(left,right,node.val)
        solv(root)
        return self.MAXX