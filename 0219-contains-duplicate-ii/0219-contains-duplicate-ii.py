class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)    
        init = nums[:k+1]
        
        if len(init) != len(set(init)):
            return True
        
        seen = set()
        for ele in init:
            seen.add(ele)
        
        for i in range(k+1,n):
            seen.discard(nums[i-k-1])
            if nums[i] in seen:
                return True
            seen.add(nums[i])
              
        return False
                
        
        
        