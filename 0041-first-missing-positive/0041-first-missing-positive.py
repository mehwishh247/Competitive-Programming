class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):           
            while nums[i] != i + 1 and (0 < nums[i] <= n) and nums[i] != nums[nums[i] - 1]:
                # print(i, nums[i] -1)
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
                # print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1