class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.original = image[sr][sc]
        def isValid(dr):
            return (0<=dr[0] < len(image)) and (0<=dr[-1] < len(image[0])) and  (image[dr[0]][dr[-1]]!=color and image[dr[0]][dr[-1]]== self.original)

        def dfs(r,c):
            directions=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            image[r][c] = color
            
            for dr in directions:
                if isValid(dr):
                    dfs(dr[0],dr[-1])
            return
        dfs(sr,sc)
        return image