class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        '''
        
        n = len(nums)        
        distincts = set(nums)

        if len(distincts) == n:
            return False
        
        return True