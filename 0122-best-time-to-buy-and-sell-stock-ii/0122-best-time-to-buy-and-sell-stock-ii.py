class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0
        n=len(prices)
        
        for i in range(n-1):
            
            change=prices[i+1]-prices[i]
            
            if change>0:
                profit+=change
        
        return profit
                
                
        