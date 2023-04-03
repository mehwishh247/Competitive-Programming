class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix[0])
        n = len(matrix)
        left = 0
        right = len(matrix[0])-1
        top=0
        bottom = len(matrix)-1
        res=[]
        while left<=right and top<=bottom:
            
            for j in range(left,right+1):
                res.append(matrix[top][j])
            for i in range(top+1,bottom+1):
                res.append(matrix[i][right])
            if top<bottom:
                for j in range(right-1,left-1,-1):
                    res.append(matrix[bottom][j])
            if left<right:  
                for i in range(bottom-1,top,-1):
                    res.append(matrix[i][left])
                
            left+=1
            right-=1
            top+=1
            bottom-=1
        return res
            
