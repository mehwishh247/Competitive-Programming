class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        incoming=defaultdict(int)
        
        for main,preq in prerequisites:
            graph[preq].append(main)
            incoming[main]+=1
        
        
        ans=[]
        queue=deque()
        
#         find source node
        for course in range(numCourses):
            if incoming[course]==0:
                queue.append(course)
        
        while queue:
            node=queue.popleft()
            ans.append(node)
            
            for child in graph[node]:
                incoming[child]-=1
                
                if incoming[child]==0:
                    queue.append(child)
        
        if len(ans)!=numCourses:
            return False
        return True