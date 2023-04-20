# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        arr=[]
        
        def traversal(node):
            nonlocal arr
            
            if not node:
                return
            
            if node.left and node.val%2==0:
                if node.left.left:
                    arr.append(node.left.left.val)
                if node.left.right:
                    arr.append(node.left.right.val)
            if node.right and node.val%2==0:
                if node.right.left:
                    arr.append(node.right.left.val)
                if node.right.right:
                    arr.append(node.right.right.val)
                
            
            left = traversal(node.left)
            right = traversal(node.right) 
            
            return 
            
            
        
        traversal(root)
        
        
        return sum(arr)