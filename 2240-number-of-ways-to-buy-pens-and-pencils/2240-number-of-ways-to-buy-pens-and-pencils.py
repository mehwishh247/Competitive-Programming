class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        loopNum = total//max(cost1,cost2)
        
        ans = 0
        
        for i in range(loopNum+1):
            
            maxRange = (total-max(cost1,cost2)*i)//min(cost1,cost2)
            
            ans += maxRange+1
            
        return ans
            
            
            
            