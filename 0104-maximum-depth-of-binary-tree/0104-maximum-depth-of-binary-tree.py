# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def sol(node):
            if node == None:
                return 0
            leftCount = sol(node.left)
            rightCount = sol(node.right)
        
            return max(leftCount,rightCount)+1
        
        return sol(root)
    