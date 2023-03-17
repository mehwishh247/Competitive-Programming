# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        sub_sum = defaultdict(int)
        
        def solv(node):
            nonlocal sub_sum
            if not node:
                return 0
            
            left = solv(node.left)
            right = solv(node.right)
            
            summ=right+left+node.val
            sub_sum[summ]+=1
            
            return summ
            
        solv(root)
                
        maxFrq =max(sub_sum.values())        
        
        result = []
        
        for key in sub_sum.keys():
            if sub_sum[key]==maxFrq:
                result.append(key)
        
        
        return result
            
            
        