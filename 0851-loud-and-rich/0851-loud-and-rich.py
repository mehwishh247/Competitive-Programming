class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph=defaultdict(list)
        answer=defaultdict(int)

        for n1,n2 in richer:
            graph[n2].append(n1)
            
        n=len(quiet)    
            
        def dfs(node):
            if answer[node]:
                return answer[node]
            answer[node] = node
            for kid in graph[node]:
                if quiet[dfs(kid)] < quiet[answer[node]]:
                    answer[node] = answer[kid]
            return answer[node]
        
        for i in range(n):
            dfs(i)
            
        result = [0] * n
        for i in range(n):
            result[i] = dfs(i)
            
        return result