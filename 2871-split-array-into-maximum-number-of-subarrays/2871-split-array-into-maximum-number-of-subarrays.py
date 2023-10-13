class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        score = 2**31-1
        count = 0
        
        for num in nums:
            if score & num == 0:
                count += 1
                score = 2**31-1
            else:
                
                score &= num
                
        return count if count != 0 else 1
                
        