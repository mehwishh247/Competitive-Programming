class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        pre_sum = []
        pre_sum.append(0)
        pre_sum.append(nums[0])

        for i in range(1,len(nums)):
            pre_sum.append(pre_sum[-1]+nums[i])
        
        min_len = float("inf")
        j=0
        i=1
        
        while i< len(pre_sum):
            dc = pre_sum[i]-pre_sum[j]
            if dc<target:
                i+=1
            else:
                min_len = min(min_len,i-j)
                j+=1
        
        if min_len != float("inf"): return min_len
        return 0
    
    
    