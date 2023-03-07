# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)
    
    
    
    
    
    
    
    
    
        '''
        at every node if it is none return 0 since 
        it is the last element and lets build up from it
        
        other wise
        calculate left count
        calculate right count
        
        return the minm of  the two +1        

        '''
    

    
    
    
    
    
    

                
        