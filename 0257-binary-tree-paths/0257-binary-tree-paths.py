# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        def solv(node,array):
            if not node:
                return
            array.append(str(node.val))
            if not node.left and not node.right:
                path.append("->".join(array.copy()))
                array.pop()
                return

            solv(node.left,array)
            solv(node.right,array)
            array.pop()





        solv(root,[])

        return path