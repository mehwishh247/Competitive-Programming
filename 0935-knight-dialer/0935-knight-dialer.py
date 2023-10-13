class Solution:
    def knightDialer(self, n: int) -> int:
        
        graph = {0 : [4,6], 1: [8,6],2: [7,9],3: [4,8],4: [0,3,9],5:[],6: [0,1,7],7: [2,6,],8: [1,3,],9: [4,2,],}
        
        @cache
        def dfs(level,node):
            
            if level==n-1:
                return 1
            
            sub_ans = 0
            
            for nxt in graph[node]:
                
                sub_ans+=dfs(level+1,nxt)
                
            return sub_ans
        
        answer = 0
        for i in range(10):
            answer += dfs(0,i)
            
        return answer %(10**9 + 7)