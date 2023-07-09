class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        distincts = set(nums)
        
        
        if len(distincts)!=len(nums):
            return True
        
        return False