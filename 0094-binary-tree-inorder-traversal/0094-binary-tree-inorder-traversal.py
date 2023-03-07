# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def sol(node,array):
            if node==None:
                return array
            left = sol(node.left,array)
            left.append(node.val)
            right=sol(node.right,left)

            return right
        return sol(root,[])
                
        