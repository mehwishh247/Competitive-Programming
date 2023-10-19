class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
    
        
        n,m = len(matrix),len(matrix[0])
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                
                
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    ans = max(dp[i + 1][j + 1], ans)
      
        return ans ** 2
                
                
        
        