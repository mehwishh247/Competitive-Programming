class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0

        result =[]
        for num in nums:
            if num!=0:
                result.append(num)
        result.extend([0]*(len(nums)-len(result)))
        
        return result
