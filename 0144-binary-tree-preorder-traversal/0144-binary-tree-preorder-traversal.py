# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def sol(node,array):
            if node==None:
                return array
            array.append(node.val)
            leftArr=sol(node.left,array)
            rightArr=sol(node.right,array)
          

       
            
            return leftArr
        return sol(root,[])