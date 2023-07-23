# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)
        def dfs(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        ans=[]
        queue,seen = deque([(target.val,0)]),set([target.val])
        
        while queue:
            node,level=queue.popleft()
    
            if level==k:
                ans.append(node)
            
            for kid in graph[node]:
                if kid not in seen:
                    seen.add(kid)
                    queue.append((kid,level+1))
                
        return ans
        