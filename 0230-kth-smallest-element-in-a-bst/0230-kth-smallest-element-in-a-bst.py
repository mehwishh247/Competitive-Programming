# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 1
        self.flag = True
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       
        def sol(node,array):
            if node==None:
                if len(array)==k and self.flag:
                    print(array)
                    self.ans=array[-1]
                    self.flag = False
                return array
        
            left = sol(node.left,array)
            left.append(node.val)
            right=sol(node.right,left)

            return right
        sol(root,[])

        return self.ans