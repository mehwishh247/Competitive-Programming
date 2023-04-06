class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        cnt = set(nums) 
        for i in nums:
            cnt.add(int(str(i)[::-1]))
        return len(cnt)
        
        
        