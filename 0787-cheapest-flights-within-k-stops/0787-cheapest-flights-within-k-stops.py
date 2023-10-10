class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        seen = set()
        
        for st,ds,cost in flights:
            graph[st].append((ds,cost))
        
        
        def dijkstra(graph,src):
            
            costs = {node:float('inf') for node in range(n)}
            costs[src] = 0
            
            queue = [(0,0,src)]
            
            while queue:
                
                stops,cost,node = heappop(queue)
                
#                 if node in seen:continue
#                 seen.add(node)
                
                for dest,price in graph[node]:
                    
                    total = cost + price
                    
                    if stops <= k and total < costs[dest] :
                            costs[dest] = total
                            heappush(queue,(stops+1,total,dest))
                    
            return costs
        
        x = dijkstra(graph,src)
        
        return x[dst] if x[dst] != float('inf') else -1
                    
            
        