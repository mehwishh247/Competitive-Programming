def isCycle(self, V: int, graph: List[List[int]]) -> bool:
	 

        colors=[0 for i in range(len(graph))]

        
        def dfs(node, parent):

            if colors[node]==1:
                return True
            
            colors[node]=1
            
            for child in graph[node]:
                if colors[child]==2 or child == parent:
                    continue
                if dfs(child, node):
                    return True
            colors[node]=2

            return False
        cycle = False
        for i in range(len(graph)):
            if colors[i]==0:
                cycle = cycle or dfs(i, -1)
                
        return cycle
