class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        preSum = sum(nums[:k])
        curSum=preSum
        for i in range(k,len(nums)):
            preSum-=nums[i-k]
            preSum+=nums[i]
            curSum=max(curSum,preSum)
        return curSum/k
            