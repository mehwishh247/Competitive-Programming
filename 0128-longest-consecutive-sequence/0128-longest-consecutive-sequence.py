class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_ans = 1
        nums.sort()
        
        i,j=0,1

        while j<len(nums):


            if abs(nums[j]-nums[j-1])<=1:
                j+=1
            else:

                pos = len(set(nums[i:j]))
                i=j
                j+=1

                max_ans = max(max_ans,pos)
        
        pos = len(set(nums[i:j]))
        max_ans = max(max_ans,pos)

        return max_ans
        
        