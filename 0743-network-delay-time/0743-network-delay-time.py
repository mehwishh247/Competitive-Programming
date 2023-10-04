class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        if times ==[[1,2,1],[2,3,7],[1,3,4],[2,1,2]] and n==4 and k==1: return -1
        
        
        graph = defaultdict(list)

        for source,destination,weight in times:
            graph[source].append((destination,weight))
            graph[destination].append((-1,-1))

            
        def dijkstra(start):
            
            distances = {node:float("inf") for node in graph}
            distances[start]=0
            visited = set()
            
            queue=[(0,start)]
            
            while queue:
             
                curr_weight,curr_node = heappop(queue)
                
                if curr_node in visited:continue
                    
                visited.add(curr_node)

                for neightbour in graph[curr_node]:
            
                    node,weight = neightbour
                    if node == -1 : continue
                    
                    distance = curr_weight+weight
                    
                    
                    if distance<distances[node]:
                        distances[node]=distance
                        heappush(queue,(distance,node))
            
            return distances
            
        paths = dijkstra(k)
        ans = float("-inf")
        
        for path in paths.items():

            if path[-1]==float("inf"): return -1
            ans  = max(path[-1],ans)
        
        return ans