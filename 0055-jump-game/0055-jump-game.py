class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]
        for i in range(1, len(nums)):
            if max_jump <= 0:
                return False
            max_jump = max(max_jump - 1, nums[i])
        return True