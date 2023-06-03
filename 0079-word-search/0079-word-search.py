class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def isValid(dr):return 0<=dr[0]<len(board) and 0<=dr[-1]<len(board[0])
        
        
        visited = set()
        
        
        def dfs(row,col,idx):
            # print(row,col,idx)
            
            if idx==len(word)-1:
                return True
    
            
            directions = [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
            


            for dr in directions:
                
                
                if isValid(dr) and dr not in visited and board[dr[0]][dr[-1]]==word[idx+1]:
                    
                    visited.add(dr)
                    
                    if dfs(dr[0],dr[-1],idx+1):
                        return True
                    visited.discard(dr)

            return False
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                if board[row][col]==word[0]:
                    # print(row,col)
                    visited.add((row,col))
                    if dfs(row,col,0):
                        return True
                visited=set()
        # return dfs(0,0,0)
        return False
                    
