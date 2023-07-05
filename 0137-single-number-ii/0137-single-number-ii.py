class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        cnt = Counter(nums)
        
        for key in cnt.keys():
            if cnt[key]==1:
                return key
        