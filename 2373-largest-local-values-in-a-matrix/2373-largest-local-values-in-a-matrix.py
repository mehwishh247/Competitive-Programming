class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maweda= []
        n=len(grid)
        for k in range(n):
            temp=[]
            for i in range(n-2):
                maxi=max(grid[k][i],grid[k][i+1],grid[k][i+2])
                temp.append(maxi)
            maweda.append(temp)
        ans=[]
        for k in range(n-2):
            temp=[]
            for i in range(n-2):
                maxi=max(maweda[k][i],maweda[k+1][i],maweda[k+2][i])
                temp.append(maxi)
            ans.append(temp)
        return ans
        