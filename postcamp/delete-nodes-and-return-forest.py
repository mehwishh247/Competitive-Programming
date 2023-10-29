# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    
        if not to_delete: return [root]
        if not root: return []
        
        look = set(to_delete)
        
        answer = []
        
        def dfs(node,parent):
            
            
            if not node: return
            
            if node.val in look: 
                
                node.left = dfs(node.left, False)
                node.right = dfs(node.right, False)
                
                return

            if not parent:     
                answer.append(node)

            node.left = dfs(node.left,True)
            node.right = dfs(node.right,True)

            return node
                
        
        dfs(root,False)        
                    
        return answer
                

        
        