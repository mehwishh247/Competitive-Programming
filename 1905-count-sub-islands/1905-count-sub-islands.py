class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        
        def isValid(dr,matrix):
            return (0<=dr[0] < len(matrix)) and (0<=dr[-1] < len(matrix[0])) and  (matrix[dr[0]][dr[-1]]!=0 and matrix[dr[0]][dr[-1]]!=2)

        
        mainIs = []
        temp=set()

        def dfs(r,c,matrix):
            nonlocal temp
            temp.add((r,c))

            directions=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            matrix[r][c] = 2

            for dr in directions:
                if isValid(dr,matrix):
                    dfs(dr[0],dr[-1],matrix)
            return
        
        
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if isValid((row,col),grid2):
                    dfs(row,col,grid2)
                    mainIs.append(temp)
                    temp=set()
                    
                    
        ans=0
        for island in mainIs:
            i=0
            for points in island:
                if grid1[points[0]][points[1]]==0:
                    break
                i+=1
            if i==len(island):
                ans+=1
                
                    
        
        return ans