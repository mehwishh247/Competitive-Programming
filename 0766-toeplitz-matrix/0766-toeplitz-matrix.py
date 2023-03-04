class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        count = 0
        for row in range(len(matrix)-1):
            first = matrix[row][0:-1]
            second = matrix[row+1][1::]
            if first!=second:
                return False
        return True
            
        
        