class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low=0
        hi=len(nums)-1
        
        while low<=hi:
            mid = low + (hi-low)//2
            
            if nums[mid]==target:
                return mid
            if nums[mid]<=target:
                low+=1
            else:
                hi-=1
        return -1
        