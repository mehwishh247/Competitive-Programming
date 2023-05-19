class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        graph=defaultdict(list)
        incoming=defaultdict(int)

        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
            incoming[n1]+=1
            incoming[n2]+=1

        queue=deque()
        
        for key in incoming.keys():
            if incoming[key]==1:
                queue.append(key)
        

        remaining = n
        
        while remaining>2:
            size=len(queue)
            remaining-=size
            
            for i in range(size):
                node=queue.popleft()
                incoming[node]-=1


                for child in graph[node]:   
                    incoming[child]-=1

                    if incoming[child]==1:
                        queue.append(child)


        return queue