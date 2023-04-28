class Solution:
    def isValid(self,dr,board):
        return (0<=dr[0]<len(board)) and (0<=dr[1]<len(board[0])) and (board[dr[0]][dr[1]]==0)
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        queue = deque([(0,0,1)])
        
        if grid[0][0]==1:
            return -1

        
        while queue:
            
            rrow, ccol, level = queue.popleft()
        
            if rrow==len(grid)-1 and ccol==len(grid[0])-1:
                return level
            
            directions = [(rrow+1,ccol),(rrow-1,ccol),(rrow,ccol+1),(rrow,ccol-1),(rrow+1,ccol+1),(rrow-1,ccol-1),(rrow-1,ccol+1),(rrow+1,ccol-1) ]
            
            for dr in directions:
                if self.isValid(dr,grid):
                    grid[dr[0]][dr[1]]=1
                    queue.append((dr[0],dr[1],level+1))
                    

        return -1
        
        
        
        
        