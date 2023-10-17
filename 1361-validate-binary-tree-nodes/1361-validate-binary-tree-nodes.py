class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        graph = defaultdict(list)
        income = defaultdict(int)
        

        for i in range(n):
            
            left,right = leftChild[i],rightChild[i]
            
            if left != -1:
                graph[i].append(left)
                income[left] += 1
            
            if right != -1:
                graph[i].append(right)
                income[right] += 1
        

        let = 0
        queue = deque()
        
        for j in range(n):
            
            if income[j]==0:
                queue.append(j)
            
            if income[j]>= 2: return False
            
        
        if len(queue)!=1: return False
        
        while queue:
            
            node = queue.popleft()
            let+=1
            
            for child in graph[node]:
                income[child]-=1
                
                if income[child]==0:
                    queue.append(child)
                    
        if let != n: return False
        
        return True