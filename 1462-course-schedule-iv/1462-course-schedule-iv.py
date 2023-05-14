class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indegree = [0] * n
        adj = {i: set() for i in range(n)}
        prerequisitesMap = {i: set() for i in range(n)}
        
        for pre in prerequisites:
            indegree[pre[1]] += 1
            adj[pre[0]].add(pre[1])
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for next in adj[node]:
                prerequisitesMap[next].add(node)
                prerequisitesMap[next].update(prerequisitesMap[node])
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)
        
        res = []
        for pair in queries:
            if pair[0] in prerequisitesMap[pair[1]]:
                res.append(True)
            else:
                res.append(False)
        
        return res