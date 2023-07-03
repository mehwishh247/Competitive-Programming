class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        if nums==[0]:
            return 1
        
        i = 0
        total = 0
        n = len(nums)

        while i < n:
            if nums[i] != 0:
                i += 1
                continue

            j = i + 1
            while j < n and nums[j] == 0:
                j += 1

            ele = j - i
            total+= ele*(ele+1)/2

            i = j


        return int(total)
    


        
        
            
        