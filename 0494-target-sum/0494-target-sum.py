class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
            
        n = len(nums)
        memo={}
        
        def dfs(ind,curr_sum):
            if ind==n:
                if curr_sum == target:
                    return 1
                else:
                    return 0
            if (ind,curr_sum) in memo:
                return memo[(ind,curr_sum)]
            
            positive = dfs(ind+1,curr_sum+nums[ind])
            negative = dfs(ind+1,curr_sum-nums[ind]) 
            
            memo[(ind,curr_sum)]= positive + negative
            
            return positive+negative
        
        return dfs(0,0)


