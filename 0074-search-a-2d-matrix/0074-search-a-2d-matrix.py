class Solution:
    def rowTeller(self,matrix,target):
        l,h=0, len(matrix)-1
        while l<=h:
            mid = l + (h-l)//2
            if target<matrix[mid][0]:
                h=mid-1
            elif target>matrix[mid][-1]:
                l=mid+1
            else:
                return mid
        return -1
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            ansRow = self.rowTeller(matrix,target) 
            if ansRow == -1:
                return False
            left,right=0,len(matrix[ansRow])-1
            while left <= right:
                mid = left + (right-left)//2
                if matrix[ansRow][mid]==target:
                    return True
                elif matrix[ansRow][mid]<target:
                    left+=1
                else:
                    right-=1
            return False




    