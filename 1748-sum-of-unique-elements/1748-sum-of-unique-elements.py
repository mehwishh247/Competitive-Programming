class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        tot=0
        cnt = Counter(nums)
        for num in nums:
            if cnt[num]==1:
                tot+=num
        return tot
        