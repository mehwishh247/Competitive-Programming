# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        see = defaultdict(list)
        
        def dfs(node):
            
            if not node: return "N"
            
            res = "-".join([str(node.val),dfs(node.left),dfs(node.right)])
            
            if len(see[res]) == 1 : result.append(node)
                
            see[res].append(node)

            return res
           
        result = []
        dfs(root)
    
        
        return result