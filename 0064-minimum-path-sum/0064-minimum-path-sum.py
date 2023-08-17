class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        m,n = len(grid[0]),len(grid)
        
        for col in range(m-2,-1,-1):
            grid[n-1][col] += grid[n-1][col+1]
        
        for row in range(n-2,-1,-1):
            grid[row][m-1] += grid[row+1][m-1]
        
        
        for row in range(n-2,-1,-1):
            for col in range(m-2,-1,-1):
                grid[row][col]+=min(grid[row+1][col],grid[row][col+1])
        
        return grid[0][0]
             

        
#         def inBound(r,c):
#             return 0<=r<len(grid) and 0<=c<len(grid[0])
                
#         self.summ = grid[0][0]
#         self.min = float("inf")
        
#         def dfs(r,c):
            
    
#             if r==len(grid)-1 and c==len(grid[0])-1:
#                 self.min = min(self.min,self.summ)
                
#             directions = [(r+1,c),(r,c+1)]
            
#             for dr in directions:
                
#                 row,col = dr
#                 if inBound(row,col):
                    
#                     self.summ += grid[row][col]
#                     dfs(row,col)
#                     self.summ -= grid[row][col]
                
      
#         dfs(0,0)
        
        
#         return self.min
                    
        