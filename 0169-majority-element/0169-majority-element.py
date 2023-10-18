class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt = Counter(nums)
        
        keys = sorted(cnt.items(),key = lambda x:x[1])
        
        return keys[-1][0]