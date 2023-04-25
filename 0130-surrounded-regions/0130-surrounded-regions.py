class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rowL= len(board)
        colL=len(board[0])
        changed = set()
        # visited=set()

        def isOnBorder(row,col):
            return (row==0 or row==rowL-1 or col==0 or col==colL-1)
        def isInBound(row,col):
            return (0<=row<rowL and 0<=col<colL)

        def dfs(row,col):
            # visited.add((row,col))

            directions=[(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
            for dr in directions:
                if isInBound(dr[0],dr[-1]) and board[dr[0]][dr[-1]]=="O" and dr not in changed: 
                    changed.add(dr)
                    dfs(dr[0],dr[-1])
            return 





        for row in range(rowL):
            for col in range(colL):
                if isOnBorder(row,col) and board[row][col]=="O":
                    dfs(row,col) 
                    
        for row in range(rowL):
            for col in range(colL):
                if (row,col) not in changed and not isOnBorder(row,col):
                    board[row][col]="X"