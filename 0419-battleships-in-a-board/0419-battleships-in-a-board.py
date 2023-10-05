class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        n,m = len(board),len(board[0])
        answer = 0
        
        
        for row in range(n):
            for col in range(m):
                
                if board[row][col]=="X":
                    board[row][col]="."
                    
                    #check row
                    i = col+1 
                    while i < m and board[row][i]=="X":
                        board[row][i] = "."
                        i+=1
                    j = row +1
                    while j < n and board[j][col]=="X":
                        board[j][col] = "."
                        j+=1
                        
                    answer+=1

        return answer