# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        if both sides of the nodes exist and there value is equal return True 
        then check 
        else  return false 
        
        [2,3,3,4,5,5]
        
        '''
        def solv(nodeX,nodeY):
            if not nodeX and not nodeY:
                return True
            if nodeX and not nodeY:
                return False
            if not nodeX and nodeY:
                return False
            
            if nodeX.val!= nodeY.val:
                return False
            
            right = solv(nodeX.right,nodeY.left)
            left  = solv(nodeX.left,nodeY.right)
            
            return right and left
            
            
        if not root:
            return True
        return solv(root.left,root.right)
        
        