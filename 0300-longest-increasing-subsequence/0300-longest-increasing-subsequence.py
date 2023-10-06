class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0]*n
        dp[0] = 1
        
        
        for i in range(1,n):
            temp_max = float('-inf')
            
            for j in range(i):
                if nums[i]>nums[j]: temp_max = max(temp_max,dp[j])

            dp[i] = temp_max + 1 if temp_max != float('-inf') else 1

        
        return max(dp)
                