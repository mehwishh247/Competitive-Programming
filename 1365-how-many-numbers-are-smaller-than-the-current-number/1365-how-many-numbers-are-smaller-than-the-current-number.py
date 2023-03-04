class Solution(object):
        def smallerNumbersThanCurrent(self, nums):
            count = defaultdict(int)
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j and nums[i]>nums[j]:
                        count[i]+=1
            result=[]
            for k in range(len(nums)):
                if k in count:
                    result.append(count[k])
                else:
                    result.append(0)
            return result
