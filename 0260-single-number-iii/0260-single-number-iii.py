class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        cnt = Counter(nums)
        
        for key in cnt.keys():
            if cnt[key]==1:
                ans.append(key)
        
        return ans
        
        