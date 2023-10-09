class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        seen = set()
        
        for i,edge in enumerate(edges):
            s,d = edge
            graph[s].append((d,succProb[i]))
            graph[d].append((s,succProb[i]))
        

        props = {i:0 for i in range(n)}
        props[start_node] = 1
        
        queue = [(-1,start_node)]
        
        while queue:
            
            chance,node = heappop(queue)
            chance*=-1
            
            if node in seen:continue
            seen.add(node)
            
            for neighbor,cost in graph[node]:
                
                prop = cost*chance
                
                if prop> props[neighbor]:
                    props[neighbor] = prop
                    heappush(queue, (-prop, neighbor))
                
        return props[end_node]
            