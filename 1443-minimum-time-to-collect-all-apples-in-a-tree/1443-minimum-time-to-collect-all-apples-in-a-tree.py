class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph=defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)


        visited=set([0])

        def dfs(node):
            ans=0
            for kid in graph[node]:
                if kid not in visited:
                    visited.add(kid)
                    time = dfs(kid)
                    ans+=time
            
            if node!=0 and (hasApple[node] or ans):
                ans+=2
            return ans
        
        return dfs(0)
