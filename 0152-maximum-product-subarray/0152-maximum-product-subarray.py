class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre = post = 1
        currMax = -11

        for i in range(n):
            
            
            if pre==0: pre=1
            if post==0: post=1
                
            pre *=nums[i]
            post*= nums[n-i-1]
            
            possible = max(pre,post)
            currMax = max(currMax,possible)
        
        return currMax
                
                
            
        
        
        