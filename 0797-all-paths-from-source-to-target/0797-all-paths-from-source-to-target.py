class Solution:
    def allPathsSourceTarget(self, graphM: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for i in range(len(graphM)):
            graph[i]=graphM[i]
        ans = []
        temp=[]
        end = len(graphM)-1
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
        