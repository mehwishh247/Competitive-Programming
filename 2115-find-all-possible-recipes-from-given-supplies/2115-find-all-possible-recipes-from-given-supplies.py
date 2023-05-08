class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph=defaultdict(list)
        incoming=defaultdict(int)
        
        for index,ingridientList in enumerate(ingredients):
            for single in ingridientList:
                graph[single].append(recipes[index])
                incoming[recipes[index]]+=1  
        

        order=[]
        queue=deque()
        
        for supply in supplies:
            if graph[supply]:
                queue.append(supply)
                
        while queue:
            node= queue.popleft()
            if node in recipes:
                order.append(node)
            
            for child in graph[node]:
                incoming[child]-=1
                
                if incoming[child]==0:
                    queue.append(child)
                    
                
        return order
                
        