# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
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
        
        
        ans=0
        queue,seen = deque([(start,0)]),set([start])
        
        while queue:
            size = len(queue)
            for i in range(size):
                node,level=queue.popleft()
                for kid in graph[node]:
                    if kid not in seen:
                        seen.add(kid)
                        queue.append((kid,level+1))
            ans=level

                
        return ans