class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        temp = 0
        def isValid(dr):
            return (0<=dr[0] < len(grid)) and (0<=dr[-1] < len(grid[0])) and  (grid[dr[0]][dr[-1]]!=0 and grid[dr[0]][dr[-1]]!=2)

        def dfs(r,c):
            nonlocal temp
            directions=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            if grid[r][c]==1:               
                temp+=1
            grid[r][c] = 2


            for dr in directions:
                if isValid(dr):
                    dfs(dr[0],dr[-1])
            return
        maxxArea = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if isValid((row,col)):
                    dfs(row,col)
                    maxxArea = max(maxxArea,temp)
                    temp=0
        return maxxArea
