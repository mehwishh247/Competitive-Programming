# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node,checkP):
            if not node: return True
            
            if not (checkP[0]<node.val<checkP[-1]):
                return False
            
            left  = validate(node.left,(checkP[0],node.val))
            right  = validate(node.right,(node.val,checkP[-1]))

            return left and right

            
        return validate(root,(float("-inf"),float("inf")))