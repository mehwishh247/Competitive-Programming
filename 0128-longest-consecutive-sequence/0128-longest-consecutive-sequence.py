class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        look  = set(nums)
        ans = float('-inf')
        
        for ele in nums:
            
            if ele-1 in look:
                continue
            
            start=ele
            while start in look:
                start+=1
            
            ans = max(ans,start-ele)
        
        
        return ans
                
            
        
        
        
        