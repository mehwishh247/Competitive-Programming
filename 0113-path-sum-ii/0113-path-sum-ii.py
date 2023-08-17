# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        answers = []
        temp = []
        self.summ = 0
        
        def dfs(node):
            
            if not node:return
            
            if not(node.left or node.right):
                if self.summ + node.val == targetSum:
                    pos = temp.copy()
                    pos.append(node.val)
                    answers.append(pos)
                    return True
            
            self.summ+=node.val
            temp.append(node.val)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.summ-=node.val
            temp.pop()
            
            return left or right
        
        if not root:return []
        
        dfs(root)
        return answers
            
            
            
            
        