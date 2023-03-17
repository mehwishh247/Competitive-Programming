# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        def solv(nodeX,nodeY):
            if not nodeX and not nodeY:
                return True
            if not nodeX or not nodeY:
                return False
            if nodeX.val!=nodeY.val:
                return False
            right = solv(nodeX.right,nodeY.right) or solv(nodeX.right,nodeY.left) 
            left = solv(nodeX.left,nodeY.left) or solv(nodeX.left,nodeY.right)


            return right and left

        return solv(root1,root2)