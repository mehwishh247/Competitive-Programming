# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def solv(nodeX,nodeY):
            if not nodeX and not nodeY:
                return True
            if not nodeX or not nodeY:
                return False
            if nodeX.val!=nodeY.val:
                return False
            right = solv(nodeX.right,nodeY.right)
            left = solv(nodeX.left,nodeY.left)
            
            
            return right and left
        
        return solv(p,q)