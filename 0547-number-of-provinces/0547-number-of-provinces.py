class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)    
    
        for i in range(len(isConnected)):
            for j in range(1,len(isConnected[0])):
                if isConnected[i][j]==1 and i!=j:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)


        totalVisit = set()
        count=0

        def dfs(node):
            totalVisit.add(node)        
            for neighbour in graph[node]:
                if neighbour not in totalVisit:
                    dfs(neighbour)


        for node in range(1,len(isConnected)+1):
            if node not in totalVisit:
                count+=1
                dfs(node)
        return count