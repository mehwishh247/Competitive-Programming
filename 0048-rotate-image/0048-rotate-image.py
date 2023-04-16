class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        result =[] 
        for i in range(len(matrix[0])):
            row= []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            result.append(row)
        for row in range(len(matrix)):
            matrix[row]=result[row][::-1]