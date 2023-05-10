class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        adjList=defaultdict(list)
        
        for i in range(len(graph)):
            for ele in graph[i]:
                adjList[ele].append(i)
    
    
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
        ans = sorted(ans)
        return ans 
            
            
            