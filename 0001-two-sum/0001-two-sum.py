from itertools import combinations

class Solution(object):

    def twoSum(self, nums, target):
        pairs = combinations(nums, 2)
        
        for i in pairs:
            if sum(i) == target:
                return i
