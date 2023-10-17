class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        @cache
        def dfs(idx,sign):
            
            if idx==n:
                return 0
            
            curr = nums[idx] if sign==1 else (-1*nums[idx])
            
            pick = dfs(idx+1,sign)
            notpick = dfs(idx+1,-1*sign)
            
            return max(curr+notpick,pick)
                
        return dfs(0,1)