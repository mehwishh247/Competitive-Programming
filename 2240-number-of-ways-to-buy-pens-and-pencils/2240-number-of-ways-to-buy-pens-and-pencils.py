class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        a = max(cost1,cost2)
        b = min(cost1,cost2)
        
        loopNum = total//a
        ans = 0
        
        for i in range(loopNum+1):
            
            maxRange = (total-a*i)//b
            ans += maxRange+1
            
        return ans
            
            
            
            