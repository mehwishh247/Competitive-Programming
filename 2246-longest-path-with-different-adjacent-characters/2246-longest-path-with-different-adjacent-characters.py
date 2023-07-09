class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        if len(parent)<=1:
            return 1
        graph = defaultdict(list)

        for i,num in enumerate(parent):
            graph[num].append(i)
            
        longestPath = 0
        
        def dfs(node):
            nonlocal longestPath
            
            longestLength = 0
            longestLength2 = 0

            for kid in graph[node]:
                lengthChild = dfs(kid)
                if (s[node] == s[kid]): continue
                if (longestLength < lengthChild):
                    longestLength2 = longestLength
                    longestLength = lengthChild

                elif (longestLength2 < lengthChild):
                    longestLength2 = lengthChild
    
            longestPath = max(longestPath, longestLength + longestLength2 + 1)
            return longestLength + 1
               
            
        dfs(0)
        
        return longestPath