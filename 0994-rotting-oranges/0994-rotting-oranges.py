class Solution:
    
    def isValid(self,dr,board):
        return (0<=dr[0]<len(board)) and (0<=dr[1]<len(board[0])) and (board[dr[0]][dr[1]]==1)
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        
        # find all rottens and add them to the que 
        
        rowL = len(grid)
        colL = len(grid[0])
        
        for row in range(rowL):
            for col in range(colL):
                if grid[row][col]==2:
                    queue.append((row,col,0))

        level=0

        while queue:
            nodeData = queue.popleft()
            rrow = nodeData[0]
            ccol = nodeData[1]
            level = nodeData[2]
            
            directions = [(rrow+1,ccol),(rrow-1,ccol),(rrow,ccol+1),(rrow,ccol-1)]
            for dr in directions:
                if self.isValid(dr,grid):
                    grid[dr[0]][dr[1]]=2
                    queue.append((dr[0],dr[1],level+1))
                    
        for row in range(rowL):
            for col in range(colL):
                if grid[row][col]==1:
                    return -1
        
        

        return level