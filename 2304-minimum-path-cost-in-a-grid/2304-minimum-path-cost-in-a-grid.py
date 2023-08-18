class Solution:
    def minPathCost(self, matrix: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        def rec(i, j, dp):
            # Pruning:
            if i >= m or i < 0 or j < 0 or j >= n:
                return 1e9
            
            # Base case:
            if i == 0:
                return matrix[i][j]
            
            # Cache check
            if dp[i][j] != -1:
                return dp[i][j]
            
            # Computations
            row = i - 1
            ans = 1e8
            
            for col in range(n):
                val = matrix[row][col]
                costForComing = moveCost[val][j]
                ans = min(ans, matrix[i][j] + costForComing + rec(row, col, dp))
            
            # Save and return
            dp[i][j] = ans
            return dp[i][j]
        
        grid = matrix
        cost = moveCost
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        
        # Find the best selection from the last row
        ans = float('inf')
        row = m - 1
        for col in range(n):
            ans = min(ans, rec(row, col, dp))
        
        return ans
