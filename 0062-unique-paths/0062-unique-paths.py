class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
#         ans = [[1]*n]*m
        
#         for i in range(m-2,-1,-1):
#             for j in range(n-2,-1,-1):
#                 ans[i][j] = ans[i+1][j]+ans[i][j+1]
            
#         return ans[0][0]

        @cache
        def uniquePath(point):

            if point ==(m-1,n-1):
                return 1

            row,col = point

            ways=0

            if row+1<m:
                ways+=uniquePath((row+1,col))
            if col+1<n:
                ways+=uniquePath((row,col+1))

            return ways

        return uniquePath((0,0))
    
    
    

        
        
        
        
    
    