# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        viewed = defaultdict(int)
        viewed[0]=1
        count=0
        
        def solv(node,summ):
            nonlocal count
            if not node:
                return
            summ+=node.val
            count+=viewed[summ-targetSum]
            viewed[summ]+=1
    
            
            solv(node.left,summ)
            solv(node.right,summ)
            
            viewed[summ]-=1


            
        solv(root,0)
        return count
