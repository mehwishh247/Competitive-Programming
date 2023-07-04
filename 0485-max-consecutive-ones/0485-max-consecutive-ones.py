class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
         
        ans=0
        n=len(nums)
        i = 0
        while i < n:
            if nums[i]==1:
                length = 1
                j = i + 1
                while j < n and nums[j]==1:
                    length += 1
                    j += 1
                ans= max(j-i,ans)
                i = j
            else:
                i += 1
        return ans
            
            
            
            
                    
       