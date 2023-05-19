class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        
        rep = {i:i for i in range(n)}
        rank = [1] * n
        
        def find(node):
            parent = node
            while parent != rep[parent]:
                parent = rep[parent]
                
            while node != rep[node]:
                temp = rep[node]
                rep[node] = parent
                node = temp
            
            return parent
    
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            
            
            if rank[xRep] >= rank[yRep]:
                rep[yRep] = xRep
                rank[xRep] += rank[yRep]
            
            else:
                rep[xRep] = yRep
                rank[yRep] += rank[xRep]
        
        arr=[]
        heapify(arr)
        
        for i in range(n):
            for j in range(i+1,n):
                xo,yo = points[i]
                x1,y1 = points[j]
                
                cost = abs(xo-x1)+abs(yo-y1)
                heappush(arr,(cost,(i,j)))
        
        solution=[]
        total=0
        

        while len(solution)<n-1:
            
            cost,edge = heappop(arr)
            
            node1,node2 = edge
            
            if find(node1)!=find(node2):
                union(node1,node2)
                solution.append(edge)
                total+=cost

        return total
            
            
        
        
        
        