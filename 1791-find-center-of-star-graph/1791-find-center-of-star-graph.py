class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            if len(graph[n1])>1:
                return n1
            if len(graph[n2])>1:
                return n2
       
            
        # for i in graph.keys():
        #     if len(graph[i])>1:
        #         return i
    
