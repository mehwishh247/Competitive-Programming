class Solution(object):
    def targetIndices(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        result=[]
        for i in range(n):
            if nums[i]==target:
                result.append(i)
        return result