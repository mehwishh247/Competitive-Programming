class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        colors=[0 for i in range(len(graph))]
        ans=set()
        
        
        def dfs(node):

            if colors[node]==1:
                return False
            
            colors[node]=1
            
            for child in graph[node]:
                if colors[child]==2:
                    continue
                if not dfs(child):
                    return False
            colors[node]=2
            ans.add(node)
            return True
        
        for i in range(len(graph)):
            if colors[i]==0:
                dfs(i)
                
        ans=list(ans)
        ans.sort()
        return ans 
            
            
            