class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n,m = len(dungeon), len(dungeon[0])
        
            
        r = 1 - dungeon[-1][-1] 
        dungeon[-1][-1] = max(1,r)
    
        
        for i in range(m-2,-1,-1):
            r =  dungeon[-1][i+1] -  dungeon[-1][i] 
            dungeon[-1][i] = max(1,r)
        
        for j in range(n-2,-1,-1):

            r = dungeon[j+1][-1] - dungeon[j][-1]
            dungeon[j][-1] = max(1,r)
        
        for row in range(n-2,-1,-1):
            for col in range(m-2,-1,-1):
                
                r1 = dungeon[row+1][col] - dungeon[row][col]
                r2 = dungeon[row][col+1] - dungeon[row][col]
                
                dungeon[row][col] = 1 if (r1<=0 or r2<=0) else min(r1,r2)
                
        return dungeon[0][0]
            
            
            
    
       