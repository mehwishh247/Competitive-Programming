class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(nums,target):
            l,r=0,len(nums)-1
            
            while l<=r:
                mid = l + (r-l)//2
                if nums[mid]==target: return True
                if nums[mid]<=target: l = mid +1
                else: r=mid-1
            return False
        
        for row in range(len(matrix)):
            
            if binarySearch(matrix[row],target):
                return True
        return False
                

                        
                        
                