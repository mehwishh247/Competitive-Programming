class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            cnt = Counter(board[row])
            for ele in cnt.keys():
                if  ele!="." and cnt[ele]>=2:
                    return False


        for i in range(len(board)):
            colm = [
                board[3][i],board[4][i],board[5][i],
                board[0][i],board[1][i],board[2][i],
                board[6][i],board[7][i],board[8][i]
                    ]
            cnt2 = Counter(colm)
            for ele in cnt2.keys():
                 if  ele!="." and cnt2[ele]>=2:
                    return False
        for row in range(0,len(board)-2,3):
            for col in range(0,len(board[0])-2,3):
                pos=[]
                pos.extend(board[row][col:col+3])
                pos.extend(board[row+1][col:col+3])
                pos.extend(board[row+2][col:col+3])

                cnt3 = Counter(pos)
                for ele in cnt3.keys():
                    if  ele!="." and cnt3[ele]>=2:
                        return False

        return True