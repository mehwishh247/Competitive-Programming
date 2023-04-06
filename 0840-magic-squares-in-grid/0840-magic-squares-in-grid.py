class Solution:
    def numMagicSquaresInside(self, matrix: List[List[int]]) -> int:
            if len(matrix)<3 or len(matrix[0])<3:
                return 0
            count = 0
            for row in range(len(matrix)-2):
                for col in range(len(matrix[0])-2):
                    pos = [matrix[row][col],matrix[row][col+1],matrix[row][col+2],matrix[row+1][col],matrix[row+1][col+1],matrix[row+1][col+2],matrix[row+2][col],matrix[row+2][col+1],matrix[row+2][col+2],]
                    
                    if len(set(pos))==9 and max(pos)<=9 and min(pos)>=1:
                        if pos[0]+pos[1]+pos[2]==pos[3]+pos[4]+pos[5] and pos[3]+pos[4]+pos[5]==pos[6]+pos[7]+pos[8]:
                            if pos[0]+pos[3]+pos[6] == pos[1]+pos[4]+pos[7] and pos[1]+pos[4]+pos[7] == pos[2]+pos[5]+pos[8]:
                                if pos[0]+pos[8] == pos[2]+pos[6]:
                                    count+=1
            return count
                    
        