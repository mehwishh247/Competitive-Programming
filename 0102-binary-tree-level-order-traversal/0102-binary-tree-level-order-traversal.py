# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
#         BFS
        if not root: return []
        queue=deque([root])
        ans=[]
        
        while queue:
            size = len(queue)
            temp=[]
            for i in range(size):
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
        return ans
                
        
        

        
#         #######DFS
#         view = defaultdict(list)

#         def solv(node,level):
#             if not node:
#                 return
            
#             view[level].append(node.val)
#             level+=1
#             solv(node.left,level)
#             solv(node.right,level)

#         solv(root,0)
        
#         res = []
        
#         for i in view.keys():
#             res.append(view[i])
#         return res

