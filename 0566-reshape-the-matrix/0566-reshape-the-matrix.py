class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        if row*col != r*c:
            return mat
        result =[]
        src=[]
        for i in range(row):
            src.extend(mat[i])
        m=0
        while m<len(src):
            ned = src[m:m+c]
            result.append(ned)
            m+=c
        return result
            
            