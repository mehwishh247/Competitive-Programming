class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid[0]),len(grid)
        currMax = float("-inf")

        for row in range(n-2):
            for col in range(m-2):
                
                top = grid[row][col] + grid[row][col+1]+grid[row][col+2]
                btm = grid[row+2][col] + grid[row+2][col+1]+grid[row+2][col+2]
                currMax = max(currMax,top+btm+grid[row+1][col+1])
        
        return currMax