# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = defaultdict(int)
        def modeCal(node):
            if not node:
                return 
            cnt[node.val]+=1
    
            modeCal(node.left)
            modeCal(node.right)
            
            # cnt[node.val]-=1
        
        modeCal(root)
        max_val = max(cnt.values())
        
        res = []
        
        for key in cnt:
            if cnt[key]==max_val:
                res.append(key)
        return res

            
            
        