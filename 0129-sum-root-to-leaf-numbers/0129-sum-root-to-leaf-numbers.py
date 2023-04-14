# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        paths=[]
        def traversal(node,temp):
            if not node:
                return
            temp.append(str(node.val))

            if not node.left and not node.right:
                   paths.append("".join(temp))
                

            traversal(node.left,temp)
            traversal(node.right,temp)
            temp.pop()


        traversal(root,[])
        result = sum(map(int,paths))
        
    

        return result
        