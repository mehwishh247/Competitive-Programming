class Solution:
    
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=sorted_numbers = sorted(nums, key=lambda x: int(x))
        return nums[len(nums)-k]
            

