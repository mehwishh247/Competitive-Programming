class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        temp=[]
        end = len(graph)-1
        def can_reach(start):
            if start==end:
                temp.append(end)
                ans.append(temp.copy())
                return
            temp.append(start)
            for neighbour in graph[start]:
                can_reach(neighbour)
                temp.pop()
            return 
        
        can_reach(0)
        
        return ans
        