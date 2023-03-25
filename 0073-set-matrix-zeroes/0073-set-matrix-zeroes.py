class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        placer = []
        for row in range(len(matrix)):
            c=False
            for col in range(len(matrix[0])):
                if matrix[row][col]==0:
                    c = True
                    placer.append(col)
            if c:
                matrix[row]=[0]*len(matrix[0])

        for col in placer:
            for r in range(len(matrix)):
                if matrix[r][col] !=0:
                    matrix[r][col]=0