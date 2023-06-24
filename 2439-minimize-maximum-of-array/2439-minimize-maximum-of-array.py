class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        
        n  = len(nums)
        tot = 0
        ans = 0
        
        for i in range(n):
            
            tot+=nums[i]

            ans = max(ans,(tot+i)//(i+1))
        
        return int(ans)
    
    