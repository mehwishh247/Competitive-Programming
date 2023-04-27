class Solution(object):
    def twoSum(self, nums, target):
        # counter=0
        tuples = []
        for i in range(len(nums)):
            tuples.append((nums[i],i))
        tuples.sort()
        low,hi=0,len(nums)-1
        while low<hi:
            tot = tuples[low][0]+tuples[hi][0] 
            if tot == target:
                return [tuples[low][1],tuples[hi][1]]
            if tot>target:
                hi-=1
            else:
                low+=1
        
        # return counter
        
        