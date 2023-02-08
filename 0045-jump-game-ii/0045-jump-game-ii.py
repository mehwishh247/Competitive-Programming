class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        end = 0
        maxReach = 0
        n = len(nums)
        for i in range(n - 1):
            maxReach = max(maxReach, i + nums[i])
            if i == end:
                step += 1
                end = maxReach
        return step




