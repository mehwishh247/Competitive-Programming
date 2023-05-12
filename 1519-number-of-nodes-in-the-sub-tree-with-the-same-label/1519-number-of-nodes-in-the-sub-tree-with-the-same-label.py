class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
    
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        arr = [0]*n
        visited=set()
        
        
        def dfs(node):
            
            if node in visited:
                return defaultdict()
            
            visited.add(node)
            
            dicit = defaultdict(int)
            dicit[labels[node]]+=1


            for kid in graph[node]:

                res=dfs(kid)
                for i in res.keys():
                    dicit[i]+=res[i]

            arr[node]+=dicit[labels[node]]

            return dicit


        x = dfs(0)
        return arr




        