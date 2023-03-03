class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if mid <= 0 or mid >= len(nums)-1:
                return nums[mid]
            if (mid-low) % 2 == 0:  # even number of elements to the left
                if nums[mid] == nums[mid-1]: # same with left go left
                    high = mid-2
                elif nums[mid] == nums[mid+1]: # same with right go right
                    low = mid+2
                else:
                    return nums[mid]
            else: # odd number of elements to the left
                if nums[mid] == nums[mid-1]: # same with left go right
                    low = mid+1
                elif nums[mid] == nums[mid+1]: # same with right go left
                    high = mid-1
                else:
                    return nums[mid]   
            
        return nums[low]
