class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
        ans = [[1]*n]*m
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                ans[i][j] = ans[i+1][j]+ans[i][j+1]
            
        return ans[0][0]