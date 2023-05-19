class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph=defaultdict(list)
        indegree = defaultdict(int)

        for n1,n2 in adjacentPairs:
            graph[n1].append(n2)
            graph[n2].append(n1)

            indegree[n1]+=1
            indegree[n2]+=1

        seen=set()
        ans=[]
        def dfs(node):
            if node not in seen:
                ans.append(node)
            
            seen.add(node)
            for kid in graph[node]:
                if kid not in seen:
                    dfs(kid)






        for key in indegree.keys():
            if indegree[key]==1:
                dfs(key)

                return ans

